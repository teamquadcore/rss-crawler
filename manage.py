from manager import Manager
from quadcore.tests.manual import ManualTest
from quadcore.crawler.wiki import WikipediaCrawler
from quadcore.manager.data import DataManager as dm
from quadcore.models import Article, Entity
import quadcore.tests
import time
import unittest
import os

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
def crawl_wiki(crawling_range):
    """
    Run the entity crawler for wikipedia.
    """
    slack_alert("*Wikipedia Crawling* 을 시작합니다!\n> 요청된 값은 *" + str(crawling_range) + "* 입니다.")
    print("[+] Crawling wikipedia...")
    start = time.time()
    wiki_crawl_result = WikipediaCrawler(options={
        "mode": "html",
        "range": crawling_range
    })
    end = time.time()
    spent = end - start
    slack_alert("Crawling이 완료되었습니다!\n> 총 {time}분 소요됨".format(time=(spent / 60)))
    slack_alert("DB에 정보를 넣는 중입니다...")
    print("[+] Adding results to database...")
    count = 1
    for key in wiki_crawl_result.keys():
        if count % 50 == 0:
            print("[+] " + str(count) + "th data is processing...")
        item_value = wiki_crawl_result[key]
        dm.set_entity(Entity(int(key), item_value))
        count += 1
    slack_alert("모든 작업이 완료되었습니다!\n> 요청된 값은 " + str(crawling_range) + "입니다.")

if __name__ == '__main__':
    manager.main()