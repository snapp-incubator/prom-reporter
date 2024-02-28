from .schemas import output_schema
import pandas as pd
from .logger import logger


class OutputHandler:
    # convert raw result to a template suited for the final json result
    def prune_metric(self, df: pd.DataFrame, name: str, legend: str) -> pd.DataFrame:
        if legend in df.columns:
            df["name"] = df[legend].apply(lambda x: f"{name}: {x}")
        else:
            df["name"] = name

        columns_to_keep = ["timestamp", "name", "value"]
        df = df[columns_to_keep]
        return df

    def concat_items(self, dfs: list[pd.DataFrame]):
        return pd.concat(dfs, ignore_index=True)

    def validate(self, data_json) -> bool:
        if not output_schema.validate(data_json):
            logger.error("output schema is not vald")
            raise
        return True

    def save(self, df: pd.DataFrame, output_path):
        json_str = df.to_json(
            orient="records",
            date_format="iso",
            date_unit="s",
        )
        with open(output_path, "w") as json_file:
            json_file.write(json_str)
        return json_str
