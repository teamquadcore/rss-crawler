import requests
import json
from bs4 import BeautifulSoup, Tag, NavigableString   
from quadcore.crawler import Crawler
from quadcore.config import Config

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
    def get_range(cls, source):
        section_xml = requests.get(Config.wiki_url %(source, 1)).text
        obj = BeautifulSoup(section_xml)

        items = obj.findAll('div', {"class": "navbox"})

        for entry in items:
            for item in entry.children:
                if type(item) == Tag and item.name == "b":
                    if "Total" in item.text:           
                        wiki_range = int(int(item.text[15:]) / 1000 + 1)
        
        return wiki_range
    
    @classmethod
    def preprocess(cls, source, options):
        """
        Preprocess source to proper URL string.
        """
        wiki_url = list()
        wiki_range = cls.get_range(options["category"])
        category = options["category"]

        for i in range(1, wiki_range+1):
            offset = 1 + (1000 * (i - 1))         
            wiki_url.append(Config.wiki_url %(category, offset))       
        
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
                            wiki_id = cls.parse_article_id(link["href"]).strip()
                            # We need first attribute 'a'
                            flag = 1
                            break
                        if wiki_id != str():
                            extract_entity[wiki_id] = wiki_title
        
        return extract_entity

    @classmethod
    def parse_article_id(cls, link):
        """
        Parse article id form Wikipedia.
        """
        resp = requests.get(link).text
        comment_part = resp[resp.index("\"wgArticleId\":") + 14:]
        return comment_part[0:comment_part.index(",")]
