from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('0.0.0.0', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
print(    """
HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<HTML>
<HEAD>
<TITLE>Room Added</TITLE>
</HEAD>
<BODY>Room with name M2Z08 is successfully added.</BODY>
</HTML>
    """.encode(encoding='iso-8859-1'))
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    print(sentence)
    connectionSocket.sendall(
    """
HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<HTML>
<HEAD>
<TITLE>Room Added</TITLE>
</HEAD>
<BODY>Room with name M2Z08 is successfully added.</BODY>
</HTML>
    """.encode(encoding='iso-8859-1'))
    connectionSocket.close()