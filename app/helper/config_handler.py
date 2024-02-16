import yaml
import os
from .logger import logger
from .schemas import config_schema
import schema

class ConfigHandler:
    def __init__(self):
        self.output_path = os.getenv("OUTPUT_PATH", "/tmp/result.json")
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
        # Read the YAML file
        yaml_content = self._load_yaml(self._config_path)
        if not self.validate_yaml_with_schema(yaml_content, config_schema):
            logger.error("Schema is not vald")
            raise
        return yaml_content

    @staticmethod
    def validate_yaml_with_schema(yaml_data, schema_data):
        try:
            schema_data.validate(yaml_data)
            logger.info("Validation successful!")
            return True
        except schema.SchemaError as e:
            logger.error(f"Schema validation error: {e}")
            return False
