import socket
import threading
import random

def get_answer(name):
    # secret
    return name

def process_connection(addr, conn):
    number = random.randint(1,100)

    try:
        while True:
            guess = int(conn.recv(128).decode('utf-8'))

            if guess == number:
                conn.send('Yes'.encode('utf-8'))
                client_name = conn.recv(128).decode('utf-8')
                answer = get_answer(client_name)
                conn.send(answer.encode('utf-8'))
                conn.close()
                break
            else:
                conn.send('No'.encode('utf-8'))
    except:
        conn.send('Not a number'.encode('utf-8'))
        conn.close()

sock = socket.socket()
sock.bind(('185.247.118.6', 2223))
sock.listen(1)

while True:
    try:
        conn, addr = sock.accept()
        process_connection(addr, conn)
    except Exception as e:
        print(e)
