from socket import *
from threading import Thread
from queue import Queue

THREAD_POOL_SIZE = 16

class Socket:

    def __init__(self, address, port, controller) -> None:
        self.server_socket = socket(AF_INET,SOCK_STREAM)
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.server_socket.bind((address, port))
        self.server_socket.listen(1)
        self.controller = controller
        self.job_pool = Queue()
        self.init_threads()
        print(f'The server is ready to receive on port:{port}')

    def start_listening(self):
        try:
            while True:
                socket, addr = self.server_socket.accept()
                decoded_message = socket.recv(1024).decode()

                print(f'{"-" * 30}')
                splitted_request = decoded_message.split()[1].split('?', 1)
                if len(splitted_request) > 2:
                    print(f'Unknown request: {splitted_request[0]}')
                    print(f'Skipping...')
                    continue

                if len(splitted_request) == 1:
                    splitted_request.append('')

                endpoint, query = splitted_request
                args = dict(arg.split('=') for arg in query.split('&')) if query != '' else dict()

                self.job_pool.put((socket, endpoint, args))
        except KeyboardInterrupt:
            self.exit()

    def init_threads(self):
        self.threads = [Thread(target=self.worker_thread) for _ in range(THREAD_POOL_SIZE)]
        
        for t in self.threads:
            t.start()

    def worker_thread(self):
        while True:
            socket, endpoint, args = self.job_pool.get()

            if socket == None:
                return
            
            host, port = socket.getpeername()

            print(f'Connection established. Host: {host}, Port:{port}')
            print(f'Endpoint: {endpoint}')
            print(f'Query: {args}')

            self.controller(socket, endpoint, args)

            print(f'Connection terminated.')

    def exit(self):
        for _ in range(THREAD_POOL_SIZE):
            self.job_pool.put((None, None, None))

        for t in self.threads:
            t.join()
        
        self.server_socket.shutdown(SHUT_RDWR)