import socket
import pickle

sock = socket.socket()
sock.bind(('127.0.0.1', 8080))
sock.listen(1)
conn, addr = sock.accept()


def crypt(data, keypublic, keyprivate):
    return ''.join(map(chr, [x - keypublic - keyprivate for x in map(ord, data)]))


def main():
    global K, B, A
    msg = conn.recv(1024)
    p, g, A = pickle.loads(msg)
    b = 9
    B = g ** b % p
    K = A ** b % p
    conn.send(pickle.dumps(B))

    while True:
        msg = conn.recv(1024)
        if not msg:
            break
        print(pickle.loads(msg))
        print(crypt(pickle.loads(msg), K, B))
    conn.close()


if __name__ == '__main__':
    main()
