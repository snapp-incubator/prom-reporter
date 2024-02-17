from unittest.mock import patch, Mock
from app.main import main

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
def test_main():
    main(config_path="tests/config.yaml", output_path="tests/output.json")