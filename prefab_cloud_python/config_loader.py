import glob
import os
from .yaml_parser import YamlParser
import prefab_pb2 as Prefab

class ConfigLoader:
    def __init__(self, base_client):
        self.base_client = base_client
        self.options = base_client.options
        self.highwater_mark = 0
        self.__load_classpath_config()
        self.__load_local_overrides()
        self.api_config = {}

    def calc_config(self):
        return self.classpath_config | self.api_config | self.local_overrides

    def set(self, config, source):
        existing_config = self.api_config.get(config.key)
        if existing_config and existing_config["config"].id >= config.id:
            return

        if len(config.rows) == 0 and config.key in self.api_config:
            self.api_config.pop(config.key)
        else:
            if existing_config:
                self.base_client.logger().debug("Replace %s with value from %s %s -> %s" % (config.key, source, existing_config["config"].id, config.id))
            self.api_config[config.key] = {"source": source, "config": config}
        self.highwater_mark = max([config.id, self.highwater_mark])

    def get_api_deltas(self):
        configs = Prefab.Configs()
        for config_value in self.api_config.values():
            configs.configs.append(config_value["config"])
        return configs

    def __load_classpath_config(self):
        classpath_dir = self.options.prefab_config_classpath_dir
        self.classpath_config = self.__load_config_from(classpath_dir)

    def __load_local_overrides(self):
        override_dir = self.options.prefab_config_override_dir
        self.local_overrides = self.__load_config_from(override_dir)

    def __load_config_from(self, dir):
        envs = self.options.prefab_envs
        envs.insert(0, "default")
        loaded_config = {}
        for env in envs:
            loaded_config.update(ConfigLoader.__load_glob(os.path.join(dir, ".prefab.%s.config.yaml" % env)))
        return loaded_config

    def __load_glob(filepath):
        rtn = {}
        for file in glob.glob(filepath):
            rtn = rtn | YamlParser(file).data
        return rtn
