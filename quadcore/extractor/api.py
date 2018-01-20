from quadcore.config import Config
import requests
import json

class ApiManage: 
    """
    Manager for Dandelion API.
    """
    # Get category from dictionary 
    @classmethod
    def get_entities(cls, processed_list, confidence=0.1, lang='en'):
        new_dict = dict()
        for url in processed_list:

            payload = {
                'token': Config.dandelion_token,
                'url': url,
                'confidence': confidence,
                'lang': lang,
            }

            response = requests.get(Config.dandelion_url, params=payload)
            category_list = cls.get_category_list(response.json())
            new_dict[url] = category_list
        
        return new_dict
    
    # Get category list
    def get_category_list(data):
        category_list = list()

        for annotation in data['annotations']:
            category_list.append(annotation["id"])
        
        return category_list 
