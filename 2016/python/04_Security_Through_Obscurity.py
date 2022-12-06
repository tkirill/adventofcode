from aoc import *
import itertools as itls
from collections import Counter
import string


ENG = string.ascii_lowercase


rooms = read(sep=r'-|\[|\]')
total = 0
for *name, sid, checksum, _ in rooms:
    c = Counter(itls.chain.from_iterable(name))
    keys = ''.join(sorted(c.keys(), key=lambda k: (-c[k], k)))
    if keys.startswith(checksum):
        total += sid
print('Star 1:', total)


for *name, sid, checksum, _ in rooms:
    decrypted = []
    for c in ' '.join(name):
        if c == ' ':
            decrypted.append(' ')
        else:
            tmp = (ENG.index(c) + sid) % len(ENG)
            decrypted.append(ENG[tmp])
    decrypted = ''.join(decrypted)
    if 'northpole' in decrypted:
        print('Star 2:', sid, decrypted)
        break