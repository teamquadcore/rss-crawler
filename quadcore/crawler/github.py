import requests
from bs4 import BeautifulSoup
from quadcore.crawler import Crawler

class GithubCrawler(Crawler):
    """
    Fetch Github profile and restruct to proper format dictionary.
    """
    @classmethod
    def __new__(cls, self, code, options={"mode": "json"}):
        processed_codes = cls.preprocess(code, options)
        soups = cls.fetch(processed_codes, options)
        return cls.extract(soups, code, options)

    @classmethod
    def preprocess(cls, source, options):
        """
        Preprocess source to proper URL string.
        """
        # Github profile url format
        return [
            # Index 0: User metadata
            "https://api.github.com/users/" + source,
            # Index 1: User repository list
            "https://api.github.com/users/" + source + "/repos"
        ]
    
    @classmethod
    def extract(cls, objs, code, options):
        """
        Extract news from BeautifulSoup object.
        """
        metadata, repolist = objs[0], objs[1]
        ret = dict()

        # Profile extraction
        user = dict()
        user["name"] = metadata["name"]
        user["nickname"] = metadata["login"]
        user["company"] = metadata["company"]
        user["location"] = metadata["location"]
        user["avatar_url"] = metadata["avatar_url"]
        ret["user"] = user

        # Repository extraction
        repos = list()
        for r in repolist:
            repo = dict()
            repo["name"] = r["name"]
            repo["owner"] = r["owner"]["login"]
            repo["url"] = r["html_url"]
            repo["language"] = r["language"]
            repos.append(repo)
        ret["repos"] = repos
        
        return ret