from lib.socket import Socket
from lib.controller import Controller
from socket import *

class Room(Controller):

    def __init__(self, socket, endpoint, args):
        super().__init__(socket)

        endpoints = {
            '/add': self.add,
            '/remove': self.remove,
            '/reserve': self.reserve,
            '/checkavailability': self.check_availability
        }

        endpoints[endpoint](**args)

        self.exit()

        def add(name: str):
            pass

        def remove(name: str):
            pass

        def reserve(name: str, day: int, hour: int, duration: int):
            pass

        def check_availability(name: str, day: int):
            pass


Socket(lambda socket, endpoint, args: Room(socket, endpoint, args), '0.0.0.0', 8002).start_listening()