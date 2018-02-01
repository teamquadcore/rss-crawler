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
    def __new__(cls, self, obj):
        category_list = cls.get_entities(obj)
        cls.article_entity_relation(obj, category_list)
        #print(category_objects)
        #return category_objects

    @classmethod
    def get_entities(cls, obj, confidence=0.1, lang='en'):
        category_list = [185868, 247315, 36544534, 50741788, 1062429, 6639133, 51746, 10294, 300602, 93755, 195149, 2044496, 9988187, 290909, 675426, 105070, 29816, 186493, 153217, 9801859, 1619599, 63121, 486547, 251540, 45207, 683672, 23475353, 25755, 277663, 148131, 55974, 167079, 52231341, 118450, 5309, 87231, 90815, 36689092, 161999, 3736784, 42257619, 41684, 4624596, 4822, 33094374, 7398, 50408, 46313, 147184, 5167862, 10501, 30871819, 7279897, 5405, 33057, 39206, 72487, 39208, 46380, 254769, 17555269, 32070, 634183, 598345, 240468, 360788, 5043544, 26561880, 3372377, 42852, 130918, 48999, 69480, 41837, 59252, 28030850, 65411, 18619278, 33172, 100245, 1398166, 10134, 47005, 3369375, 40228775, 19881, 43950, 202672, 25009, 187317, 433590, 735672, 174521, 224700, 39399882, 22217168, 46545, 46426065, 18998750, 4122592, 4595, 8182, 44026]
        '''
        payload = {
            'token': Config.dandelion_token,
            'url': obj.link,
            'confidence': confidence,
            'lang': lang,
        }
        response = requests.get(Config.dandelion_url, params=payload)
        category_list = cls.get_category_list(response.json())
        '''
        
        return category_list

    # Get category list
    @classmethod
    def get_category_list(cls, data):
        category_list = list()

        for annotation in data['annotations']:
            category_list.append(annotation["id"])
        
        return category_list
    
    @classmethod
    def article_entity_relation(cls, obj, category_list):         
        obj.entities = list(set(category_list))        

        # Set articles to redis
        dm.update_article(obj)
        dm.update_entity_by_article(obj)


        


