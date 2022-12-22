from socket import *
from threading import Thread, Semaphore
HTTP_VERSION = "HTTP/1.1"
response_strings = {
    200: "200 OK",
    401: "401 Unauthorized",
    403: "403 Forbidden",
    404: "404 Not Found"
}

semaphore = Semaphore(8)
class Socket:

    __endpoints: dict
    __current_response: str

    def __init__(self, endpoints, address = "0.0.0.0", port = 8000) -> None:
        self.serverSocket = socket(AF_INET,SOCK_STREAM)
        self.serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.serverSocket.bind((address, port))
        self.serverSocket.listen(1)
        self.HTTP_VERSION = "HTTP/1.1"
        self.current_response = ""
        self.__endpoints = endpoints
        print('The server is ready to receive')

    def start_listening(self):
        count = 0
        while True:
            connection_socket, addr = self.serverSocket.accept()
            decoded_message = connection_socket.recv(1024).decode()

            endpoint, query = decoded_message.split()[1].split('?', 1)
            args = dict(arg.split('=') for arg in query.split('&'))
            args['socket'] = connection_socket
            args['semaphore'] = thread_exit

            self.initialize_response(200).add_response_header("Content-Type", "text/html").add_response_body(f"""{count}\n""").encode_current_response()
            count += 1
            args['response'] = self.current_response
            self.current_response = ""
            
            print(semaphore._value)
            semaphore.acquire()
            x = Thread(target=self.__endpoints[endpoint], args=args.values())
            x.start()


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


def thread_exit():
    semaphore.release()