from dotenv import load_dotenv

from app.helper.config_handler import ConfigHandler
import pytest

load_dotenv("tests/test.env", override=True)

def test_config_handler_correct():
    config_handler = ConfigHandler()
    expected_data = {'spec': {'prometheus': {'url': ''}, 'queries': [{'name': 'Node Load Average', 'legend': 'instance', 'operation': 'lastValue', 'query': 'node:load_average:5m{}'}, {'name': 'Memory Usage', 'legend': 'pod', 'operation': 'lastValue', 'query': 'sum(container_memory_working_set_bytes{}) by (pod)'}]}}
    data = config_handler.config_parser()
    assert expected_data == data

def test_config_handler_wrong():
    load_dotenv("tests/test_wrong.env", override=True)
    with pytest.raises(Exception):
        config_handler = ConfigHandler()
        _ = config_handler.config_parser()
