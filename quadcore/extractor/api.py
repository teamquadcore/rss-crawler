from quadcore.config import Config
import requests
import json

class ApiManage: 
    """
    Manager for Dandelion API.
    """

    # Get category from dictionary 
    @classmethod
    def get_entities(cls, processed_dict, confidence=0.1, lang='en'):
        new_dict = dict()
        for key in processed_dict:
            text = processed_dict.get(key)

            payload = {
                'token': Config.dandelion_token,
                'url': text,
                'confidence': confidence,
                'lang': lang,
            }

            response = requests.get(Config.dandelion_url, params=payload)
            category_list = cls.get_category_list(response.json())
            new_dict[text] = category_list
        
        return new_dict
    
    # Get category list
    def get_category_list(data):
        category_list = list()

        for annotation in data['annotations']:
            category_list.append(annotation["id"])
        
        return category_list 
    

