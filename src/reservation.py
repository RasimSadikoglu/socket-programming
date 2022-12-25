from business.reservation_business import ReservationBusiness
from clients.room_client import RoomClient
from lib.server_socket import Socket
from lib.controller import Controller
from socket import *

class Reservation(Controller):

    def __init__(self, socket, endpoint, args):
        super().__init__(socket)

        self.business = ReservationBusiness()

        endpoints = {
            '/reserve': self.reserve,
            '/listavailability': self.list_availability,
            '/display': self.display
        }

        endpoints[endpoint](**args)

        self.exit()

    def reserve(self, room = "", activity = "", day = 0, hour = 0, duration = 0):
        self.send_html(self.business.reserve(room, activity, int(day), int(hour), int(duration)))

    def list_availability(self, room = "", day = 0):
        self.send_html(self.business.list_availability(room, int(day)))

    def display(self, id = 0):
        self.send_html(self.business.display(int(id)))

Socket('0.0.0.0', 8080, lambda socket, endpoint, args: Reservation(socket, endpoint, args)).start_listening()