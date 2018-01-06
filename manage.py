from manager import Manager
from quadcore.crawler.rss import RSSCrawler
from quadcore.crawler.github import GithubCrawler

import quadcore.tests
import json
import sys
import unittest

manager = Manager()

@manager.command
def test(category):
    """
    Run the manual test codes for developers.
    """
    if category == "rss":
        # TODO prevent from unappropriate input
        newspaper = input("[+] Newspaper name: ")
        rss_result = RSSCrawler(newspaper)
        print(json.dumps(rss_result, indent=4))
    elif category == "github":
        # TODO prevent from fake username
        username = input("[+] GitHub Username: ")
        github_result = GithubCrawler(username)
        print(json.dumps(github_result, indent=4))
    elif category == "linkedin":
        print("[-] Not supported yet!")

if __name__ == '__main__':
    manager.main()