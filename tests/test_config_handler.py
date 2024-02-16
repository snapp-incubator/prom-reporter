from dotenv import load_dotenv
from app.helper.config_handler import ConfigHandler
from app.helper.prometheus import Prometheus
import pytest
from unittest.mock import patch, Mock

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

@patch('app.helper.prometheus.PrometheusConnect.check_prometheus_connection', Mock(return_value=True))
@patch('app.helper.prometheus.PrometheusConnect.custom_query', Mock(return_value=50))
def test_prometheus():
    prometheus = Prometheus(url='')
    result = prometheus.get_current_value("dummy_query")
    assert result == 50

    