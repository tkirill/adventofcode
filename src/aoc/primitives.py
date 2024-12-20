from __future__ import annotations
from typing import NamedTuple, Optional
from dataclasses import dataclass
from collections.abc import Iterable
import math


def sign(x: int) -> bool:
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


@dataclass(frozen=True)
class Vec2:

    x: int = 0
    y: int = 0

    def __add__(self, other: Vec2) -> Vec2:
        return Vec2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: Vec2) -> Vec2:
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, s: int) -> Vec2:
        return Vec2(self.x * s, self.y * s)
    
    def __rmul__(self, s: int) -> Vec2:
        return Vec2(self.x * s, self.y * s)
    
    def __neg__(self) -> Vec2:
        return Vec2(-self.x, -self.y)
    
    def __abs__(self) -> Vec2:
        return Vec2(abs(self.x), abs(self.y))
    
    def increase(self, v: int) -> Vec2:
        return Vec2(self.x+v, self.y+v)
    
    def decrease(self, v: int) -> Vec2:
        return Vec2(self.x-v, self.y-v)
    
    def mod_by(self, other: Vec2) -> Vec2:
        return Vec2(self.x % other.x, self.y % other.y)
    
    def mdist(self, other: Vec2) -> int:
        return abs(self.x-other.x) + abs(self.y-other.y)
    
    def cdist(self, other: Optional[Vec2]=None) -> int:
        if other is None:
            other = Vec2()
        return max(abs(self.x-other.x), abs(self.y-other.y))
    
    def sign(self) -> Vec2:
        return Vec2(sign(self.x), sign(self.y))
    
    def beam(self, delta: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
        cur = self
        if not skip_start:
            yield cur
        while True:
            cur = cur + delta
            yield cur
    
    def beam_to(self, other: Vec2, skip_start: bool=False, skip_other: bool=False) -> Iterable[Vec2]:
        delta = (other - self).normalize()
        for cur in self.beam(delta, skip_start=skip_start):
            if not skip_other or cur != other:
                yield cur
    
    def range_to(self, other: Vec2, skip_start: bool=False, skip_other: bool=False) -> Iterable[Vec2]:
        delta = (other - self).normalize()
        for cur in self.beam(delta, skip_start=skip_start):
            if not skip_other or cur != other:
                yield cur
            if cur == other:
                break
    
    def normalize(self) -> Vec2:
        g = math.gcd(abs(self.x), abs(self.y))
        return Vec2(self.x // g, self.y // g)
    
    def circle(self, r: int, emit_center: bool=True) -> Iterable[Vec2]:
        for dx in range(-r, r+1):
            for dy in range(abs(dx)-r, r-abs(dx)+1):
                yield Vec2(self.x + dx, self.y + dy)


class Vec3(NamedTuple):

    x: int = 0
    y: int = 0
    z: int = 0

    def __add__(self, other: Vec3) -> Vec3:
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other: Vec3) -> Vec3:
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, s: int) -> Vec3:
        return Vec3(self.x * s, self.y * s, self.z * s)
    
    def __neg__(self) -> Vec3:
        return Vec3(-self.x, -self.y, -self.z)
    
    def up(self):
        return Vec3(self.x, self.y-1, self.z)
    
    def down(self):
        return Vec3(self.x, self.y+1, self.z)
    
    def left(self):
        return Vec3(self.x-1, self.y, self.z)
    
    def right(self):
        return Vec3(self.x+1, self.y, self.z)
    
    def forward(self):
        return Vec3(self.x, self.y, self.z+1)
    
    def backward(self):
        return Vec3(self.x, self.y, self.z-1)
    
    def near6(self):
        yield self.up()
        yield self.down()
        yield self.left()
        yield self.right()
        yield self.forward()
        yield self.backward()


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