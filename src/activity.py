from lib.socket import Socket
from socket import *

def add(name: str):
    pass

def remove(name: str):
    pass

def check(name: str):
    pass

endpoints = {
    '/add': add,
    '/remove': remove,
    '/check': check
}

Socket(endpoints, '0.0.0.0', 8001).start_listening()