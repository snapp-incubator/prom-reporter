from schema import Schema, Optional

config_schema = Schema({
    "spec": [{
        "name": str,
        Optional("legend"): str,
        "operation": str,
        "query": str
 } ]
})