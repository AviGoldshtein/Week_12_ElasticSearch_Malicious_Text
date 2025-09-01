from core.elastic_connector import ElasticConnector
import pandas as pd
from core.logger import logger


class Analyzer:
    def  __init__(self, df: pd.DataFrame):
        self.logger = logger
        self.es_connector = ElasticConnector()
        self.df = df

    def create_mapping_and_insert_to_es(self):
        self.logger.debug("create_mapping_and_insert_to_es")
        # self.es_connector.create_index("@@@@@@@@@@@@@@@")
        # create the mapping

    def find_sentiments(self):
        self.logger.debug("find_sentiments")

    def find_detected_weapons(self):
        self.logger.debug("find_detected_weapons")

    def delete_non_relevant_rows(self):
        self.logger.debug("delete_non_relevant_rows")