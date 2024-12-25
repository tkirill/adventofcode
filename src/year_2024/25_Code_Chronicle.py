from aoc.io import *
from aoc.grid import *


blocks = readblocks()
keys, locks = [], []

for b in blocks:
    is_key = b[0][0] == '.'
    nb = b[:-1] if is_key else b[1:]
    m = Field(nb)
    hs = []
    for c in m.columnsv():
        hs.append(sum(1 for _, v in c if v == '#'))
    if is_key:
        keys.append(hs)
    else:
        locks.append(hs)

result = 0
for key in keys:
    for lock in locks:
        if all(kh + lh < 6 for kh, lh in zip(key, lock)):
            result += 1
print('Star 1:', result)