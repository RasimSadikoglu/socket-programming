from lib.client_socket import ClientSocket
from lib.html_result import HTMLResult

class ActivityClient(ClientSocket):
    
    def __init__(self):
        super().__init__('0.0.0.0', 8082)

    def add(self, name: str) -> HTMLResult:
        self.send_request('POST', '/add', f'name={name}')
        return self.get_HTML_response()

    def remove(self, name: str) -> HTMLResult:
        self.send_request('DELETE', '/remove', f'name={name}')
        return self.get_HTML_response()

    def check(self, name: str) -> HTMLResult:
        self.send_request('GET', '/check', f'name={name}')
        return self.get_HTML_response()