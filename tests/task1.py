import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 2222))

sock.send('Ростислав'.encode('utf-8'))
print(sock.recv(128).decode('utf-8'))