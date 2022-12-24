from lib.socket import Socket
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

    def reserve(room: str, activity: str, day: int, hour: int, duration: int):
        pass

    def list_availability(room: str, day: int = 0):
        pass

    def display(id: int):
        pass


Socket(lambda socket, endpoint, args: Reservation(socket, endpoint, args), '0.0.0.0', 8000).start_listening()