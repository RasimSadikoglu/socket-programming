from lib.server_socket import Socket
from lib.controller import Controller
from socket import *

class Activity(Controller):

    def __init__(self, socket, endpoint, args):
        super().__init__(socket)

        endpoints = {
            '/add': self.add,
            '/remove': self.remove,
            '/check': self.check
        }

        endpoints[endpoint](**args)

        self.exit()

    def add(self, name: str):
        self.initialize_response(200) \
            .add_header('Content-Type', 'text/html') \
            .add_body(f'Hello, {name}!\n') \
            .encode() \
            .send()

    def remove(self, name: str):
        pass

    def check(self, name: str):
        pass


Socket('0.0.0.0', 8001, lambda socket, endpoint, args: Activity(socket, endpoint, args)).start_listening()