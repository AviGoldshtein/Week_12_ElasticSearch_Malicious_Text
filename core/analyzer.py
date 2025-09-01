from core.elastic_connector import ElasticConnector
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from core.logger import logger
from dateutil import parser
import pandas as pd
import os
import nltk
import json
import re



nltk_dir = "/tmp/nltk_data"
os.makedirs(nltk_dir, exist_ok=True)
nltk.data.path.append(nltk_dir)
nltk.download('vader_lexicon', download_dir=nltk_dir, quiet=True)



class Analyzer:
    def  __init__(self, df: pd.DataFrame, index_name: str):
        self.logger = logger
        self.es_connector = ElasticConnector()
        self.df = df
        self.index_name = index_name

    def create_index_and_mapping(self, index_name):
        self.logger.debug("create_index_mapping")
        mapping = {
            'properties': {
                'TweetID': {
                    'type': 'keyword'
                },
                'CreateDate': {
                    'type': 'date',
                    "format": "strict_date_optional_time||epoch_millis"
                },
                'Antisemitic': {
                    'type': 'boolean'
                },
                'text': {
                    'type': 'text',
                    'fields': {
                        'keyword': {
                            'type': 'keyword',
                            'ignore_above': 256
                        }
                    }
                },
                'sentiment': {
                    'type': 'keyword'
                },
                'weapons_detected': {
                    'type': 'keyword'
                }
            }
        }
        self.es_connector.create_index(index_name, mappings=mapping)

    def insert_data_to_es(self, index_name):
        self.logger.debug("insert_data_to_es")
        documents = self.df.to_dict(orient="records")
        normalized_documents = [self._normalize_document(doc) for doc  in documents]

        self._insert_documents(index_name, normalized_documents)
        # print(json.dumps(normalized_documents[:10], indent=4))

    def find_sentiments(self):
        self.logger.debug("find_sentiments")
        all_documents = self.es_connector.get_all_documents(index_name=self.index_name)
        for doc in all_documents:
            sentiment = self._find_sentiment(doc['_source'])

            self.es_connector.update_document(
                index=doc['_index'],
                id=doc['_id'],
                body= {
                    "doc": {
                        "sentiment": sentiment
                    }
                }
            )


    def find_detected_weapons(self):
        self.logger.debug("find_detected_weapons")

    def delete_non_relevant_rows(self):
        self.logger.debug("delete_non_relevant_rows")


    def _insert_documents(self, index_name, documents):
        for doc in documents:
            pass
            self.es_connector.insert_document(index_name, doc)
    def _normalize_document(self, doc):
        doc['TweetID'] = str(doc['TweetID'])
        doc['Antisemitic'] = bool(doc['Antisemitic'])
        doc['CreateDate'] = self._proper_date(doc['CreateDate'])
        doc['sentiment'] = ""
        doc['weapons_detected'] = []
        return doc
    def _proper_date(self, date: str) -> str:
        dt = parser.parse(date)
        return dt.isoformat()
    def _find_sentiment(self, doc):
        txt = doc['text']
        score = SentimentIntensityAnalyzer().polarity_scores(txt)
        compound = score['compound']
        if compound <= -0.5:
            return "negative"
        elif compound < 0.5:
            return "neutral"
        else:
            return "positive"

