from utils import *
from collections import Counter, defaultdict
import re
import itertools
import functools
import matplotlib.pyplot as plt


algo, img = read('20_input.txt')
img = {(r, c): val for r, c, val in cells(img)}

for ii in range(50):
    nimg = dict()
    lookup = set()
    for r, c in img:
        for rr in range(r-1, r+2):
            for cc in range(c-1, c+2):
                lookup.add((rr, cc))
    for r, c in lookup:
        bits = []
        for rr in range(r-1, r+2):
            for cc in range(c-1, c+2):
                val = img.get((rr, cc), '#' if ii%2 else '.')
                bits.append('1' if val == '#' else '0')
        pos = int(''.join(bits), 2)
        nimg[(r, c)] = algo[pos]
    img = nimg
    if ii == 1:
        print('Star 1:', sum(1 for x in img.values() if x == '#'))
print('Star 2:', sum(1 for x in img.values() if x == '#'))


x, y = [], []
for (r, c), val in img.items():
    if val == '#':
        x.append(c)
        y.append(r)
plt.scatter(x, y, s=1, marker='s')
plt.show()