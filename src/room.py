from lib.socket import Socket
from socket import *

def add(name: str):
    pass

def remove(name: str):
    pass

def reserve(name: str, day: int, hour: int, duration: int):
    pass

def check_availability(name: str, day: int):
    pass

endpoints = {
    '/add': add,
    '/remove': remove,
    '/reserve': reserve,
    '/checkavailability': check_availability
}

Socket(endpoints, '0.0.0.0', 8002).start_listening()