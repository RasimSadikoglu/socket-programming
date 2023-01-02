from lib.html_result import HTMLResult
from lib.server_socket import Socket
from lib.controller import Controller
from socket import *
from business.room_business import RoomBusiness
class Room(Controller):

    def __init__(self, socket, endpoint, args):
        endpoints = {
            '/add': self.add,
            '/remove': self.remove,
            '/reserve': self.reserve,
            '/checkavailability': self.check_availability
        }

        super().__init__(socket, endpoints, endpoint, args, RoomBusiness)

    def add(self, name = ""):
        self.send_html(self.business.add(name))

    def remove(self, name = ""):
        self.send_html(self.business.remove(name))

    def reserve(self, name = "", day = 0, hour = 0, duration = 0):
        self.send_html(self.business.reserve(name, int(day), int(hour), int(duration)))

    def check_availability(self, name = "", day = 0):
        self.send_html(self.business.check_availability(name, int(day)))

Socket('0.0.0.0', 8081, Room).start_listening()