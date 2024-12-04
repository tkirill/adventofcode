from aoc.io import *
from aoc.grid import *
from aoc.primitives import *
from aoc import algo
import itertools as itls
import more_itertools as mitls


NEXT_LETTER = {
    'X': 'M',
    'M': 'A',
    'A': 'S'
}
field = Field(readlines())


def beam8(pos):
    yield field.beam_up_leftv(pos)
    yield field.beam_upv(pos)
    yield field.beam_up_rightv(pos)
    yield field.beam_rightv(pos)
    yield field.beam_down_rightv(pos)
    yield field.beam_downv(pos)
    yield field.beam_down_leftv(pos)
    yield field.beam_leftv(pos)



def try_find(pos):
    r = 0
    for beam in beam8(pos):
        word = ''.join(v for p, v in itls.islice(beam, 4))
        if word == 'XMAS':
            r += 1
    return r


print('Star 1:', sum(try_find(pos) for pos, v in field.cellsv() if v == 'X'))