from business.reservation_business import ReservationBusiness
from lib.html_result import HTMLResult
from lib.server_socket import Socket
from lib.controller import Controller
from socket import *

class Reservation(Controller):

    def __init__(self, socket, endpoint, args):
        endpoints = {
            '/reserve': self.reserve,
            '/listavailability': self.list_availability,
            '/display': self.display
        }

        super().__init__(socket, endpoints, endpoint, args, ReservationBusiness)

    def reserve(self, room = "", activity = "", day = 0, hour = 0, duration = 0):
        self.send_html(self.business.reserve(room, activity, int(day), int(hour), int(duration)))

    def list_availability(self, room = "", day = 0):
        self.send_html(self.business.list_availability(room, int(day)))

    def display(self, id = 0):
        self.send_html(self.business.display(int(id)))

Socket('0.0.0.0', 8080, Reservation).start_listening()