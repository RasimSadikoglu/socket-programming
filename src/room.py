from lib.server_socket import Socket
from lib.controller import Controller
from socket import *
from business.room_business import RoomBusiness
class Room(Controller):

    def __init__(self, socket, endpoint, args):
        super().__init__(socket)

        self.business = RoomBusiness()

        endpoints = {
            '/add': self.add,
            '/remove': self.remove,
            '/reserve': self.reserve,
            '/checkavailability': self.check_availability
        }

        endpoints[endpoint](**args)

        self.exit()

    def add(self, name: str):
        result = self.business.add(name)
        self.send_json(*result)


    def remove(self, name: str):
        result = self.business.remove(name)
        self.send_json(*result)

    def reserve(self, name: str, day: int, hour: int, duration: int):
        result = self.business.reserve(name, day, hour, duration)

    def check_availability(self, name: str, day: int):
        result = self.business.check_availability(name, day)


Socket('0.0.0.0', 8002, lambda socket, endpoint, args: Room(socket, endpoint, args)).start_listening()