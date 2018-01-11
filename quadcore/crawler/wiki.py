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
        wiki_url = list()
        offset = 1 + (1000 * (int(options["range"]) - 1))
        wiki_url.append("https://tools.wmflabs.org/enwp10/cgi-bin/list2.fcgi?run=yes&projecta=Computing&limit=1000&offset=%d&sorta=Article+title&sortb=Quality" % offset)
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
        comment_part = resp[resp.index("enwiki:pcache:idhash:") + 21:]
        return comment_part[0:comment_part.index("-")]
    