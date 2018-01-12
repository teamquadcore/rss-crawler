from manager import Manager

from quadcore.config import Config
from quadcore.tests.manual import ManualTest
from quadcore.crawler.rss import RSSCrawler
from quadcore.crawler.wiki import WikipediaCrawler
from quadcore.extractor.article import ArticleExtractor
from quadcore.manager.data import DataManager as dm
from quadcore.manager.db import DBManager
from quadcore.models import Article, Entity

import quadcore.tests
import time
import unittest
import os
import json

manager = Manager()

manual_test_pair = {
    "rss": ManualTest.rss,
    "github": ManualTest.github,
    "data": ManualTest.data
}

def slack_alert(msg):
    test_link = "https://hooks.slack.com/services/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"
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
def map_entities():
    """
    Run the article crawler for all newspapers.
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

    # TODO(@harrydrippin): Crawl for all newspapers after enough tokens
    newspaper = "The Verge"
    articles = RSSCrawler(newspaper)
    entity_data = ArticleExtractor(articles)

    for article, link in zip(articles, entity_data.keys()):
        article = Article.build(article)

        if not dm.is_article_duplicate(article):
            article.entities = list(set(entity_data[link]))

            # Set articles to redis
            dm.set_article(article)
            dm.update_entity_by_article(article)

            # Duplication mark
            db.hset("article_map", article.link, "1")

@manager.command
def crawl_entity(crawling_range):
    """
    Run the entity crawler for wikipedia.
    """
    slack_alert("*Wikipedia Crawling* started!\n> Requested: *" + str(crawling_range) + "*")

    start = time.time()
    wiki_crawl_result = WikipediaCrawler(options={
        "mode": "html",
        "range": crawling_range
    })
    end = time.time()
    spent = end - start

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
    end = time.time()
    spend = end - start
    
    slack_alert("All jobs are done! Spent " + str(spent) + " min.\n> Requested: *" + str(crawling_range) + "*")

if __name__ == '__main__':
    manager.main()