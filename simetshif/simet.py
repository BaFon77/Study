from collections import Counter
from random import randint


def encrypt(key, data):
    '''Кодирования - шифр Цезаря'''
    return ''.join(map(chr, [x + key for x in map(ord, data)]))


def decrypt(key, data):
    '''Декодирования - шифр Цезаря'''
    return ''.join(map(chr, [x - key for x in map(ord, data)]))


def cesar_hack(data):
    '''Взлом - шифр Цезаря'''
    maximum = Counter(data).most_common()[0][0]
    key = ord(maximum) - ord(' ')
    return decrypt(key, data)


def enven(data):
    '''Кодирования - шифр Вернама'''
    keys = ''
    itog = ''
    for i in data:
        key = randint(0, 33)
        keys += str(key) + " "
        itog += chr((ord(i) + key))
    return [itog, keys]


def deven(itog, keys):
    '''Декодирования - шифр Вернама'''
    keys = keys.split()
    decrypta = ""
    for k, c in enumerate(itog):
        sdf = ord(c) - int(keys[k])
        decrypta += chr(sdf)
    return decrypta


if __name__ == '__main__':
    data = 'Это самое ужасное рассуждение: если я не могу всего — значит, я ничего не буду делать.'
    print('№1')
    print(encrypt(3, data))
    print(decrypt(3, encrypt(3, data)))
    print('№2')
    print(cesar_hack(encrypt(3, data)))
    print('№3')
    a = enven(data)
    print(a)
    print(deven(a[0], a[1]))
