import socket
import pickle
from random import randint


def connection():
    with socket.socket() as s:
        s.connect(('127.0.0.1', 8080))
        host = input('Host:')
        s.send(pickle.dumps(host))
        print(host)
        return int(host)

p, g, a = 7, 5, 5
A = g ** a % p
sock = socket.socket()
sock.connect(('127.0.0.1', connection()))

sock.send(pickle.dumps((p, g, A)))


def crypt(data, keypublic, keyprivate):
    return ''.join(map(chr, [x + keypublic + keyprivate for x in map(ord, data)]))


def generate_key():
    global K, B
    msg = sock.recv(1024)
    B = pickle.loads(msg)
    K = B ** a % p


def main():
    msg = ''
    while msg != 'exit':
        msg = input('Введите своё сообщение: ')
        sock.send(pickle.dumps(crypt(msg, K, B)))
    sock.close()


if __name__ == '__main__':
    generate_key()
    main()