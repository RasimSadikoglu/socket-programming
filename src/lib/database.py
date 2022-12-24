import redis
from singleton import Singleton

class Database(metaclass=Singleton):
    _database = None
    def __init__(self):
        self._database = redis.Redis(host='localhost', port=6379, db=0)
        print("Connected to Redis")
    
    def set(self, key, value):
        self._database.set(key, value)
        return self
    
    def delete(self, key):
        self._database.delete(key)
        return self

    def get(self, key):
        self._database.get(key)
        return self


