from aoc import *
from itertools import permutations
import more_itertools as mtls


sides = read(sep='\s+')
total = 0
for side in sides:
    total += int(all(p[0] + p[1] > p[2] for p in permutations(side)))
print('Star 1:', total)


total = 0
for row in columns(sides):
    for side in mtls.chunked(row, 3):
        total += int(all(p[0] + p[1] > p[2] for p in permutations(side)))
print('Star 2:', total)