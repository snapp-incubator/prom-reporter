from schema import Schema, Optional

config_schema = Schema(
    {
        "spec": {
            "prometheus": dict,
            "queries": [
                {"name": str, Optional("legend"): str, "operation": str, "query": str}
            ],
        }
    }
)
