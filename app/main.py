from helper.config_handler import ConfigHandler
from helper.prometheus import Prometheus
from helper.output_handler import OutputHandler
import argparse
import os
from helper.logger import logger

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prometheus Reporter")
    parser.add_argument("-c", "--config-path", type=str, help="specify the configuration file path", required=True, dest='config_path')
    args = parser.parse_args()
    config_path = args.config_path
    if not config_path:
        logger.error("config path is not specified")
        exit(1)
    if not os.path.exists(config_path):
        logger.error("config file not found in path {}".format(config_path))
        exit(1)
    
    config_handler = ConfigHandler()
    config = config_handler.config_parser(config_path)

    output_handler = OutputHandler()

    prometheus = Prometheus(**config["prometheus"])
    dfs = []
    for item in config["queries"]:
        df = prometheus.get_current_value(query=item["query"])
        if "legend" not in item.keys():
            item["legend"] = ""
        df = output_handler.prune_metric(df, item["name"], item["legend"])
        dfs.append(df)
    
    final_df = output_handler.concat_items(dfs)
    result = output_handler.save(final_df)
    print(output_handler.validate(result))