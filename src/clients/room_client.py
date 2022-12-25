from lib.client_socket import ClientSocket
from lib.html_result import HTMLResult

class RoomClient(ClientSocket):
    
    def __init__(self):
        super().__init__('0.0.0.0', 8081)

    def add(self, name: str) -> HTMLResult:
        self.send_request('POST', '/add', f'name={name}')
        return self.get_HTML_response()

    def remove(self, name: str) -> HTMLResult:
        self.send_request('DELETE', '/remove', f'name={name}')
        return self.get_HTML_response()

    def reserve(self, name: str, day: int, hour: int, duration: int) -> HTMLResult:
        self.send_request('POST', '/reserve', f'name={name}&day={day}&hour={hour}&duration={duration}')
        return self.get_HTML_response()

    def check_availability(self, name: str, day: int) -> HTMLResult:
        self.send_request('GET', '/checkavailability', f'name={name}&day={day}')
        return self.get_HTML_response()