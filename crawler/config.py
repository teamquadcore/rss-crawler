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
        "LifeHacker": "https://lifehacker.com/rss",
        "Wired": "https://www.wired.com/feed/rss",
        # TODO(@ethkim): Fix the XML feed consumption to prevent breaking from browser-friendly style codes
        # "TechCrunch": "http://feeds.feedburner.com/TechCrunch/"
    }

    # Positional ordered: name, publish, content, author
    properties = {
        "The Verge": ("entry", "published", "content", "author"),
        "Engadget": ("item", "pubDate", "description", "creator"),
        "LifeHacker": ("item", "pubDate", "description", "creator"),
        "Wired": ("item", "pubDate", "description", "creator")
    }