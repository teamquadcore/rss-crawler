from datetime import datetime
import json

class Newspaper:
    THE_VERGE = "The Verge"
    ENGADGET = "Engadget"
    LIFEHACKER = "LifeHacker"
    WIRED = "Wired"

class Article:
    """
    Article model.
    """
    STATE_NOT_INDEXED = 0
    STATE_INDEXED = 1
    STATE_COMPLETED = 2

    def __init__(self, **kwargs):
        if "article_key" not in kwargs == None:
            self.state = Article.STATE_NOT_INDEXED
        else: 
            self.article_key = kwargs["article_key"]
            if len(kwargs["entities"]) != 0:
                self.state = Article.STATE_INDEXED
            else:
                self.state = Article.STATE_COMPLETED
        
        # String or Numbers
        self.title = kwargs["title"]
        self.newspaper = kwargs["newspaper"]
        self.link = kwargs["link"]
        self.published = kwargs["published"]
        self.content = kwargs["content"]
        self.author = kwargs["author"]

        # Lists
        self.category = kwargs["category"]
        self.entities = kwargs["entities"]
       
    @classmethod
    def build(cls, resp):
        return Article(
            article_key=resp["article_key"],
            title=resp["title"],
            newspaper=resp["newspaper"],
            link=resp["link"],
            published=resp["published"],
            content=resp["content"],
            author=resp["author"],
            category=resp["category"],
            entities=resp["entities"]
        )

    def extract(self):
        """
        Extracts the structure to dict.
        """
        return {
            "article_key": self.article_key,
            "title": self.title,
            "newspaper": self.newspaper,
            "link": self.link,
            "published": self.published,
            "content": self.content,
            "author": self.author,
            # Due to redis hash structure, 
            # only string will be accepted
            "category": json.dumps(self.category),
            "entities": json.dumps(self.entities)
        }

class Entity:
    """
    Entity model.
    """
    STATE_NOT_INDEXED = 0
    STATE_INDEXED = 1

    def __init__(self, entity_id, title, entity_key=None, articles=list()):
        if len(articles) == 0:
            self.state = Entity.STATE_NOT_INDEXED
        else:
            self.state = Entity.STATE_INDEXED

        # String and Numbers
        self.entity_id = entity_id
        self.entity_key = entity_key
        self.title = title

        # Lists
        self.articles = articles

    @classmethod
    def build(cls, resp):
        return Entity(resp["id"], resp["title"], articles=json.loads(resp["articles"]))

    def extract(self):
        """
        Extracts the structure to dict.
        """
        return {
            "id": self.entity_id,
            "title": self.title,
            # Due to redis hash structure, 
            # only string will be accepted
            "articles": json.dumps(self.articles)
        }
