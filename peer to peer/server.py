import socket

# create the socket
# AF_INET == ipv4
# SOCK_STREAM == TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print('True...')
    print(f"Connection from {address} has been established.")
    # Receive from client
    data = clientsocket.recv(1024)
    print(data.decode("utf-8"))

    # Send data to client
    clientsocket.send(bytes("Hey there, I am from Server!!!","utf-8"))
    clientsocket.close()