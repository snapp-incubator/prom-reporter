from schema import Schema, Optional, And, Use, Or
import json

config_schema = Schema(
    {
        "prometheus": dict,
        "queries": [
            {"name": str, Optional("legend"): str, "operation": str, "query": str}
        ],
    }
)

output_schema = Schema(
    And(Use(json.loads)),
    [{"name": str, "timestamp": str, "value": Or(float, int, str)}],
)
