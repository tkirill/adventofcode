from __future__ import annotations
from dataclasses import dataclass
import dataclasses
from collections.abc import Sequence, Iterable
from typing import Tuple, Optional, Callable
import itertools

from aoc.primitives import Vec2, Rectangle
from aoc import algo


@dataclass
class Grid2d:

    delta_right: Vec2 = Vec2(1, 0)
    delta_up: Vec2 = Vec2(0, -1)
    delta_left: Vec2 = dataclasses.field(init=False)
    delta_down: Vec2 = dataclasses.field(init=False)

    def __post_init__(self):
        self.delta_left = -self.delta_right
        self.delta_down = - self.delta_up

    def up(self, p: Vec2, d: int=1) -> Vec2:
        return p + self.delta_up * d
    
    def down(self, p: Vec2, d: int=1) -> Vec2:
        return p - self.delta_up * d
    
    def left(self, p: Vec2, d: int=1) -> Vec2:
        return p - self.delta_right * d
    
    def right(self, p: Vec2, d: int=1) -> Vec2:
        return p + self.delta_right * d
    
    def up_left(self, p: Vec2, d_up: int=1, d_left: int=1) -> Vec2:
        return self.left(self.up(p, d_up), d_left)
    
    def up_right(self, p: Vec2, d_up: int=1, d_left: int=1) -> Vec2:
        return self.right(self.up(p, d_up), d_left)
    
    def down_left(self, p: Vec2, d_up: int=1, d_left: int=1) -> Vec2:
        return self.left(self.down(p, d_up), d_left)
    
    def down_right(self, p: Vec2, d_up: int=1, d_left: int=1) -> Vec2:
        return self.right(self.down(p, d_up), d_left)
    
    def step(self, p: Vec2, dir: str, dist: int=1) -> Vec2:
        match(dir):
            case 'L' | 'W': return self.left(p, dist)
            case 'R' | 'E': return self.right(p, dist)
            case 'U' | 'N': return self.up(p, dist)
            case 'D' | 'S': return self.down(p, dist)
    
    def beam_up(self, p: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
        return p.beam(self.delta_up, skip_start)
    
    def beam_up_left(self, p: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
        return p.beam(self.delta_up + self.delta_left, skip_start)
    
    def beam_up_right(self, p: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
        return p.beam(self.delta_up + self.delta_right, skip_start)
    
    def beam_down(self, p: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
        return p.beam(self.delta_down, skip_start)
    
    def beam_down_left(self, p: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
        return p.beam(self.delta_down + self.delta_left, skip_start)
    
    def beam_down_right(self, p: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
        return p.beam(self.delta_down + self.delta_right, skip_start)
    
    def beam_left(self, p: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
        return p.beam(self.delta_left, skip_start)
    
    def beam_right(self, p: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
        return p.beam(self.delta_right, skip_start)
    
    def range_up(self, p: Vec2, l: int) -> Iterable[Vec2]:
        return itertools.islice(self.beam_up(p), l)
    
    def range_down(self, p: Vec2, l: int) -> Iterable[Vec2]:
        return itertools.islice(self.beam_down(p), l)
    
    def range_left(self, p: Vec2, l: int) -> Iterable[Vec2]:
        return itertools.islice(self.beam_left(p), l)
    
    def range_right(self, p: Vec2, l: int) -> Iterable[Vec2]:
        return itertools.islice(self.beam_right(p), l)
    
    def near4(self, p: Vec2) -> Iterable[Vec2]:
        yield self.up(p)
        yield self.right(p)
        yield self.down(p)
        yield self.left(p)
    
    def near8(self, p: Vec2) -> Iterable[Vec2]:
        yield self.up_left(p)
        yield self.up(p)
        yield self.up_right(p)
        yield self.right(p)
        yield self.down_right(p)
        yield self.down(p)
        yield self.down_left(p)
        yield self.left(p)
    
    def beam4(self, p: Vec2, skip_start: bool=False) -> Iterable[Iterable[Vec2]]:
        yield self.beam_up(p, skip_start)
        yield self.beam_right(p, skip_start)
        yield self.beam_down(p, skip_start)
        yield self.beam_left(p, skip_start)
    
    def beam8(self, p: Vec2, skip_start: bool=False) -> Iterable[Iterable[Vec2]]:
        yield self.beam_up_left(p, skip_start)
        yield self.beam_up(p, skip_start)
        yield self.beam_up_right(p, skip_start)
        yield self.beam_right(p, skip_start)
        yield self.beam_down_right(p, skip_start)
        yield self.beam_down(p, skip_start)
        yield self.beam_down_left(p, skip_start)
        yield self.beam_left(p, skip_start)
    
    def near8_rectangle(self, r: Rectangle) -> Iterable[Vec2]:
        cur = self.up_left(r.top_left)
        yield cur
        for _ in range(r.w+1):
            cur = self.right(cur)
            yield cur
        for _ in range(r.h+1):
            cur = self.down(cur)
            yield cur
        for _ in range(r.w+1):
            cur = self.left(cur)
            yield cur
        for _ in range(r.h):
            cur = self.up(cur)
            yield cur
    
    def rotatelr(self, p: Vec2, dir: str) -> Vec2:
        if dir == 'R':
            return Vec2(p.y * self.delta_up.y, p.x * -self.delta_up.y)
        return Vec2(p.y * -self.delta_up.y, p.x * self.delta_up.y)


screen = Grid2d()


@dataclass(frozen=True)
class GridWalker:
    pos: Vec2 = Vec2(0, 0)
    velocity: Vec2 = None
    grid: Grid2d = dataclasses.field(default_factory=lambda: screen, compare=False)

    def __post_init__(self):
        if self.velocity is None:
            self.velocity = self.grid.delta_up
    
    def step(self) -> GridWalker:
        return dataclasses.replace(self, pos=self.pos + self.velocity)
    
    def rotatelr(self, dir: str) -> GridWalker:
        return GridWalker(self.pos, self.grid.rotatelr(self.velocity, dir))


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
        return self.takewhile_inside(start.beam_to(other, skip_start=skip_start, skip_other=skip_other))
    
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
        return self.inside(self.grid.near4(pos))
    
    def near4v(self, pos: Vec2) -> Iterable[Vec2]:
        return self.with_values(self.near4(pos))
    
    def near8(self, pos: Vec2) -> Iterable[Vec2]:
        return self.inside(self.grid.near8(pos))
    
    def near8v(self, pos: Vec2) -> Iterable[Vec2]:
        return self.with_values(self.near8(pos))
    
    def beam4(self, pos: Vec2, skip_start: bool=False) -> Iterable[Iterable[Vec2]]:
        for beam in self.grid.beam4(pos, skip_start):
            yield self.takewhile_inside(beam)
    
    def beam4v(self, pos: Vec2, skip_start: bool=False) -> Iterable[Iterable[Tuple[Vec2, TValue]]]:
        for beam in self.beam4(pos, skip_start):
            yield self.with_values(beam)
    
    def beam8(self, pos: Vec2, skip_start: bool=False) -> Iterable[Iterable[Vec2]]:
        for beam in self.grid.beam8(pos, skip_start):
            yield self.takewhile_inside(beam)
    
    def beam8v(self, pos: Vec2, skip_start: bool=False) -> Iterable[Iterable[Tuple[Vec2, TValue]]]:
        for beam in self.beam8(pos, skip_start):
            yield self.with_values(beam)
    
    def bfs4(self, start: Vec2, nfilter: Optional[Callable[[Vec2, Vec2], bool]]=None, track_visited: bool=True) -> Iterable[tuple[Vec2, int]]:
        def nearfunc(cur):
            return filter(lambda n: nfilter(cur, n), self.near4(cur))
        near = self.near4 if nfilter is None else nearfunc
        yield from algo.bfs(start, near, track_visited=track_visited)
