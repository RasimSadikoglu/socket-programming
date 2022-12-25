from business.activity_business import ActivityBusiness
from lib.server_socket import Socket
from lib.controller import Controller
from socket import *

class Activity(Controller):

    def __init__(self, socket, endpoint, args):
        super().__init__(socket)

        self.business = ActivityBusiness()

        endpoints = {
            '/add': self.add,
            '/remove': self.remove,
            '/check': self.check
        }

        endpoints[endpoint](**args)

        self.exit()

    def add(self, name = ""):
        self.send_html(self.business.add(name))

    def remove(self, name = ""):
        self.send_html(self.business.remove(name))

    def check(self, name = ""):
        self.send_html(self.business.check(name))

Socket('0.0.0.0', 8082, lambda socket, endpoint, args: Activity(socket, endpoint, args)).start_listening()