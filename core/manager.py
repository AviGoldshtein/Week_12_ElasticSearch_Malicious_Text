from core.data_loader import DataLoader
from core.elastic_connector import ElasticConnector
from core.logger import logger
from core.analyzer import Analyzer


class Manager:
    def __init__(self):
        self.logger = logger
        self.data_loader = DataLoader()
        self.es_connector = ElasticConnector()

    def initialize_data(self):
        self.logger.debug("initialize_data")
        df = self.data_loader.load_data()
        analyzer = Analyzer(df, index_name="malicious")
        analyzer.create_index_and_mapping(index_name="malicious")
        analyzer.insert_data_to_es(index_name="malicious")
        analyzer.find_sentiments()
        analyzer.find_detected_weapons()
        analyzer.delete_non_relevant_rows()
    def get_all_data(self):
        documents = self.es_connector.get_all_documents(index_name="malicious")
        return [doc['_source'] for doc in documents]
    def get_all_data_more_weapons(self):
        data = self.get_all_data()
        return [doc for doc in data if len(doc['weapons_detected']) >= 2]
