from aoc.io import *
from aoc.grid import *
from itertools import *
import math


field = Field([list(map(int, l)) for l in readlines()])


def get_visible_forward(arr: list[(Vec2, int)]) -> Iterable[Vec2]:
    curmax = -1
    for pos, v in arr:
        if v > curmax:
            yield pos
            curmax = v


def get_visible_2ways(arr: list[(Vec2, int)]) -> set[Vec2]:
    return set(get_visible_forward(arr)) | set(get_visible_forward(reversed(arr)))


def get_visible_2d(field: Field):
    visible = set(chain.from_iterable(get_visible_2ways(list(row)) for row in field.rowsv()))
    visible.update(chain.from_iterable(get_visible_2ways(list(col)) for col in field.columnsv()))
    return visible


def get_visible_from(field: Field, cur: Vec2) -> int:
    cur_val = field[cur]
    scores = []
    for beam in field.beam4v(cur, skip_start=True):
        total = 0
        for pos, v in beam:
            total += 1
            if v >= cur_val:
                break
        scores.append(total)
    return math.prod(scores)


print('Star 1:', len(get_visible_2d(field)))
print('Star 2:', max(get_visible_from(field, pos) for pos in field.cells()))