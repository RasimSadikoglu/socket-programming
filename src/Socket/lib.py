from socket import *
HTTP_VERSION = "HTTP/1.1"
response_strings = {
    200: "200 OK",
    401: "401 Unauthorized",
    403: "403 Forbidden",
    404: "404 Not Found"
}
class Socket:
    def __init__(self, address = "0.0.0.0", port = 8000,) -> None:
        self.serverSocket = socket(AF_INET,SOCK_STREAM)
        self.serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.serverSocket.bind((address, port))
        self.serverSocket.listen(1)
        self.HTTP_VERSION = "HTTP/1.1"
        self.current_response = ""
        print('The server is ready to receive')

    def start_listening(self):
        while True:
            connection_socket, addr = self.serverSocket.accept()
            decoded_message = connection_socket.recv(1024).decode()
            self.initialize_response(200).add_response_header("Content-Type", "text/html").add_response_body("""
<!DOCTYPE html>
<HTML>
<HEAD>
<TITLE>Room Added</TITLE>
</HEAD>
<BODY>Room with name M2Z08 is successfully added.</BODY>
</HTML>     
            """).encode_current_response().send_response(connection_socket)

    def initialize_response(self, status):
        response_string = response_strings[status]
        if response_string == None:
            self.current_response += "-1 Invalid Status Code"
        else:
            self.current_response += f"{HTTP_VERSION}  {response_string}"
        self.current_response += "\n"
        return self

    def add_response_header(self, key, value):
        self.current_response += f"{key}: {value}\n"
        return self
    
    def add_response_body(self, body):
        self.current_response += f"\n{body}"
        return self

    def encode_current_response(self):
        self.current_response = self.current_response.encode(encoding='iso-8859-1')
        return self
    
    def send_response(self, connection_socket):
        connection_socket.sendall(self.current_response)
        connection_socket.close()
        self.current_response = ""