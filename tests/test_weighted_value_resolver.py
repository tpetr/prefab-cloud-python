from prefab_cloud_python.weighted_value_resolver import WeightedValueResolver
import prefab_pb2 as Prefab
import pytest

key = "config_key"

class TestWeightedValueResolver:
    def test_resolving_a_single_value(self):
        weighted_values = self.build_weighted_values({"abc": 1})

        resolved = WeightedValueResolver(weighted_values, key).resolve()
        assert resolved.value.string == "abc"

    def test_multiple_values_with_even_distribution(self):
        weighted_values = self.build_weighted_values({"abc": 1, "def": 1})

        resolved = WeightedValueResolver(weighted_values, key, "user:001").resolve()
        assert resolved.value.string == "abc"

        resolved = WeightedValueResolver(weighted_values, key, "user:456").resolve()
        assert resolved.value.string == "def"

    def test_multiple_values_with_uneven_distribution(self):
        weighted_values = self.build_weighted_values({"abc": 1, "def": 98, "ghi": 1})
        resolved = WeightedValueResolver(weighted_values, key, "user:456").resolve()
        assert resolved.value.string == "def"

        resolved = WeightedValueResolver(weighted_values, key, "user:103").resolve()
        assert resolved.value.string == "ghi"

        resolved = WeightedValueResolver(weighted_values, key, "user:119").resolve()
        assert resolved.value.string == "abc"

    def test_distribution_simulation(self):
        weighted_values = self.build_weighted_values({"abc": 1, "def": 98, "ghi": 1})
        results = {}
        for i in range(10_000):
            resolved = WeightedValueResolver(weighted_values, key, "user:%s" % i).resolve()
            result = resolved.value.string
            if results.get(result) is None:
                results[result] = 1
            else:
                results[result] += 1

        assert results["abc"] == pytest.approx(100, 20)
        assert results["def"] == pytest.approx(9800, 50)
        assert results["ghi"] == pytest.approx(100, 20)

    @staticmethod
    def build_weighted_values(values_and_weights):
        weighted_values = []
        for value in values_and_weights:
            weighted_value = Prefab.WeightedValue(
                value=Prefab.ConfigValue(string=value),
                weight=values_and_weights[value]
            )
            weighted_values.append(weighted_value)
        return weighted_values

