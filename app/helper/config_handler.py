import yaml
from .logger import logger
from .schemas import config_schema
import schema


class ConfigHandler:
    @staticmethod
    def _load_yaml(file_path):
        with open(file_path, "r") as file:
            return yaml.safe_load(file)

    @staticmethod
    def validate_yaml_with_schema(yaml_data, schema_data):
        try:
            schema_data.validate(yaml_data)
            logger.info("validation successful!")
            return True
        except schema.SchemaError as e:
            logger.error(f"schema validation error: {e}")
            return False

    def parse_config(self, config_path):
        yaml_content = self._load_yaml(config_path)
        if not self.validate_yaml_with_schema(yaml_content, config_schema):
            logger.error("config schema is not valid")
            raise
        return yaml_content
