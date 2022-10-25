import socket

sock = socket.socket()
sock.setblocking(True)

def send():
    while True:
        data = sock.recv(1024)
        print(data.decode())

try:
    host = input("Введите имя хоста: ")
    port = int(input("Введите номер порта: "))
    addr = (host, port)
    sock.connect(addr)
except Exception:
    sock.connect(('localhost', 9090))

password = input("Введите пароль: ")
sock.send(passwod.encode())
send()

while True:
    data = input()
    if data != "exit":
        sock.send(data.encode())
        break

sock.send("Client disconnected".encode())
sock.close()