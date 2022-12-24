import socket

class ClientSocket:

    def __init__(self, address, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((address, port))

    def send_request(self, method: str, endpoint: str, query: str):
        self.client_socket.send(f'{method} {endpoint}?{query} HTTP1.1'.encode(encoding='iso-8859-1'))

    def get_response(self):
        response = self.client_socket.recv(4096)
        response.decode()
        self.client_socket.close()
        return response