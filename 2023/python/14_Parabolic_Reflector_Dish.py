from aoc import *
from itertools import takewhile
from more_itertools import last
from typing import Callable


def tilt(
    dish: Field,
    rocks: Iterable[Vec2],
    beamv: Callable[[Vec2], Iterable[tuple[Vec2, str]]],
) -> Iterable[Vec2]:
    for rock in rocks:
        moves = takewhile(lambda x: x[1] == ".", beamv(rock))
        npos = last((p for p, v in moves), rock)
        dish[rock] = "."
        dish[npos] = "O"
        yield npos


def spin_cycle(dish: Field, rocks: Iterable[Vec2]) -> tuple[Vec2]:
    rocks = list(tilt(dish, rocks, dish.beam_upv))
    rocks.sort(key=lambda r: (r.x, r.y))
    rocks = list(tilt(dish, rocks, dish.beam_leftv))
    rocks.sort(key=lambda r: (r.y, r.x), reverse=True)
    rocks = list(tilt(dish, rocks, dish.beam_downv))
    rocks.sort(key=lambda r: (r.x, r.y), reverse=True)
    rocks = list(tilt(dish, rocks, dish.beam_rightv))
    rocks.sort(key=lambda r: (r.y, r.x))
    return tuple(rocks)


dish = Field([list(l) for l in read()])
rocks = [p for p, v in dish.cellsv() if v == "O"]
rocks = tilt(dish, rocks, dish.beam_upv)
print("Star 1:", sum(dish.h - pos.y for pos in rocks))


dish = Field([list(l) for l in read()])
rocks = tuple(p for p, v in dish.cellsv() if v == "O")
c = callchain(lambda r: spin_cycle(dish, r), rocks, yield_init=True)
rocks = nth_with_cycle(c, 1_000_000_000)
print("Star 2:", sum(dish.h - pos.y for pos in rocks))
