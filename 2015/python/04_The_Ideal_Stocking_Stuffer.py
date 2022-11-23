from hashlib import md5
from itertools import count
from typing import Iterable


def mining(prefix) -> Iterable[tuple[int, str]]:
    for i in count():
        yield i, md5((prefix + str(i)).encode('ascii')).hexdigest()


line = open('04_input.txt').readline().strip()

for i, hash in mining(line):
    if hash.startswith('00000'):
        print('Star 1:', i)
        break
for i, hash in mining(line):
    if hash.startswith('000000'):
        print('Star 2:', i)
        break