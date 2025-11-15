from dataclasses import dataclass

from aoc.vec2 import Vec2


@dataclass(frozen=True)
class Rectangle:
    top_left: Vec2
    width: int
    height: int

    @classmethod
    def ylr(cls, y: int, l: int, r: int) -> Rectangle:
        return Rectangle(Vec2(l, y), r-l+1, 1)