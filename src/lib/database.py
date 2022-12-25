import redis
from lib.singleton import Singleton

class Database(metaclass=Singleton):
    __database = None
    def __init__(self):
        self.__database = redis.Redis(host='localhost', port=6379, db=0)
        print("Connected to Redis")
    
    def set(self, key, value) -> bool:
        return self.__database.set(key, value)

    def delete(self, key) -> bool:
        return self.__database.delete(key) > 0

    def get(self, key):
        return self.__database.get(key)

    def get_new_id(self):
        return int(self.__database.incr('__reservation_id'))