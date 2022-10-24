import socket

sock = socket.socket()
sock.setblocking(True)
sock.connect(('localhost', 9090))
print('Соединение с сервером')
while True:
    msg = input()
    sock.send(msg.encode())
    print('Отправка данных серверу')
    if msg == 'exit':
        break
    data = sock.recv(1024)
    print('Прием данных от сервера')
    print(data.decode())
sock.close()
print('Разрыв соединения с сервером')