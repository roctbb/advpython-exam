import socket


def process(name):
    return '_'.join([str(ord(s) - ord('а')) for s in name.lower()])


sock = socket.socket()
sock.bind(('0.0.0.0', 2222))
sock.listen(1)

while True:
    try:
        conn, addr = sock.accept()
        name = conn.recv(128).decode('utf-8')
        result = process(name)
        conn.send(result.encode('utf-8'))
        conn.close()
    except Exception as e:
        print(e)
