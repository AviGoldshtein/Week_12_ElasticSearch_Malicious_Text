from elasticsearch import Elasticsearch
import os
import json


class ElasticConnector:
    def __init__(self):
        host = os.getenv("ELASTIC_HOST", "localhost")
        port = os.getenv("ELASTIC_PORT", "9200")
        self.es = Elasticsearch(f'http://{host}:{port}')

    def get_all_documents(self, index_name):
        res = self.es.search(index=index_name, body={"query": {"match_all": {}}}, size=10000)
        return res['hits']['hits']

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







# mapping = {
#     'properties': {
#         'TweetID': {
#             'type': 'keyword'
#         },
#         'CreateDate': {
#             'type': 'date'
#         },
#         'Antisemitic': {
#             'type': 'boolean'
#         },
#         'text': {
#             'type': 'text',
#             'fields': {
#                 'keyword': {
#                     'type': 'keyword',
#                     'ignore_above': 256
#                 }
#             }
#         }
#     }
# }


# es = Elasticsearch('http://localhost:9200')
# # es.indices.create(index="my_index", mappings=mapping)
#
# index_mapping = es.indices.get_mapping(index='my_index')
# # print(type(index_mapping["my_index"]["mappings"]["properties"]))
# res = dict(index_mapping)
# print(json.dumps(res, indent=4))