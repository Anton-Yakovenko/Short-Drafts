"""Connection between 2 apps (first app)"""

import socket


def input_data():       # simple input
    user_data = input('Your data: ')
    client(user_data)


def client(data):
    sock = socket.socket()
    sock.connect(('localhost', 9090))
    sock.send(data.encode())

    new_data = sock.recv(1024)
    sock.close()

    print(data, new_data.decode())


if __name__ == '__main__':
    input_data()



