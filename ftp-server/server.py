import socket
import os
import shutil

'''
pwd - показывает название рабочей директории
ls - показывает содержимое текущей директории
cat <filename> - отправляет содержимое файла
mkdir <filename> - создание новой папки
rmdir <filename> - удаление папки
rename <filename> - изменение название папки
copy_to_server название_файла_на_сервере директория_название_файла_клиента - копирование файла с клиента на сервер
copy_to_server название_файла_на_сервере директория_название_файла_клиента - копирование файла с сервера на клиент
'''

dirname = os.path.join(os.getcwd(), 'docs')


def process(req):

    if req == 'pwd':
        return dirname
    elif req == 'ls':
        return '; '.join(os.listdir(dirname))
    elif req[:3] == 'cat':
        path = os.path.join(os.getcwd(), 'docs', req[4:])
        if os.path.exists(path):
            with open(path, 'r+') as file:
                line = ''
                for l in file:
                    line += l
            return line
        else:
            return 'Файла не существует'

    elif req[:5] == 'mkdir':
        path = os.path.join(os.getcwd(), 'docs', req[5:])
        if not os.path.exists(path):
            os.mkdir(path)
            return 'Папка успешно создана'
        return 'Папка скорее всего уже создана'

    elif req[:5] == 'rmdir':
        path = os.path.join(os.getcwd(), 'docs', req[5:])
        if os.path.exists(path):
            os.rmdir(path)
            return 'Папка успешно удалена'
        return 'Папка скорее всего уже удалена'

    elif req[:6] == 'rename':
        req = req.split()
        path1 = os.path.join(os.getcwd(), 'docs', req[1])
        path2 = os.path.join(os.getcwd(), 'docs', req[2])
        if os.path.exists(path1):
            os.rename(path1, path2)
            return 'Файл успешно переименован'
        return 'Такого файла не существует'

    elif req[:14] == 'copy_to_server':
        req = req.split()
        path = os.path.join(os.getcwd(), 'docs', req[1])
        shutil.copyfile(req[2], path)
        return 'Файл успешно скопирован'

    elif req[:16] == 'copy_from_server':
        req = req.split()
        path = os.path.join(os.getcwd(), 'docs', req[1])
        shutil.copyfile(path, req[2])
        return 'Файл успешно скопирован'

    return 'bad request'


def main():
    PORT = 6987

    sock = socket.socket()
    sock.bind(('', PORT))
    sock.listen()
    print("Прослушиваем порт", PORT)

    while True:
        conn, addr = sock.accept()

        request = conn.recv(1024).decode()
        print(request)

        if request == 'exit':
            conn.close()

        response = process(request)
        conn.send(response.encode())


if __name__ == '__main__':
    main()
