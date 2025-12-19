from typing import Iterable, Optional
from itertools import islice, pairwise
import dataclasses

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


@dataclasses.dataclass(frozen=True)
class GridInterval:

    begin: Vec2
    end: Vec2

    def __post_init__(self):
        if gridpos(self.begin) > gridpos(self.end):
            tmp = self.begin
            object.__setattr__(self, 'begin', self.end)
            object.__setattr__(self, 'end', tmp)
    
    @property
    def is_vertical(self):
        return self.begin.x == self.end.x
    
    @property
    def is_horizontal(self):
        return self.begin.y == self.end.y
    
    def __contains__(self, other: Vec2) -> bool:
        if self.is_vertical:
            return self.begin.x == other.x and self.begin.y <= other.y <= self.end.y
        return self.begin.y == other.y and self.begin.x <= other.x <= self.end.x


def direction(s: str, d: int=1) -> Vec2:
    match s:
        case 'D':
            return DOWN * d
        case 'L':
            return LEFT * d
        case 'R':
            return RIGHT * d
        case 'U':
            return UP * d


def opposite(d: Vec2) -> Vec2:
    return OPPOSITE[d]


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
        yield from islice(beam(p, delta, skip_start=skip_start), n)
        return
    cur = p
    if not skip_start:
        yield cur
    while True:
        cur += delta
        yield cur


def mdist(a: Vec2, b: Vec2) -> int:
    return abs(a.x - b.x) + abs(a.y - b.y)


def turn(v: Vec2, d: str) -> Vec2:
    match d:
        case 'CW':
            return Vec2(-v.y, v.x)
        case 'CCW':
            return Vec2(v.y, -v.x)


def pick_theorem(edge: list[Vec2], include_edge: bool=True) -> int:
    b = 0
    # Shoelace formula: https://en.wikipedia.org/wiki/Shoelace_formula
    A = 0
    for cur, nxt in pairwise(edge):
        b += mdist(cur, nxt)
        A += (cur.y + nxt.y) * (cur.x - nxt.x)
    b += mdist(edge[-1], edge[0])
    A += (edge[-1].y + edge[0].y) * (edge[-1].x - edge[0].x)
    A //= 2
    # Pick's theorem: https://en.wikipedia.org/wiki/Pick%27s_theorem
    inside = A - b // 2 + 1
    if include_edge:
        inside += b
    return inside


def gridpos(a: Vec2):
    return (a.y, a.x)