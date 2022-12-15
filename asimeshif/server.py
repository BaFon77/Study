import socket
import pickle
import os
import re
import random


def receip_host():
    sock = socket.socket()
    sock.bind(('127.0.0.1', 8080))
    sock.listen(1)
    conn, addr = sock.accept()
    host = int(pickle.loads(conn.recv(1024)))
    sock.close()
    conn.close()
    return host

host = receip_host()
sock = socket.socket()
sock.bind(('127.0.0.1', host))
sock.listen(1)
conn, addr = sock.accept()


def crypt(data, keypublic, keyprivate):
    return ''.join(map(chr, [x - keypublic - keyprivate for x in map(ord, data)]))


def generation_key(conn):
    msg = conn.recv(1024)
    p, g, A = pickle.loads(msg)
    accept_list = [i for i in range(0, 100)]
    if int(A) in accept_list:
        b = random.randint(744, 983)
        B = g ** b % p
        K = A ** b % p
        return B, K
    else:
        conn.close()


def cheack_file_key(conn):
    public_key, private_key = generation_key(conn)
    if os.path.isfile('server_key.txt'):
        if os.stat('server_key.txt').st_size == 0:
            f = open('server_key.txt', "r+")
            file_info = f"Public key:\n{str(public_key)}\nPrivate key:\n{str(private_key)}"
            f.write(file_info), f.close()
            f = open('server_key.txt', "r+")
            lines = f.readlines()
            return lines
        else:

            f = open('server_key.txt', "r+")
            lines = f.readlines()
            return lines
    else:
        f = open('server_key.txt', "w")
        file_info = f"Public key:\n{str(public_key)}\nPrivate key:\n{str(private_key)}"
        f.write(file_info), f.close()
        f = open('server_key.txt', "r+")
        lines = f.readlines()
        return lines


def main():
    data = cheack_file_key(conn)
    public_key = int(data[1].replace('\n', ''))
    private_key = int(data[3])
    conn.send(pickle.dumps(public_key))

    while True:
        msg = conn.recv(1024)
        if not msg:
            break
        print(pickle.loads(msg))
        print(crypt(pickle.loads(msg), private_key, public_key))
    conn.close()


if __name__ == '__main__':
    main()
