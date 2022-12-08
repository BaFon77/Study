import socket

HOST = 'localhost'
PORT = 6987

while True:
    try:
        request = input('>')

        sock = socket.socket()
        sock.connect((HOST, PORT))

        sock.send(request.encode())

        response = sock.recv(1024).decode()
        print(response)

        sock.close()
    except ConnectionRefusedError:
        print('Успешное отключение от сервера')
        break