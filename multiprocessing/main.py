"""LEARNING MULTIPROCESSING"""

import socket
from multiprocessing import Process


def client():
    data = 'ara'
    sock = socket.socket()
    sock.connect(('localhost', 9090))
    sock.send(data.encode())

    new_data = sock.recv(1024)
    sock.close()

    print('[CLIENT] ', data, new_data.decode())


def server():
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(1)
    conn, addr = sock.accept()
    print('[SERVER] connected:', addr)

    while True:
        data = conn.recv(1024)
        print('[SERVER] ', data.decode())
        if not data:
            break
        conn.send(data.upper())

    conn.close()


if __name__ == '__main__':
    output_code = Process(target=server)
    input_code = Process(target=client)

    output_code.start()
    input_code.start()

    output_code.join()
    input_code.join()

