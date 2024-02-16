from dotenv import load_dotenv

from app.helper.config_handler import ConfigHandler
import pytest

load_dotenv("example.env", override=True)

def test_config_handler_correct():
    config_handler = ConfigHandler()
    expected_data = [{'name': 'Stream Publish Rate', 'legend': 'stream_name', 'operation': 'lastValue', 'query': 'rate(nats_stream_last_seq{stream_name="rides", namespace="nats-production"}[5m])'}, {'name': 'Golchin Consuming Rate', 'operation': 'lastValue', 'query': 'sum(rate(nats_consumer_delivered_consumer_seq{consumer_name=~".*golchin.*ride-started.*", namespace="nats-production"}[5m])) by (consumer_name)', 'legend': ''}, {'name': 'Node Load Average', 'legend': 'instance', 'operation': 'lastValue', 'query': 'node:load_average:5m{instance=~"^(okd4-worker-worker-2|okd4-worker-worker-71|okd4-worker-worker-91)"}'}, {'name': 'Pending Acks', 'legend': 'consumer_name', 'operation': 'lastValue', 'query': 'sum(nats_consumer_num_ack_pending{namespace="nats-production"}) by (stream_name,consumer_name) > 100'}, {'name': 'Consumer Redelivery', 'legend': 'consumer_name', 'operation': 'lastValue', 'query': 'rate(nats_consumer_num_redelivered{pod=~"js-nats-production-.*", stream_name=~"(callbacks|ride|scheduled_rides|scrooge|ginger|rides|authentication|cancellation_reason|danzer-ride-evidence|gabriel|guardian-actions|passenger-profile|santa)", namespace="nats-production"}[5m]) > 0'}, {'name': 'Memory Usage', 'legend': 'pod', 'operation': 'lastValue', 'query': 'sum(container_memory_working_set_bytes{pod=~"js-nats-production-.*"}) by (pod)'}]
    data = config_handler.config_parser()
    assert expected_data == data

def test_config_handler_wrong():
    load_dotenv("tests/example_wrong.env", override=True)
    with pytest.raises(Exception):
        config_handler = ConfigHandler()
        _ = config_handler.config_parser()
