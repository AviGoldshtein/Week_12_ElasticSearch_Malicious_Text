from elasticsearch import Elasticsearch


class ElasticConnector:
    def __init__(self, host='localhost', port='9200'):
        self.es = Elasticsearch(f'http://{host}:{port}')

    def create_index(self, index_name):
        if not self.es.indices.exists(index=index_name):
            self.es.indices.create(index=index_name)


