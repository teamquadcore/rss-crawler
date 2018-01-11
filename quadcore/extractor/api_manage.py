from quadcore.extractor import Extractor
import requests
import json

class ApiManage: 
    # TODO(@achaccha): Move this to .env 
    TOKEN = '0af76af32cb343a19f7c7ea0e153922e'    
    ENTITY_URL = 'https://api.dandelion.eu/datatxt/nex/v1'    
    
    # Get category from dicitionary   
    def get_entities(processed_dict, confidence=0.1, lang='en'):
        new_dict = dict()
        for key in processed_dict:
            text = processed_dict.get(key)

            payload = {
                'token': TOKEN,
                'text': text,
                'confidence': confidence,
                'lang': lang,
            }

            response = requests.get(ENTITY_URL, params=payload)
            category_list = get_category_list(response.json())
            new_dict[text] = category_list
        
        return new_dict
    
    # Get category list
    def get_category_list(data):
        category_list = list()

        for annotation in data['annotations']:
            category_list.append(annotation["id"])
        
        return category_list 
    

