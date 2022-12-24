from lib.client_socket import ClientSocket

class RoomClient(ClientSocket):
    
    def __init__(self):
        super().__init__('0.0.0.0', 8002)

    def add(self, name: str):
        self.send_request('POST', '/add', f'name={name}')
        return self.get_response()

    def remove(self, name: str):
        self.send_request('DELETE', '/remove', f'name={name}')
        return self.get_response()

    def reserve(self, name: str, day: int, hour: int, duration: int):
        self.send_request('POST', '/remove', f'name={name}&day={day}&hour={hour}&duration={duration}')
        return self.get_response()

    def check_availability(self, name: str, day: int):
        self.send_request('GET', '/remove', f'name={name}&day={day}')
        return self.get_response()