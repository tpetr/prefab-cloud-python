from .config_loader import ConfigLoader
from .config_resolver import ConfigResolver
from .read_write_lock import ReadWriteLock
from .config_value_unwrapper import ConfigValueUnwrapper

import grpc
import threading
import time
import urllib3
import base64
import prefab_pb2 as Prefab
import prefab_pb2_grpc as PrefabGrpc
import concurrent.futures
import functools

class InitializationTimeoutException(Exception):
    def __init__(self, timeout_seconds, key):
        super().__init__(f"Prfeab couldn't initialize in {timeout_seconds} second timeout. Trying to fetch key `{key}`.")


class MissingDefaultException(Exception):
    def __init__(self, key):
        super().__init__(f"""No value found for key '{key}' and no default was provided.

If you'd prefer returning `None` rather than raising when this occurs, modify the `on_no_default` value you provide in your Options.""")


class ConfigClient:
    def __init__(self, base_client, timeout):
        base_client.logger().info("Initializing ConfigClient")
        self.base_client = base_client
        self.options = base_client.options
        self.timeout = timeout

        self.stream_lock = ReadWriteLock()
        self.init_lock = ReadWriteLock()

        self.checkpoint_freq_secs = 60

        self.config_loader = ConfigLoader(base_client)
        self.config_resolver = ConfigResolver(base_client, self.config_loader)

        self.base_client.logger().debug("Initialize ConfigClient: acquire write lock")
        self.init_lock.acquire_write()
        self.base_client.logger().debug("Initialize ConfigClient: acquired write lock")
        self.init_future = concurrent.futures.ThreadPoolExecutor().submit(lambda: self.init_lock.acquire_read())

        if self.options.is_local_only():
            self.finish_init("local only")
        else:
            self.load_checkpoint()
            self.start_checkpointing_thread()
            self.start_streaming()

    def get(self, key, default="NO_DEFAULT_PROVIDED", properties={}, lookup_key=None):
        value = self.__get(key, lookup_key, properties)
        if value is not None:
            return ConfigValueUnwrapper.unwrap(value, key, properties)
        else:
            return self.handle_default(key, default)

    def __get(self, key, lookup_key, properties):
        self.init_future.result(self.options.connection_timeout_seconds)
        if not self.init_future.done():
            if self.options.on_connection_failure == "RAISE":
                raise InitializationTimeoutException(self.options.connection_timeout_seconds, key)
            self.base_client.logger().warn(f"Couldn't initialize in {self.options.connection_timeout_seconds}. Key {key}. Returning what we have.")
            self.init_lock.release_write()
        return self.config_resolver.get(key, lookup_key, properties)

    def handle_default(self, key, default):
        if default != "NO_DEFAULT_PROVIDED":
            return default
        if self.options.on_no_default == "RAISE":
            raise MissingDefaultException(key)
        return None

    def load_checkpoint(self):
        if self.load_checkpoint_from_api_cdn():
            return
        self.base_client.logger().info("load_checkpoint: fallback to GRPC API")
        if self.load_checkpoint_from_grpc_api():
            return
        self.base_client.logger().warn("No success loading checkpoints")

    def start_checkpointing_thread(self):
        threading.Thread(target=self.checkpointing_loop).start()

    def start_streaming(self):
        threading.Thread(target=self.grpc_stream).start()

    def grpc_stream(self):
        channel = self.grpc_channel()
        req = Prefab.ConfigServicePointer(start_at_id=self.config_loader.highwater_mark)
        stub = PrefabGrpc.ConfigServiceStub(channel)
        stream = stub.GetConfig(req, metadata=[("auth", self.options.api_key)])
        for resp in stream:
            self.load_configs(resp, "remote_api_grpc_stream")

    def checkpointing_loop(self):
        while True:
            try:
                self.load_checkpoint()
                time.sleep(self.checkpoint_freq_secs)
            except:
                self.base_client.logger().info("Issue Checkpointing")

    def load_checkpoint_from_api_cdn(self):
        url = "%s/api/v1/configs/0" % self.options.url_for_api_cdn
        auth = "%s:%s" % ("authuser", self.options.api_key)
        token = base64.b64encode(auth.encode("utf-8")).decode("ascii")
        headers = {"Authorization": "Basic %s" % token}
        response = urllib3.PoolManager().request("GET", url, headers=headers)
        if response.status == 200:
            configs = Prefab.Configs.FromString(response.data)
            self.load_configs(configs, "remote_api_cdn")
            return True
        else:
            self.base_client.logger().info(f"Checkpoint remote_cdn_api failed to load. Response {response.status}")
            return False

    def load_checkpoint_from_grpc_api(self):
        try:
            channel = self.grpc_channel()
            request = Prefab.ConfigServicePointer(start_at_id=self.config_loader.highwater_mark)
            stub = PrefabGrpc.ConfigServiceStub(channel)
            response = stub.GetAllConfig(request=request, metadata=[('auth', self.options.api_key)])
            self.load_configs(response, "remote_api_grpc")
        except Exception as ex:
            self.base_client.logger().warn("Unexpected error loading GRPC checkpoint %s" % ex)

    def load_configs(self, configs, source):
        project_id = configs.config_service_pointer.project_id
        project_env_id = configs.config_service_pointer.project_env_id
        self.config_resolver.project_env_id = project_env_id
        starting_highwater_mark = self.config_loader.highwater_mark
        for config in configs.configs:
            self.config_loader.set(config, source)
        if self.config_loader.highwater_mark > starting_highwater_mark:
            self.base_client.logger().info(f"Found new checkpoint with highwater id {self.config_loader.highwater_mark} from {source} in project {project_id} environment: {project_env_id} and namespace {self.base_client.options.namespace}")
        else:
            self.base_client.logger().debug(f"Checkpoint with highwater id {self.config_loader.highwater_mark} from {source}. No changes.")
        self.config_resolver.update()
        self.finish_init(source)

    def finish_init(self, source):
        if not self.init_lock._write_locked:
            return
        self.base_client.logger().info(f"Unlocked config via {source}")
        self.init_lock.release_write()

    @functools.cache
    def grpc_channel(self):
        creds = grpc.ssl_channel_credentials()
        return grpc.secure_channel(self.options.prefab_grpc_url, creds)
