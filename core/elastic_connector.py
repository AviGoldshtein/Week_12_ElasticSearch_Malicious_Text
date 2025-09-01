from elasticsearch import Elasticsearch
from core.data_loader import DataLoader
import os
import json


class ElasticConnector:
    def __init__(self):
        host = os.getenv("ELASTIC_HOST", "localhost")
        port = os.getenv("ELASTIC_PORT", "9200")
        self.es = Elasticsearch(f'http://{host}:{port}')
        self.data_loader = DataLoader()

    def get_all_documents(self, index_name):
        res = self.es.search(index=index_name, body={"query": {"match_all": {}}}, size=10000)
        return res['hits']['hits']

    def get_problematic_docs(self, index_name):
        black_list = self.data_loader.get_black_list()
        query_string = " ".join(black_list)

        query = {
            "query": {
                "multi_match": {
                    "query": query_string,
                    "fields": ["text"]
                }
            }
        }
        return self.es.search(index=index_name, body=query)['hits']['hits']

    def create_index(self, index_name, mappings):
        if not self.es.indices.exists(index=index_name):
            self.es.indices.create(index=index_name, mappings=mappings)

    def insert_document(self, index_name, doc):
        self.es.index(index=index_name, document=doc)

    def update_document(self, index, id, body):
        self.es.update(
            index=index,
            id=id,
            body=body
        )
