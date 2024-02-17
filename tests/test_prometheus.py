from unittest.mock import patch, Mock
from prometheus_api_client import MetricSnapshotDataFrame
from app.helper.prometheus import Prometheus


@patch(
    "app.helper.prometheus.PrometheusConnect.check_prometheus_connection",
    Mock(return_value=True),
)
@patch(
    "app.helper.prometheus.PrometheusConnect.custom_query",
    Mock(
        return_value=[
            {
                "metric": {"__name__": "dummy_metric"},
                "value": [1708184035.052, "0.29875"],
            }
        ]
    ),
)
def test_prometheus():
    prometheus = Prometheus(url="dummy_url")
    result = prometheus.get_current_value("dummy_query")
    assert type(result) == MetricSnapshotDataFrame
