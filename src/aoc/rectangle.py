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
    
    @classmethod
    def by_corners(cls, u: Vec2, v: Vec2) -> Rectangle:
        min_x, min_y = min(u.x, v.x), min(u.y, v.y)
        max_x, max_y = max(u.x, v.x), max(u.y, v.y)
        return Rectangle(Vec2(min_x, min_y), max_x-min_x, max_y-min_y)