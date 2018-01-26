import requests
from bs4 import BeautifulSoup
from quadcore.extractor.api import ApiManage

class Extractor:
    """
    Superclass for all extractor.
    """

    @classmethod
    def __new__(cls, self, obj, options=dict()):
        processed_dict = cls.preprocess(obj, options)
        category_objects = ApiManage.get_entities(processed_dict)
        return category_objects



