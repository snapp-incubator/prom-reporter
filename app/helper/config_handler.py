import yaml
import os
from .logger import logger
from .schemas import config_schema
import schema

class ConfigHandler:
    def __init__(self):
        self.output_path = os.getenv("OUTPUT_PATH", "/tmp/result.json")

    @staticmethod
    def _load_yaml(file_path):
        with open(file_path, "r") as file:
            return yaml.safe_load(file)

    def config_parser(self, config_path):
        # Initialize an empty list to hold the queries
        # Read the YAML file
        yaml_content = self._load_yaml(config_path)
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
