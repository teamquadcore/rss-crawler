import requests
import json
from bs4 import BeautifulSoup
from quadcore.config import Config
from quadcore.manager.data import DataManager as dm
from quadcore.manager.db import DBManager

class Extractor:
    """
    Extract entity from article and connect article with entity
    """
    db = DBManager.get_redis()
    @classmethod
    def __new__(cls, self, obj, token):
        category_list = cls.get_entities(obj, token)
        cls.article_entity_relation(obj, category_list)

    @classmethod
    def get_entities(cls, obj, token, confidence=0.1, lang='en'):        
        category_list = list()
        payload = {
            'token': token,
            'url': obj.link,
            'confidence': confidence,
            'lang': lang,
        }
              
        response = requests.get(Config.dandelion_url, params=payload)        
        category_list = cls.get_category_list(response.json())
        
        return category_list

    @classmethod
    def get_category_list(cls, data):
        category_list = list()
        
        if "annotations" in data:
            for annotation in data['annotations']:
                category_list.append(annotation["id"])
        
        return category_list
    
    @classmethod
    def article_entity_relation(cls, obj, category_list):         
        obj.entities = list(set(category_list))        

        # Set articles to redis
        dm.update_article(obj)
        dm.update_entity_by_article(obj)
        