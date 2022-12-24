from lib.socket import Socket
from socket import *

def reserve(room: str, activity: str, day: int, hour: int, duration: int):
    pass

def list_availability(room: str, day: int = 0):
    pass

def display(id: int):
    pass

endpoints = {
    '/reserve': reserve,
    '/listavailability': list_availability,
    '/display': display
}

Socket(endpoints, '0.0.0.0', 8000).start_listening()