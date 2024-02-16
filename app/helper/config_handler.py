import yaml
import os
from .logger import logger
from .config_schema import config_schema
import schema

class ConfigHandler:
    def __init__(self):
        self._config_path = os.environ["CONFIG_PATH"]
        if not os.path.exists(self._config_path):
            logger.error("Config file not found in path {}".format(self._config_path))
            exit(1)

    @staticmethod
    def _load_yaml(file_path):
        with open(file_path, "r") as file:
            return yaml.safe_load(file)

    def config_parser(self):
        # Initialize an empty list to hold the queries
        queries_list = []
        # Read the YAML file
        yaml_content = self._load_yaml(self._config_path)
        if not self.validate_yaml_with_schema(yaml_content, config_schema):
            logger.error("Schema is not vald")
            raise
        # Iterate through each spec item
        for item in yaml_content["spec"]:
            # Check if 'legend' is not specified and set it to an empty string if so
            if "legend" not in item:
                item["legend"] = ""
            # Append the modified item to the queries_list
            queries_list.append(item)
        return queries_list

    @staticmethod
    def validate_yaml_with_schema(yaml_data, schema_data):
        try:
            schema_data.validate(yaml_data)
            logger.info("Validation successful!")
            return True
        except schema.SchemaError as e:
            logger.error(f"Schema validation error: {e}")
            return False
