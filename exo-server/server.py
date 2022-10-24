import socket
print('Запуск сервера')
sock = socket.socket()
sock.bind(('', 9090))
print('Начало прослушивания порта')
sock.listen(1)
conn, addr = sock.accept()
print('Подключение клиента')
while True:
    data = conn.recv(1024)
    print('Прием данных от клиента')
    if not data:
        break
    conn.send(data.upper())
    print('Отправка данных клиенту')
conn.close()
print('Отключение клиента')
print('Остановка сервера')