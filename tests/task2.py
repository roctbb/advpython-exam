import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 2223))

for i in range(1,101):
    sock.send(str(i).encode('utf-8'))
    a = sock.recv(128).decode('utf-8')

    if a == 'Yes':
        sock.send("Ростислав".encode('utf-8'))
        print(sock.recv(128).decode('utf-8'))
        sock.close()
        break