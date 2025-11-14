from aoc.io import *
from collections import Counter


l1, l2 = [], []
for a, b in read():
    l1.append(a)
    l2.append(b)
l1.sort()
l2.sort()

print('Star 1:', sum(abs(a-b) for a, b in zip(l1, l2)))

cc = Counter(l2)
print('Star 2:', sum(a * cc[a] for a in l1))