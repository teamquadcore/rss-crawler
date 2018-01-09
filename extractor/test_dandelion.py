# SAMPLE CODE FOR DANDELION API
# API token from @achaccha

import requests
import json
 
# TODO(@achaccha): Move this to .env 
TOKEN = '0af76af32cb343a19f7c7ea0e153922e'
 
ENTITY_URL = 'https://api.dandelion.eu/datatxt/nex/v1'
 
def get_entities(text, confidence=0.1, lang='en'):
    payload = {
        'token': TOKEN,
        'text': text,
        'confidence': confidence,
        'lang': lang,
    }
    response = requests.get(ENTITY_URL, params=payload)
    return response.json()
 
def print_entities(data):
    extract_data = dict()
    for annotation in data['annotations']:
        extract_data[annotation["label"]] = annotation["id"]
    
    print(extract_data)    
 
if __name__ == '__main__':
    query = "Trump has a son called Donald Trump and Donald Trump has a father named Trump."
    response = get_entities(query)
    print_entities(response)
   #print(json.dumps(response, indent=4))
    

