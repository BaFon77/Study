import socket
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

def func(conn, addr):
    password = str(conn.recv(1024).decode())
    with open("data_password.txt", "r", encoding="utf-8") as file:
        for i in file:
            if str(addr[0]) == i.split(";")[0] and password == i.split(";")[1]:
                break
        else:
            print("Error")
            with open("data_password.txt", "a", encoding="utf-8") as file1:
                file1.write(str(addr[0]) + ";" + str(password))
            with open("data_log.txt") as file2:
                file2.write(str(addr) + " connected\n")


    while True:
        data = conn.recv(1024)
        if not data:
            break
        if data != 'exit':
            conn.send(data.upper())
        else:
            with open("data_log.txt", "a", encoding="utf-8") as file3:
                file3.write(str(addr) + " disconnected\n")
                break
    conn.close()