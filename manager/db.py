import redis
from dotenv import load_dotenv, find_dotenv

class DBManager:
    __redis_store = None

    @staticmethod
    def __init_redis():
        Cache.__redis_store = redis.StrictRedis(host=Config.APP_CONFIG["REDIS_HOST"], port=Config.APP_CONFIG["REDIS_PORT"], password=Config.APP_CONFIG["REDIS_PASSWORD"], db=0, charset="utf-8", decode_responses=True)
    
    @staticmethod
    def get_redis():
        if Cache.__redis_store == None: Cache.__init_redis()
        return Cache.__redis_store