from __future__ import annotations
from dataclasses import dataclass
import dataclasses
from collections.abc import Sequence, Iterable
from typing import Tuple, Optional, Callable
import itertools

from aoc.primitives import Vec2, Rectangle, Grid2d
from aoc import algo, vec2


def up(g: Grid2d, p: Vec2, d: int=1) -> Vec2:
        return p + g.delta_up * d
    
def down(g: Grid2d, p: Vec2, d: int=1) -> Vec2:
    return p - g.delta_up * d

def left(g: Grid2d, p: Vec2, d: int=1) -> Vec2:
    return p - g.delta_right * d

def right(g: Grid2d, p: Vec2, d: int=1) -> Vec2:
    return p + g.delta_right * d


def up_left(g: Grid2d, p: Vec2, d_up: int=1, d_left: int=1) -> Vec2:
    return left(g, up(g, p, d_up), d_left)

def up_right(g: Grid2d, p: Vec2, d_up: int=1, d_left: int=1) -> Vec2:
    return right(g, up(g, p, d_up), d_left)

def down_left(g: Grid2d, p: Vec2, d_up: int=1, d_left: int=1) -> Vec2:
    return left(g, down(g, p, d_up), d_left)

def down_right(g: Grid2d, p: Vec2, d_up: int=1, d_left: int=1) -> Vec2:
    return right(g, down(g, p, d_up), d_left)

def step(g: Grid2d, p: Vec2, dir: str, dist: int=1) -> Vec2:
    match(dir):
        case 'L' | 'W' | '<': return left(g, p, dist)
        case 'R' | 'E' | '>': return right(g, p, dist)
        case 'U' | 'N' | '^': return up(g, p, dist)
        case 'D' | 'S' | 'v': return down(g, p, dist)

