from aoc.io import *
from aoc.grid import *
from aoc.primitives import *
from collections import defaultdict
import itertools as itls


field = Field(readlines())
antennas = defaultdict(list)
for pos, v in field.cellsv():
    if v != '.':
        antennas[v].append(pos)


def get_antinodes(a: Vec2, b: Vec2) -> Iterable[Vec2]:
    yield from field.beam_to(a, b)
    yield from field.beam_to(b, a)


def get_antinodes_part1(a: Vec2, b: Vec2) -> Iterable[Vec2]:
    a = [2 * a - b, 2 * b - a]
    yield from field.inside(a)


# Expected answer for the input `...x..x...` is `#..x..x..#`.
# This version answers with `#..x##x..#`.
# Both versions are accepted though.
def get_antinodes_part1_v2(a: Vec2, b: Vec2) -> Iterable[Vec2]:
    for x in get_antinodes(a, b):
        da, db = x - a, x - b
        if abs(da) == 2 * abs(db) or abs(db) == 2 * abs(da):
            yield x


antinodes = set()
for items in antennas.values():
    for a, b in itls.combinations(items, 2):
        antinodes.update(get_antinodes_part1(a, b))
print('Star 1:', len(antinodes))


antinodes = set()
for items in antennas.values():
    for a, b in itls.combinations(items, 2):
        antinodes.update(get_antinodes(a, b))
print('Star 2:', len(antinodes))