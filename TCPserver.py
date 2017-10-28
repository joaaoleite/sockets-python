


import socket
ServerSock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ServerSock.bind(('localhost',7007))
ServerSock.listen(5)
(NewClientSock, addr) = ServerSock.accept()

while(True):
    ClientMessage = NewClientSock.recv(1000)
    if ClientMessage != '':
        print ClientMessage
        NewClientSock.send('xiu')
        break

NewClientSock.close()
