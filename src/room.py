from lib.socket import Socket
from lib.controller import Controller
from socket import *
from activity_client import ActivityClient

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

    def add(self, name: str):
        pass

    def remove(self, name: str):
        pass

    def reserve(self, name: str, day: int, hour: int, duration: int):
        pass

    def check_availability(self, name: str, day: int):
        pass


Socket('0.0.0.0', 8002, lambda socket, endpoint, args: Room(socket, endpoint, args)).start_listening()