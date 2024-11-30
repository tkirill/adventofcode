from __future__ import annotations
from typing import NamedTuple
from dataclasses import dataclass
from collections.abc import Iterable


class Vec2(NamedTuple):

    x: int = 0
    y: int = 0

    def __add__(self, other: Vec2) -> Vec2:
        return Vec2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: Vec2) -> Vec2:
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, s: int) -> Vec2:
        return Vec2(self.x * s, self.y * s)
    
    def __neg__(self) -> Vec2:
        return Vec2(-self.x, -self.y)
    
    def increase(self, v: int) -> Vec2:
        return Vec2(self.x+v, self.y+v)
    
    def decrease(self, v: int) -> Vec2:
        return Vec2(self.x-v, self.y-v)
    
    def mdist(self, other: Vec2) -> int:
        return abs(self.x-other.x) + abs(self.y-other.y)


class Vec3(NamedTuple):

    x: int = 0
    y: int = 0
    z: int = 0

    def __add__(self, other: Vec3) -> Vec3:
        return Vec2(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other: Vec2) -> Vec3:
        return Vec2(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, s: int) -> Vec3:
        return Vec2(self.x * s, self.y * s, self.z * s)
    
    def __neg__(self) -> Vec3:
        return Vec3(-self.x, -self.y, -self.z)


@dataclass
class Rectangle:
    top_left: Vec2
    w: int
    h: int

    @classmethod
    def ylr(cls, y: int, l: int, r: int) -> Rectangle:
        return Rectangle(Vec2(l, y), r-l+1, 1)


@dataclass(frozen=True, order=True)
class Range:
    start: int
    end: int
    
    def intersect(self, other: Range) -> Range:
        return Range(max(self.start, other.start), min(self.end, other.end))
    
    def difference_many(self, others: Iterable[Range]) -> Iterable[Range]:
        cur = self.start
        for o in sorted(others):
            if o.start >= self.end:
                break
            if o.start > cur:
                yield Range(cur, o.start)
            cur = max(cur, o.end)
        if self.start <= cur < self.end:
            yield Range(cur, self.end)
    
    def shift(self, delta: int) -> Range:
        return Range(self.start + delta, self.end + delta)
    
    def __len__(self):
        return max(self.end - self.start + 1, 0)
    
    def __contains__(self, x: int) -> bool:
        return self.start <= x <= self.end

    @classmethod
    def lw(cls, l, w) -> Range:
        return Range(l, l+w)