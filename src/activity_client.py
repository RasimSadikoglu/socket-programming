from lib.client_socket import ClientSocket

class ActivityClient(ClientSocket):
    
    def __init__(self):
        super().__init__('0.0.0.0', 8001)

    def add(self, name: str):
        self.send_request('POST', '/add', f'name={name}')
        return self.get_response()

    def remove(self, name: str):
        self.send_request('DELETE', '/remove', f'name={name}')
        return self.get_response()

    def check(self, name: str):
        self.send_request('GET', '/check', f'name={name}')
        return self.get_response()