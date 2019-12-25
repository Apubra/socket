import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
# Send data to server
# s.sendall(b'I am Client...')
s.send(bytes("Hey there, I am from Client!!!","utf-8"))

# Receive data from server
msg = s.recv(1024)
print(msg.decode("utf-8"))