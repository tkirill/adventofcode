from aoc import *
from hashlib import md5
import itertools as itls


def iterhashes(prefix):
    for i in itls.count():
        tmp = id + str(i)
        hash = md5(tmp.encode('ascii')).hexdigest()
        if hash.startswith('0'*5):    
            yield hash


id = read()[0]
password = []
for hash in iterhashes(id):
    password.append(hash[5])
    if len(password) == 8:
        break
print('Star 1:', ''.join(password))


password = ['']*8
for hash in iterhashes(id):
    if hash[5].isdigit():
        tmp = int(hash[5])
        if 0 <= tmp < len(password) and not password[tmp]:
            password[tmp] = hash[6]
            if all(password):
                break
print('Star 2:', ''.join(password))