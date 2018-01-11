import requests
import json
from bs4 import BeautifulSoup, Tag, NavigableString   
from quadcore.crawler import Crawler

class WikipediaCrawler(Crawler):
    """
    Fetch Wikipedia and restruct format dictionary.
    """
    @classmethod
    def __new__(cls, self, code="", options={"mode": "html"}):
        processed_codes = cls.preprocess(code, options)
        soups = cls.fetch(processed_codes, options)
        return cls.extract(soups, code, options)
    
    @classmethod
    def preprocess(cls, source, options):
        """
        Preprocess source to proper URL string.
        """
        wikipedia_num = 1
        wiki_url = list()
        for i in range(1, 2):    
            wikipedia_str = str(wikipedia_num)
            wiki_url.append("https://tools.wmflabs.org/enwp10/cgi-bin/list2.fcgi?run=yes&projecta=Computing&limit=1000&offset=%s&sorta=Article+title&sortb=Quality" %wikipedia_str)
            wikipedia_num += 2

        return wiki_url   
    
    @classmethod
    def extract(cls, objs, code, options):
        """
        Extract WikipediaID and WikipediaTitle
        Make Wikipedia dictionary
        @TODO Refine title and apply classify algorithm
        """
        extract_entity = dict()
        for obj in objs:
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

        return extract_entity

    