from prometheus_api_client import PrometheusConnect, PrometheusApiClientException
from requests import RequestException
from .logger import logger

class Prometheus():
    def __init__(self, url, **kv):
        self.client = PrometheusConnect(url=url, **kv)
        if self.client.check_prometheus_connection():
            logger.info("connected to prometheus on {}".format(url))
        else:
            logger.error("couldn't connect to prometheus on {}".format(url))
            raise

    def get_current_value(self, query):
        try:
            result = self.client.custom_query(query)
        except RequestException:
            logger.error("connection error while handling query {}".format(query), stack_info=True)
        except PrometheusApiClientException:
            logger.error("non 200 response status code on query {}".format(query), stack_info=True)
        return result