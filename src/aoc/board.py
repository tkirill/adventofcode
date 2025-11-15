from dataclasses import dataclass, field
from typing import Iterable

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