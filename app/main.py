from helper.config_handler import ConfigHandler
from helper.prometheus import Prometheus
from helper.output_handler import OutputHandler

if __name__ == "__main__":
    config_handler = ConfigHandler()
    config = config_handler.config_parser()

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