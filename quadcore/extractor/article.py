from quadcore.extractor import Extractor

class ArticleExtractor(Extractor):
    @classmethod
    def preprocess(cls, obj, options):
        """
        Preprocess obj to significant {key:value}
        Returns list of urls to fetch.
        """
        entity_dict = {}
        key_num = 1
        for article_num in obj:
            for key in article_num:
                entity_dict[key_num] = article_num.get("content")   
                key_num += 1

        return entity_dict
    
    
       