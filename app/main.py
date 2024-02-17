from helper.config_handler import ConfigHandler
from helper.prometheus import Prometheus
from helper.output_handler import OutputHandler
import argparse
import os
from helper.logger import logger


def main(config_path: str, output_path: str):
    config_handler = ConfigHandler()
    output_handler = OutputHandler()
    config = config_handler.parse_config(config_path)
    prometheus = Prometheus(**config["prometheus"])

    dfs = []
    for item in config["queries"]:
        df = prometheus.get_current_value(query=item["query"])
        if "legend" not in item.keys():
            item["legend"] = ""
        df = output_handler.prune_metric(df, item["name"], item["legend"])
        dfs.append(df)

    final_df = output_handler.concat_items(dfs)
    result = output_handler.save(final_df, output_path)
    if not output_handler.validate(result):
        logger.error("output schema is not valid")
        raise


if __name__ == "__main__":
    # get arguments
    parser = argparse.ArgumentParser(description="Prometheus Reporter")
    parser.add_argument(
        "-c",
        "--config-path",
        type=str,
        help="specify the configuration file path",
        required=True,
        dest="config_path",
    )
    parser.add_argument(
        "-o",
        "--output-path",
        type=str,
        help="specify the output file path",
        required=False,
        default="/tmp/output.json",
        dest="output_path",
    )
    args = parser.parse_args()
    config_path = args.config_path
    output_path = args.output_path

    if not config_path:
        logger.error("config path is not specified")
        exit(1)
    if not os.path.exists(config_path):
        logger.error("config file not found in path {}".format(config_path))
        exit(1)

    main(config_path, output_path)
