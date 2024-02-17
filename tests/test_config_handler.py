from app.helper.config_handler import ConfigHandler
import pytest


def test_config_handler_correct():
    config_handler = ConfigHandler()
    expected_data = {
        "prometheus": {"url": ""},
        "queries": [
            {
                "name": "Node Load Average",
                "legend": "instance",
                "operation": "lastValue",
                "query": "node:load_average:5m{}",
            },
            {
                "name": "Memory Usage",
                "legend": "pod",
                "operation": "lastValue",
                "query": "sum(container_memory_working_set_bytes{}) by (pod)",
            },
        ],
    }
    data = config_handler.parse_config(config_path="tests/config.yaml")
    assert expected_data == data


def test_config_handler_wrong():
    with pytest.raises(Exception):
        config_handler = ConfigHandler()
        _ = config_handler.parse_config(config_path="tests/config_wrong.yaml")
