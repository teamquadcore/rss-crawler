import requests
from bs4 import BeautifulSoup

class Extractor:
    """
    Superclass for all extractor.
    """

    @classmethod
    def __new__(cls, self, obj):
        processed_dict = cls.preprocess(obj)
        category_objects = ApiManage.get_entities(processed_dict)
        print(category_objects)



