import socket, re

from lib.html_result import HTMLResult

class ClientSocket:

    def __init__(self, address, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((address, port))

    def send_request(self, method: str, endpoint: str, query: str):
        self.client_socket.send(f'{method} {endpoint}?{query} HTTP1.1'.encode(encoding='iso-8859-1'))

    def get_HTML_response(self):
        response = self.client_socket.recv(4096).decode()
        self.client_socket.close()
        
        status = int(re.findall('HTTP/1.1 (\d+)', response)[0])
        title = re.findall('<TITLE>(.*)</TITLE>', response)[0]
        body = re.findall('<BODY>(.*)</BODY>', response)[0]

        return HTMLResult(status, title, body)