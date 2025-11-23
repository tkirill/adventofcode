from typing import Iterable, Optional
from itertools import islice

from aoc.vec2 import Vec2
from aoc.rectangle import Rectangle


UP_LEFT = Vec2(-1, -1)
UP = Vec2(0, -1)
UP_RIGHT = Vec2(1, -1)
RIGHT = Vec2(1, 0)
DOWN_RIGHT = Vec2(1, 1)
DOWN = Vec2(0, 1)
DOWN_LEFT = Vec2(-1, 1)
LEFT = Vec2(-1, 0)
OPPOSITE = {
    UP_LEFT: DOWN_RIGHT,
    UP: DOWN,
    UP_RIGHT: DOWN_LEFT,
    RIGHT: LEFT,
    DOWN_RIGHT: UP_LEFT,
    DOWN: UP,
    DOWN_LEFT: UP_RIGHT,
    LEFT: RIGHT
}


def opposite(direction: Vec2) -> Vec2:
    return OPPOSITE[direction]


def near8(p: Vec2 | Rectangle):
    if isinstance(p, Vec2):
        yield up_left(p)
        yield up(p)
        yield up_right(p)
        yield right(p)
        yield down_right(p)
        yield down(p)
        yield down_left(p)
        yield left(p)
        return
    for cur in beam(up_left(p.top_left), RIGHT, n=p.width+1):
        yield cur
    for cur in beam(right(cur), DOWN, n=p.height+1):
        yield cur
    for cur in beam(down(cur), LEFT, n=p.width+1):
        yield cur
    for cur in beam(left(cur), UP, n=p.height+1):
        yield cur


def up_left(p: Vec2) -> Vec2:
    return p + UP_LEFT


def up(p: Vec2) -> Vec2:
    return p + UP


def up_right(p: Vec2) -> Vec2:
    return p + UP_RIGHT


def right(p: Vec2) -> Vec2:
    return p + RIGHT


def down_right(p: Vec2) -> Vec2:
    return p + DOWN_RIGHT


def down(p: Vec2) -> Vec2:
    return p + DOWN


def down_left(p: Vec2) -> Vec2:
    return p + DOWN_LEFT


def left(p: Vec2) -> Vec2:
    return p + LEFT


def beam(p: Vec2, delta: Vec2, n: Optional[int]=None, skip_start: bool=False) -> Iterable[Vec2]:
    if n is not None:
        yield from islice(beam(p, delta), n)
        return
    cur = p
    if not skip_start:
        yield cur
    while True:
        cur += delta
        yield cur


def mdist(a: Vec2, b: Vec2) -> int:
    return abs(a.x - b.x) + abs(a.y - b.y)
