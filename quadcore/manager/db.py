from quadcore.config import Config
import redis

class DBManager:
    __redis_store = None

    @classmethod
    def __init_redis(cls):
        cls.__redis_store = redis.StrictRedis(host=Config.redis["host"], port=Config.redis["port"], password=Config.redis["password"], db=0, charset="utf-8", decode_responses=True)
    
    @classmethod
    def get_redis(cls):
        if cls.__redis_store == None: cls.__init_redis()
        return cls.__redis_store
        