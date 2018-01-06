from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

class Config:
    # Configuration for redis
    redis = {
        "host": os.environ.get("REDIS_HOST"),
        "id": os.environ.get("REDIS_ID"),
        "password": os.environ.get("REDIS_PASSWORD"),
        "port": os.environ.get("REDIS_PORT"),
        "db": os.environ.get("REDIS_DB_NUMBER")
    }

    # RSS feed links
    rss_links = {
        "The Verge": "https://www.theverge.com/rss/index.xml",
        "Engadget": "https://www.engadget.com/rss.xml",
        "LifeHacker": "https://lifehacker.com/rss",
        "Wired": "https://www.wired.com/feed/rss"
    }

    # Positional ordered: name, publish, content, author
    rss_factors = {
        "The Verge": ("entry", "published", "content", "author"),
        "Engadget": ("item", "pubDate", "description", "creator"),
        "LifeHacker": ("item", "pubDate", "description", "creator"),
        "Wired": ("item", "pubDate", "description", "creator")
    }

    # Header information for yielding User-Agent validation
    # TODO Add Referrer header if needed
    req_header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
    }