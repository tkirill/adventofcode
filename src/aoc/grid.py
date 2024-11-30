from __future__ import annotations
from dataclasses import dataclass, field
from collections.abc import Sequence, Iterable
from typing import Tuple
import itertools

from aoc.primitives import Vec2, Rectangle
from aoc.algo import transpose


@dataclass
class Grid2d:

    delta_right: Vec2 = Vec2(1, 0)
    delta_up: Vec2 = Vec2(0, -1)

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
    
    def step(self, p: Vec2, dir: str, dist: int=1) -> Vec2:
        match(dir):
            case 'L' | 'W': return self.left(p, dist)
            case 'R' | 'E': return self.right(p, dist)
            case 'U' | 'N': return self.up(p, dist)
            case 'D' | 'S': return self.down(p, dist)
    
    def beam_up(self, p: Vec2, emit_start: bool=True) -> Iterable[Vec2]:
        if emit_start:
            yield p
        while True:
            p = self.up(p)
            yield p
    
    def beam_down(self, p: Vec2, emit_start: bool=True) -> Iterable[Vec2]:
        if emit_start:
            yield p
        while True:
            p = self.down(p)
            yield p
    
    def beam_left(self, p: Vec2, emit_start: bool=True) -> Iterable[Vec2]:
        if emit_start:
            yield p
        while True:
            p = self.left(p)
            yield p
    
    def beam_right(self, p: Vec2, emit_start: bool=True) -> Iterable[Vec2]:
        if emit_start:
            yield p
        while True:
            p = self.right(p)
            yield p
    
    def range_up(self, p: Vec2, l: int) -> Iterable[Vec2]:
        return itertools.islice(self.beam_up(p), l)
    
    def range_down(self, p: Vec2, l: int) -> Iterable[Vec2]:
        return itertools.islice(self.beam_down(p), l)
    
    def range_left(self, p: Vec2, l: int) -> Iterable[Vec2]:
        return itertools.islice(self.beam_left(p), l)
    
    def range_right(self, p: Vec2, l: int) -> Iterable[Vec2]:
        return itertools.islice(self.beam_right(p), l)
    
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


screen = Grid2d()


@dataclass
class Field[TValue]:
    items: list[Sequence[TValue]]
    w: int = field(init=False)
    h: int = field(init=False)

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
        return Field(transpose(self.items))
    
    def beam_up(self, pos: Vec2, emit_start: bool=True, grid: Grid2d=screen) -> Iterable[Vec2]:
        return self.takewhile_inside(grid.beam_up(pos, emit_start))
    
    def beam_down(self, pos: Vec2, emit_start: bool=True, grid: Grid2d=screen) -> Iterable[Vec2]:
        return self.takewhile_inside(grid.beam_down(pos, emit_start))
    
    def beam_left(self, pos: Vec2, emit_start: bool=True, grid: Grid2d=screen) -> Iterable[Vec2]:
        return self.takewhile_inside(grid.beam_left(pos, emit_start))
    
    def beam_right(self, pos: Vec2, emit_start: bool=True, grid: Grid2d=screen) -> Iterable[Vec2]:
        return self.takewhile_inside(grid.beam_right(pos, emit_start))
    
    def beam_upv(self, pos: Vec2, emit_start: bool=True, grid: Grid2d=screen) -> Iterable[Tuple[Vec2, TValue]]:
        return self.with_values(self.beam_up(pos, emit_start, grid))
    
    def beam_downv(self, pos: Vec2, emit_start: bool=True, grid: Grid2d=screen) -> Iterable[Tuple[Vec2, TValue]]:
        return self.with_values(self.beam_down(pos, emit_start, grid))
    
    def beam_leftv(self, pos: Vec2, emit_start: bool=True, grid: Grid2d=screen) -> Iterable[Tuple[Vec2, TValue]]:
        return self.with_values(self.beam_left(pos, emit_start, grid))
    
    def beam_rightv(self, pos: Vec2, emit_start: bool=True, grid: Grid2d=screen) -> Iterable[Tuple[Vec2, TValue]]:
        return self.with_values(self.beam_right(pos, emit_start, grid))