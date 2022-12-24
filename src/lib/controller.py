HTTP_VERSION = "HTTP/1.1"
response_strings = {
    200: "200 OK",
    401: "401 Unauthorized",
    403: "403 Forbidden",
    404: "404 Not Found"
}

class Controller:
    
    def __init__(self, socket):
        self.socket = socket
        self.current_response = ""

    def initialize_response(self, status):
        response_string = response_strings[status]
        if response_string == None:
            self.current_response += "-1 Invalid Status Code"
        else:
            self.current_response += f"{HTTP_VERSION}  {response_string}"
        self.current_response += "\n"
        return self

    def add_header(self, key, value):
        self.current_response += f"{key}: {value}\n"
        return self
    
    def add_body(self, body):
        self.current_response += f"\n{body}"
        return self

    def encode(self):
        self.current_response = self.current_response.encode(encoding='iso-8859-1')
        return self
    
    def send(self):
        self.socket.sendall(self.current_response)

    def exit(self):
        self.socket.close()