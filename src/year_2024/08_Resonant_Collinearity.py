from aoc.io import *
from aoc.grid import *
from aoc.primitives import *
from aoc import algo
from collections import defaultdict
import itertools as itls


field = Field(readlines())
antennas = defaultdict(list)
for pos, v in field.cellsv():
    if v != '.':
        antennas[v].append(pos)


def get_antinodes1(items):
    for a, b in itls.combinations(items, 2):
        delta = (b - a).normalize()
        for i, x in enumerate(field.takewhile_inside(field.grid.beam(a, delta, False))):
            if x != a and x != b:
                db = x - b
                if abs(db.x // delta.x) == (i+1)*2 or abs(db.x // delta.x) * 2 == i+1:
                    yield x
        
        for i, x in enumerate(field.takewhile_inside(field.grid.beam(a, -delta, False))):
            if x != a and x != b:
                db = x - b
                if abs(db.x // delta.x) == (i+1)*2 or abs(db.x // delta.x) * 2 == i+1:
                    yield x


def get_antinodes(items):
    for a, b in itls.combinations(items, 2):
        yield from field.beam_to(a, b)
        yield from field.beam_to(b, a)


antinodes = set()
for vals in antennas.values():
    antinodes.update(get_antinodes1(vals))
antinodes.difference_update(antennas)
print('Star 1:', len(antinodes))


antinodes = set()
for vals in antennas.values():
    antinodes.update(get_antinodes(vals))
print('Star 2:', len(antinodes))