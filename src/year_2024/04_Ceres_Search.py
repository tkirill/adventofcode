from aoc.io import *
from aoc.grid import *
from aoc.primitives import *
from aoc import algo
import itertools as itls
import more_itertools as mitls


field = Field(readlines())


def count_xmas(pos):
    r = 0
    for beam in field.beam8v(pos):
        word = ''.join(v for p, v in itls.islice(beam, 4))
        if word == 'XMAS':
            r += 1
    return r


def count_x_mas(pos):
    corners = list(field.inside([
        field.grid.up_left(pos),
        field.grid.up_right(pos),
        field.grid.down_left(pos),
        field.grid.down_right(pos)]))
    if len(corners) != 4:
        return 0
    ul, ur, dl, dr = [field[p] for p in corners]
    words = [f'{ul}A{dr}', f'{ur}A{dl}']
    return all(w in ['MAS', 'SAM'] for w in words)


print('Star 1:', sum(count_xmas(pos) for pos, v in field.cellsv() if v == 'X'))
print('Star 2:', sum(count_x_mas(pos) for pos, v in field.cellsv() if v == 'A'))