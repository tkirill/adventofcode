from aoc.io import *
from aoc.grid import *
from aoc.primitives import *
from aoc import algo
import itertools as itls
import more_itertools as mitls


def walk(field, cur):
    walker = GridWalker(cur, velocity=field.grid.delta_up)
    yield walker
    while True:
        n = walker.step()
        if n.pos not in field:
            break
        if field[n.pos] != '#':
            walker = n
            yield walker
        else:
            walker = walker.rotatelr('R')


field = Field(read(parse=list))
start = [p for p, v in field.cellsv() if v == '^'][0]
visited = {w.pos for w in walk(field, start)}
print('Star 1:', len(visited))


result = 0
for p in visited:
    if p == start:
        continue
    field[p] = '#'
    if algo.detect_cycle(walk(field, start)) is not None:
        result += 1
    field[p] = '.'
print('Star 2:', result)