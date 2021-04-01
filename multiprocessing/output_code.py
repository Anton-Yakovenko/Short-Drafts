"""Connection between 2 apps (second app)"""

import socket


def server():
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(1)
    conn, addr = sock.accept()
    print('connected:', addr)

    while True:
        data = conn.recv(1024)
        output_data(data.decode())
        if not data:
            break
        conn.send(data.upper())

    conn.close()


def output_data(data):
    print(data)


if __name__ == '__main__':
    server()




