from Socket.lib import Socket
import time, random
from socket import *

def add(name: str, socket: socket, semaphore, response: bytes):
    time.sleep(random.random())
    socket.sendall(response)
    socket.close()
    semaphore()

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

Socket(endpoints, '0.0.0.0', 8000).start_listening()