def beam_up(g: Grid2d, p: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
    return vec2.beam(p, g.delta_up, skip_start)

def beam_up_left(g: Grid2d, p: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
    return vec2.beam(p, g.delta_up + g.delta_left, skip_start)

def beam_up_right(g: Grid2d, p: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
    return vec2.beam(p, g.delta_up + g.delta_right, skip_start)

def beam_down(g: Grid2d, p: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
    return vec2.beam(p, g.delta_down, skip_start)

def beam_down_left(g: Grid2d, p: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
    return vec2.beam(p, g.delta_down + g.delta_left, skip_start)

def beam_down_right(g: Grid2d, p: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
    return vec2.beam(p, g.delta_down + g.delta_right, skip_start)

def beam_left(g: Grid2d, p: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
    return vec2.beam(p, g.delta_left, skip_start)

def beam_right(g: Grid2d, p: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
    return vec2.beam(p, g.delta_right, skip_start)

def range_up(g: Grid2d, p: Vec2, l: int) -> Iterable[Vec2]:
    return itertools.islice(beam_up(g, p), l)

def range_down(g: Grid2d, p: Vec2, l: int) -> Iterable[Vec2]:
    return itertools.islice(beam_down(g, p), l)

def range_left(g: Grid2d, p: Vec2, l: int) -> Iterable[Vec2]:
    return itertools.islice(beam_left(g, p), l)

def range_right(g: Grid2d, p: Vec2, l: int) -> Iterable[Vec2]:
    return itertools.islice(beam_right(g, p), l)

def near4(g: Grid2d, p: Vec2) -> Iterable[Vec2]:
    yield up(g, p)
    yield right(g, p)
    yield down(g, p)
    yield left(g, p)

def near8(g: Grid2d, p: Vec2) -> Iterable[Vec2]:
    yield up_left(g, p)
    yield up(g, p)
    yield up_right(g, p)
    yield right(g, p)
    yield down_right(g, p)
    yield down(g, p)
    yield down_left(g, p)
    yield left(g, p)

def beam4(g: Grid2d, p: Vec2, skip_start: bool=False) -> Iterable[Iterable[Vec2]]:
    yield beam_up(g, p, skip_start)
    yield beam_right(g, p, skip_start)
    yield beam_down(g, p, skip_start)
    yield beam_left(g, p, skip_start)

def beam8(g: Grid2d, p: Vec2, skip_start: bool=False) -> Iterable[Iterable[Vec2]]:
    yield beam_up_left(g, p, skip_start)
    yield beam_up(g, p, skip_start)
    yield beam_up_right(g, p, skip_start)
    yield beam_right(g, p, skip_start)
    yield beam_down_right(g, p, skip_start)
    yield beam_down(g, p, skip_start)
    yield beam_down_left(g, p, skip_start)
    yield beam_left(g, p, skip_start)

def near8_rectangle(g: Grid2d, r: Rectangle) -> Iterable[Vec2]:
    cur = up_left(g, r.top_left)
    yield cur
    for _ in range(r.w+1):
        cur = right(g, cur)
        yield cur
    for _ in range(r.h+1):
        cur = down(g, cur)
        yield cur
    for _ in range(r.w+1):
        cur = left(g, cur)
        yield cur
    for _ in range(r.h):
        cur = up(g, cur)
        yield cur

def rotatelr(g: Grid2d, p: Vec2, dir: str) -> Vec2:
    if dir == 'R':
        return Vec2(p.y * g.delta_up.y, p.x * -g.delta_up.y)
    return Vec2(p.y * -g.delta_up.y, p.x * g.delta_up.y)

def side_up(g: Grid2d, p: Vec2) -> Iterable[Vec2]:
    yield up_left(g, p)
    yield up(g, p)
    yield up_right(g, p)

def side_right(g: Grid2d, p: Vec2) -> Iterable[Vec2]:
    yield up_right(g, p)
    yield right(g, p)
    yield down_right(g, p)

def side_down(g: Grid2d, p: Vec2) -> Iterable[Vec2]:
    yield down_left(g, p)
    yield down(g, p)
    yield down_right(g, p)

def side_left(g: Grid2d, p: Vec2) -> Iterable[Vec2]:
    yield down_left(g, p)
    yield left(g, p)
    yield up_left(g, p)

def side(g: Grid2d, p: Vec2, side: str) -> Iterable[Vec2]:
    match side:
        case 'U' | 'N': return side_up(g, p)
        case 'R' | 'E': return side_right(g, p)
        case 'D' | 'S': return side_down(g, p)
        case 'L' | 'W': return side_left(g, p)


screen = Grid2d()
traditional = Grid2d(delta_up=Vec2(0, 1))


@dataclass(frozen=True)
class GridWalker:
    pos: Vec2 = Vec2(0, 0)
    velocity: Vec2 = dataclasses.field(default_factory=lambda: screen.delta_up)
    grid: Grid2d = dataclasses.field(default_factory=lambda: screen, compare=False)

    def step(self) -> GridWalker:
        return dataclasses.replace(self, pos=self.pos + self.velocity)
    
    def mod_by(self, w: int, h: int) -> GridWalker:
        if 0 <= self.pos.x < w and 0 <= self.pos.y < h:
            return self
        return dataclasses.replace(self, pos=Vec2((self.pos.x + w) % w, (self.pos.y + h) % h))
    
    def rotatelr(self, dir: str) -> GridWalker:
        return GridWalker(self.pos, rotatelr(self.grid, self.velocity, dir))


@dataclass
class Field[TValue]:
    items: list[Sequence[TValue]]
    grid: Grid2d = dataclasses.field(default_factory=lambda: screen)
    w: int = dataclasses.field(init=False)
    h: int = dataclasses.field(init=False)

    def __post_init__(self):
        self.w = len(self.items[0])
        self.h = len(self.items)
    
    def __getitem__(self, key: Vec2) -> TValue:
        return self.items[key.y][key.x]
    
    def __setitem__(self, key: Vec2, value: TValue):
        self.items[key.y][key.x] = value
    
    def __contains__(self, key: Vec2) -> bool:
        return 0 <= key.y < self.h and 0 <= key.x < self.w

    def is_inside(self, pos: Vec2) -> bool:
        return pos in self

    def inside(self, positions: Iterable[Vec2]) -> Iterable[Vec2]:
        return filter(self.__contains__, positions)

    def insidev(self, positions: Iterable[Vec2]) -> Iterable[Tuple[Vec2, TValue]]:
        for p in self.inside(positions):
            yield p, self.items[p.y][p.x]
    
    def takewhile_inside(self, positions: Iterable[Vec2]) -> Iterable[Vec2]:
        return itertools.takewhile(self.__contains__, positions)
    
    def with_values(self, positions: Iterable[Vec2]) -> Iterable[Tuple[Vec2, TValue]]:
        for p in positions:
            yield p, self[p]
    
    def row(self, r: int) -> Iterable[Vec2]:
        for c in range(self.w):
            yield Vec2(c, r)
    
    def rowv(self, r: int) -> Iterable[Tuple[Vec2, TValue]]:
        return self.with_values(self.row(r))
    
    def rows(self) -> Iterable[Iterable[Vec2]]:
        for r in range(self.h):
            yield self.row(r)
    
    def rowsv(self) -> Iterable[Iterable[Tuple[Vec2, TValue]]]:
        for r in range(self.h):
            yield self.rowv(r)
    
    def column(self, c: int) -> Iterable[Vec2]:
        for r in range(self.h):
            yield Vec2(c, r)
    
    def columnv(self, c: int) -> Iterable[Tuple[Vec2, TValue]]:
        return self.with_values(self.column(c))
    
    def columns(self) -> Iterable[Iterable[Vec2]]:
        for c in range(self.w):
            yield self.column(c)
    
    def columnsv(self) -> Iterable[Iterable[Tuple[Vec2, TValue]]]:
        for c in range(self.w):
            yield self.columnv(c)
    
    def cells(self) -> Iterable[Vec2]:
        for r in range(self.h):
            for c in range(self.w):
                yield Vec2(c, r)
    
    def cellsv(self) -> Iterable[Tuple[Vec2, TValue]]:
        return self.with_values(self.cells())
    
    def transpose(self) -> Field[TValue]:
        return Field(algo.transpose(self.items))
    
    def beam_to(self, start: Vec2, other: Vec2, skip_start: bool=False, skip_other: bool=False) -> Iterable[Vec2]:
        return self.takewhile_inside(vec2.beam_to(start, other, skip_start=skip_start, skip_other=skip_other))
    
    def beam_up(self, pos: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
        return self.takewhile_inside(self.grid.beam_up(pos, skip_start))
    
    def beam_up_left(self, pos: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
        return self.takewhile_inside(self.grid.beam_up_left(pos, skip_start))
    
    def beam_up_right(self, pos: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
        return self.takewhile_inside(self.grid.beam_up_right(pos, skip_start))
    
    def beam_down(self, pos: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
        return self.takewhile_inside(self.grid.beam_down(pos, skip_start))
    
    def beam_down_left(self, pos: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
        return self.takewhile_inside(self.grid.beam_down_left(pos, skip_start))
    
    def beam_down_right(self, pos: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
        return self.takewhile_inside(self.grid.beam_down_right(pos, skip_start))
    
    def beam_left(self, pos: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
        return self.takewhile_inside(self.grid.beam_left(pos, skip_start))
    
    def beam_right(self, pos: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
        return self.takewhile_inside(self.grid.beam_right(pos, skip_start))
    
    def beam_upv(self, pos: Vec2, skip_start: bool=False) -> Iterable[Tuple[Vec2, TValue]]:
        return self.with_values(self.beam_up(pos, skip_start))
    
    def beam_up_leftv(self, pos: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
        return self.with_values(self.beam_up_left(pos, skip_start))
    
    def beam_up_rightv(self, pos: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
        return self.with_values(self.beam_up_right(pos, skip_start))
    
    def beam_downv(self, pos: Vec2, skip_start: bool=False) -> Iterable[Tuple[Vec2, TValue]]:
        return self.with_values(self.beam_down(pos, skip_start))
    
    def beam_down_leftv(self, pos: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
        return self.with_values(self.beam_down_left(pos, skip_start))
    
    def beam_down_rightv(self, pos: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
        return self.with_values(self.beam_down_right(pos, skip_start))
    
    def beam_leftv(self, pos: Vec2, skip_start: bool=False) -> Iterable[Tuple[Vec2, TValue]]:
        return self.with_values(self.beam_left(pos, skip_start))
    
    def beam_rightv(self, pos: Vec2, skip_start: bool=False) -> Iterable[Tuple[Vec2, TValue]]:
        return self.with_values(self.beam_right(pos, skip_start))
    
    def near4(self, pos: Vec2) -> Iterable[Vec2]:
        return self.inside(near4(self.grid, pos))
    
    def near4v(self, pos: Vec2) -> Iterable[tuple[Vec2, TValue]]:
        return self.with_values(self.near4(pos))
    
    def near8(self, pos: Vec2) -> Iterable[Vec2]:
        return self.inside(near8(self.grid, pos))
    
    def near8v(self, pos: Vec2) -> Iterable[Vec2]:
        return self.with_values(self.near8(pos))
    
    def beam4(self, pos: Vec2, skip_start: bool=False) -> Iterable[Iterable[Vec2]]:
        for beam in beam4(self.grid, pos, skip_start):
            yield self.takewhile_inside(beam)
    
    def beam4v(self, pos: Vec2, skip_start: bool=False) -> Iterable[Iterable[Tuple[Vec2, TValue]]]:
        for beam in self.beam4(pos, skip_start):
            yield self.with_values(beam)
    
    def beam8(self, pos: Vec2, skip_start: bool=False) -> Iterable[Iterable[Vec2]]:
        for beam in beam8(self.grid, pos, skip_start):
            yield self.takewhile_inside(beam)
    
    def beam8v(self, pos: Vec2, skip_start: bool=False) -> Iterable[Iterable[Tuple[Vec2, TValue]]]:
        for beam in self.beam8(pos, skip_start):
            yield self.with_values(beam)
    
    def bfs4(self, start: Vec2, nfilter: Optional[Callable[[Vec2, Vec2], bool]]=None, track_visited: bool=True) -> Iterable[tuple[Vec2, int]]:
        def nearfunc(cur):
            return filter(lambda n: nfilter(cur, n), self.near4(cur))
        near = self.near4 if nfilter is None else nearfunc
        yield from algo.bfs(start, near, track_visited=track_visited)
    
    def circle(self, pos: Vec2, r: int) -> Iterable[Vec2]:
        yield from self.inside(vec2.circle(pos, r))
    
    def circlev(self, pos: Vec2, r: int) -> Iterable[tuple[Vec2, TValue]]:
        yield from self.with_values(self.circle(pos, r))
