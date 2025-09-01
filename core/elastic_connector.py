from core.data_loader import DataLoader
from elasticsearch import Elasticsearch
import os


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
        print(black_list)

        query = {
            "query": {
                "terms": {
                    "text": black_list
                }
            }
        }
        return self.es.search(index=index_name, body=query, size=10000)['hits']['hits']
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
    def delete_by_query(self,index, query):
        response = self.es.delete_by_query(
            index=index,
            body=query,
            conflicts="proceed"
        )
        print(response)
    def refresh_index(self, index_name):
        self.es.indices.refresh(index=index_name)
