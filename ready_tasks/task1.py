import socket


def process(name):
    # secret
    return name


sock = socket.socket()
sock.bind(('185.247.118.6', 2222))
sock.listen(1)

while True:
    try:
        conn, addr = sock.accept()
        name = conn.recv(128).decode('utf-8')
        result = process(name)
        conn.send(result.encode('utf-8'))
        conn.close()
    except:
        pass
