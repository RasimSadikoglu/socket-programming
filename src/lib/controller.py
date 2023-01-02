import json

from lib.html_result import HTMLResult

HTTP_VERSION = "HTTP/1.1"
response_strings = {
    200: "200 OK",
    400: "400 Bad Request",
    401: "401 Unauthorized",
    403: "403 Forbidden",
    404: "404 Not Found"
}

class Controller:
    
    def __init__(self, socket, endpoints, endpoint, args, business):
        self.socket = socket
        self.current_response = ""
    
        self.business = business()

        try:
            endpoints[endpoint](**args)
        except KeyError as ke:
            self.send_unknown_request()
        except TypeError as te:
            self.send_unknown_query(str(te))
        except ValueError as ve:
            self.send_key_error(str(ve))

        self.exit()

    def initialize_response(self, status):
        response_string = response_strings[status]
        if response_string == None:
            self.current_response += "-1 Invalid Status Code"
        else:
            self.current_response += f"{HTTP_VERSION} {response_string}"
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

    def send_json(self, status, body):
        self.initialize_response(status) \
            .add_header('Content-Type', 'application/json') \
            .add_body(json.dumps(body)) \
            .encode() \
            .send()

    def send_html(self, response: HTMLResult):
        self.initialize_response(response.status) \
            .add_header('Content-Type', 'text/html') \
            .add_body(f'<HTML><HEAD><TITLE>{response.title}</TITLE></HEAD><BODY>{response.body}</BODY></HTML>') \
            .encode() \
            .send()

    def send_unknown_request(self):
        self.send_html(HTMLResult(404, 'Error', '404 Not Found'))

    def send_unknown_query(self, error):
        self.send_html(HTMLResult(400, 'Error', f'Unexpected query argument: {error}'))

    def send_key_error(self, error):
        self.send_html(HTMLResult(400, 'Error', f'Mismatched type error occured: {error}'))

    def exit(self):
        self.socket.close()