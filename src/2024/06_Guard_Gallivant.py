from aoc.io import *
from aoc.grid import *
from aoc.primitives import *
from aoc import algo
import itertools as itls
import more_itertools as mitls


def walk(field, cur):
    walker = GridWalker(cur, velocity=field.grid.delta_up)
    while True:
        n = walker.step()
        if n.pos not in field:
            break
        if field[n.pos] != '.':
            walker = walker.rotatelr('R')
        else:
            walker = n
            yield walker


field = Field(read(parse=list))
start = [p for p, v in field.cellsv() if v == '^'][0]
field[start] = '.'
visited = {start}
for w in walk(field, start):
    visited.add(w.pos)
print('Star 1:', len(visited))


result = 0
for p, v in field.cellsv():
    if p == start or v != '.':
        continue
    nf = Field(read(parse=list))
    nf[start] = '.'
    nf[p] = '#'
    if algo.detect_cycle(walk(nf, start)) is not None:
        result += 1
print('Star 2:', result)