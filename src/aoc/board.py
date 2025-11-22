from dataclasses import dataclass, field
from typing import Iterable, Optional

from aoc.vec2 import Vec2
from aoc.rectangle import Rectangle
from aoc import grid


@dataclass
class Board[TValue]:

    values: list[list[TValue]]
    width: int = field(init=False)
    height: int = field(init=False)

    def __post_init__(self):
        self.height = len(self.values)
        self.width = len(self.values[0]) if self.values else 0

    def __contains__(self, item: Vec2) -> bool:
        return 0 <= item.x < self.width and 0 <= item.y < self.height
    
    def __getitem__(self, key: Vec2) -> TValue:
        return self.values[key.y][key.x]


def near8[TValue](b: Board[TValue], p: Vec2 | Rectangle) -> Iterable[Vec2]:
    return filter(b.__contains__, grid.near8(p))


def near8v[TValue](b: Board[TValue], p: Vec2 | Rectangle) -> Iterable[tuple[Vec2, TValue]]:
    for p in near8(b, p):
        yield p, b[p]


def with_value[TValue](b: Board[TValue], positions: Iterable[Vec2]) -> Iterable[tuple[Vec2, TValue]]:
    for p in positions:
        yield p, b[p]


def cells[TValue](b: Board[TValue]) -> Iterable[Vec2]:
    for row in range(b.height):
        for col in range(b.width):
            yield Vec2(col, row)


def cellsv[TValue](b: Board[TValue]) -> Iterable[tuple[Vec2, TValue]]:
    yield from with_value(b, cells(b))


def find[TValue](b: Board[TValue], value: TValue) -> Optional[TValue]:
    return next((p for p, v in cellsv(b) if v == value), None)


def rows[TValue](b: Board[TValue]) -> Iterable[Iterable[Vec2]]:
    for row in range(b.height):
        yield (Vec2(col, row) for col in range(b.width))


def rowsv[TValue](b: Board[TValue]) -> Iterable[Iterable[tuple[Vec2, TValue]]]:
    for row in rows(b):
        yield with_value(b, row)


def cols[TValue](b: Board[TValue]) -> Iterable[Iterable[Vec2]]:
    for col in range(b.width):
        yield (Vec2(col, row) for row in range(b.height))


def colsv[TValue](b: Board[TValue]) -> Iterable[Iterable[tuple[Vec2, TValue]]]:
    for col in cols(b):
        yield with_value(b, col)


def itranspose[TValue](b: Board[TValue]) -> Iterable[Iterable[TValue]]:
    for col in range(b.width):
        yield (b.values[row][col] for row in range(b.height))


def transpose[TValue](b: Board[TValue]) -> Board[TValue]:
    return Board([list(c) for c in itranspose(b)])
