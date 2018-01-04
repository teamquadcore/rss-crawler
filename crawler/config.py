# Yielding User-Agent validation
# TODO Add Referrer header if needed
req_header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
}

class RSSConfig:
    # RSS feed links
    links = {
        "The Verge": "https://www.theverge.com/rss/index.xml",
        "Engadget": "https://www.engadget.com/rss.xml",
        "Life Hacker": "https://lifehacker.com/rss",
        "Wired": "https://www.wired.com/feed/rss",
        # Feedburner based XML Feed, need to be careful
        "TechCrunch": "http://feeds.feedburner.com/TechCrunch/"
    }

    item_name = {
        "The Verge": "entry",
        "Engadget" : "item",
        "LifeHacker" : "item",
        "Wired" : "item"
    }

    item_publish = {
        "The Verge": "published",
        "Engadget" : "pubDate",
        "LifeHacker" : "pubDate",
        "Wired" : "pubDate"
    }

    item_content = {
        "The Verge": "content",
        "Engadget" : "description",
        "LifeHacker" : "description",
        "Wired" : "description"
    }

    item_author = {
        "The Verge": "author",
        "Engadget" : "creator",
        "LifeHacker" : "creator",
        "Wired" : "creator"
    }