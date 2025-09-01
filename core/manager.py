from core.data_loader import DataLoader
from core.logger import logger
from core.analyzer import Analyzer


class Manager:
    def __init__(self):
        self.logger = logger
        self.data_loader = DataLoader()

    def initialize_data(self):
        self.logger.debug("initialize_data")
        df = self.data_loader.load_data()
        analyzer = Analyzer(df)
        analyzer.create_mapping_and_insert_to_es()
        analyzer.find_sentiments()
        analyzer.find_detected_weapons()
        analyzer.delete_non_relevant_rows()