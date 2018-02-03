from bs4 import BeautifulSoup
from manager import Manager
from quadcore.crawler.rss import RSSCrawler
from quadcore.crawler.wiki import WikipediaCrawler
from quadcore.config import Config
from quadcore.extractor import Extractor
from quadcore.manager.data import DataManager as dm
from quadcore.manager.db import DBManager
from quadcore.models import Article 
from quadcore.models import Entity
from quadcore.tests.manual import ManualTest

import ast
import json
import os
import quadcore.tests
import requests
import time
import unittest

manager = Manager()

manual_test_pair = {
    "rss": ManualTest.rss,
    "data": ManualTest.data
}

def slack_alert(msg):
    link = "https://hooks.slack.com/services/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"
    data = "{\"text\": \"%MSG%\"}".replace("%MSG%", msg)
    os.system("curl -X POST -H 'Content-type: application/json' --data '{data}' {link}".format(data=data, link=link))

@manager.command
def run_manual(category):
    """
    Run the manual test codes for developers.
    """
    if category in manual_test_pair:
        manual_test_pair[category]()
    else:
        print("[-] No methods available.")

@manager.command
def map_articles():
    """
    Create article map.
    """
    db = DBManager.get_redis()

    article_count = dm.get_article_count()
    for key in range(1, article_count + 1):
        if key % 50 == 0: print("[+] " + str(key) + "th data is processing...")
        article = dm.get_article_by_key(key)
        db.hset("article_map", article_link, "1")

@manager.command
def map_entities():
    """
    Create entity map.
    """
    db = DBManager.get_redis()

    entity_count = dm.get_entity_count()
    for key in range(1, entity_count + 1):
        if key % 50 == 0: print("[+] " + str(key) + "th data is processing...")
        entity = dm.get_entity_by_key(key)
        db.hset("entity_map", entity.entity_id, key)

@manager.command
def crawl_article():
    """
    Run the article crawler for all newspapers.
    """
    db = DBManager.get_redis()
    slack_alert("*News Crawling* started!\n")

    # TODO(@harrydrippin): Crawl for all newspapers after enough tokens, keying newspapers by some ID
    for newspaper in Config.rss_links:
        articles = RSSCrawler(newspaper)
        
        for article in articles:
            article = Article.build(article)

            if not dm.is_article_duplicate(article):
                dm.set_article(article)
                db.hset("article_map", article.link, "1")

    slack_alert("*News Crawling* finished!\n")

@manager.command
def crawl_entity(crawling_category):
    """
    Run the entity crawler for wikipedia.
    """
    slack_alert("*Wikipedia Crawling* started!\n> Requested: *" + str(crawling_category) + "*")

    start = time.time()
    wiki_crawl_result = WikipediaCrawler(options={
        "mode": "html",
        "category": crawling_category
    })
    spent = time.time() - start

    slack_alert("Crawling was done.\n> spent {time} min.".format(time=(spent / 60)))
    slack_alert("Inserting entities to DB...")
    
    start = time.time()
    count = 1
    
    for key in wiki_crawl_result.keys():
        if count % 50 == 0:
            print("[+] " + str(count) + "th data is processing...")
        item_value = wiki_crawl_result[key]
        dm.set_entity(Entity(int(key), item_value))
        count += 1 
    spend = time.time() - start

    slack_alert("Inserting was done.\n> spend {time} min.".format(time=(spend / 60)))
    

@manager.command
def extract_article():
    """
    Extract entity from article and two-way relationship between articles and entities.
    """
    db = DBManager.get_redis()

    article_count = dm.get_article_count()    
    token_list = Config.dandelion_token.split("#")
    key = 1
    whos = 0
    
    for token in token_list:
        remain_token = int(dm.remain_token(token))
        for i in range(1, int(remain_token/2)+1):
            print(Config.dandelion_who[whos] + ": " + str(key) + "th data is processing...")
            article = dm.get_article_by_key(key)               
            if article != None:
                article_entity = Extractor(article, token)
            if article_count == key:
                return
            key += 1 
        whos += 1 

@manager.command
def reconnect_article():
    """
    Delete article_map and create new article_map.
    """
    db = DBManager.get_redis()
    article_count = dm.get_article_count()
    
    db.delete("article_map")

    for key in range(1, article_count+1):
        article_link = dm.get_article_by_key(str(key)).link
        db.hset("article_map", article_link, "1")

@manager.command
def reconnect_entity():
    """
    Delete entity_map and create new entity_map.
    """
    db = DBManager.get_redis()
    entity_count = dm.get_entity_count()
    
    db.delete("entity_map")

    for key in range(1, entity_count+1):
        entity = dm.get_entity_by_key(key)
        db.hset("entity_map", entity.entity_id, key)

@manager.command
def disconnect_article():
    """
    Remove entities in article.
    """
    db = DBManager.get_redis()
    article_count = dm.get_article_count()

    print("[+] Article->Entity remove a connetion")
    for i in range(1, article_count + 1): 
        if i % 10 == 0: print(str(i) + "/" + str(article_count) + " 번째 데이터 처리 중")
        article_key = "article:" + str(i)
        hashmap = db.hset(article_key, "entities", "[]")

@manager.command
def disconnect_entity():
    """
    Remove articles in entity.
    """
    db = DBManager.get_redis()
    entity_count = dm.get_entity_count()

    print("[+] Entity->Article remove a connetion")
    for i in range(1, entity_count + 1): 
        if i % 50 == 0: print(str(i) + "/" + str(entity_count) + " 번째 데이터 처리 중")
        entity_key = "entity:" + str(i)
        hashmap = db.hset(entity_key, "articles", "[]")

if __name__ == '__main__':
    manager.main()