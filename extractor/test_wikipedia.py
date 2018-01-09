import requests
import json
import ast
from bs4 import BeautifulSoup, Tag, NavigableString   # XML(HTML)을 파싱

def main():
    wikipedia_num = 1
    extract_entity = dict()    
    
    for i in range(1, 50):    
        wikipedia_str = str(wikipedia_num)
        obj = fetch(wikipedia_str)
        extract(obj, extract_entity)
        wikipedia_num += 1000   

    print(extract_entity)    


def fetch(username):
    """
    Get a page from Wikipedia
    """    
    raw_code = requests.get("""https://tools.wmflabs.org/enwp10/cgi-bin/list2.fcgi?run=yes&projecta=Computing&limit=1000&offset=%s&sorta=Article+title&sortb=Quality""" %username).text
    return BeautifulSoup(raw_code, "html.parser")


def extract(obj, extract_entity):
    """
    Extract WikipediaID and WikipediaTitle
    Make Wikipedia dictionary
    """
    
    items = obj.findAll("tr", {"class": "list-odd"}) \
            + obj.findAll("tr", {"class": "list-even"})
    
    for entry in items:
        flag = 0  
        wiki_id = ""
        wiki_title = ""      
        childrens = entry.children
        for i in childrens:
            if type(i) == Tag and flag == 0:
                for link in i.findAll('a'):
                    wiki_title = link.string
                    # We need first attribute 'a'
                    flag = 1
                    break

                for j in i.attrs:
                    if i.attrs[j][0] == "resultnum":
                        wiki_id = i.string

                extract_entity[wiki_id] = wiki_title


if __name__ == "__main__":
    main()
    