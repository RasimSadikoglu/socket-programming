from clients.room_client import RoomClient
from lib.server_socket import Socket
from lib.controller import Controller
from socket import *

class Reservation(Controller):

    def __init__(self, socket, endpoint, args):
        super().__init__(socket)

        endpoints = {
            '/reserve': self.reserve,
            '/listavailability': self.list_availability,
            '/display': self.display
        }

        endpoints[endpoint](**args)

        self.exit()

    def reserve(self, room: str, activity: str, day: int, hour: int, duration: int):
        pass

    def list_availability(self, room: str, day: int = 0):
        pass

    def display(self, id: int):
        pass

Socket('0.0.0.0', 8080, lambda socket, endpoint, args: Reservation(socket, endpoint, args)).start_listening()