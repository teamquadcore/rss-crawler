from quadcore.extractor import Extractor

class ArticleExtractor(Extractor):
    @classmethod
    def preprocess(cls, obj, options):
        """
        Preprocess obj to significant {key:value}
        Returns list of urls to fetch.
        """
        entity_list = list()
        for article_num in obj:
            for key in article_num:
                entity_list.append(article_num.get("link"))   

        return entity_list 
       