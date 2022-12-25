import redis
from lib.singleton import Singleton

class Database(metaclass=Singleton):
    _database = None
    def __init__(self):
        self._database = redis.Redis(host='localhost', port=6379, db=0)
        print("Connected to Redis")
    
    def set(self, key, value) -> bool:
        return self._database.setnx(key, value)
    
    def delete(self, key) -> bool:
        return self._database.delete(key) > 0

    def get(self, key):
        self._database.get(key)


