from __future__ import annotations
from dataclasses import dataclass
from typing import NamedTuple


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
    
    def __mod__(self, other: Vec2) -> Vec2:
        return Vec2(self.x % other.x, self.y % other.y)
    
    def add_scalar(self, v: int) -> Vec2:
        return Vec2(self.x+v, self.y+v)
    
    def sub_scalar(self, v: int) -> Vec2:
        return Vec2(self.x-v, self.y-v)
    
    def mod_scalar(self, v: int) -> Vec2:
        return Vec2(self.x % v, self.y % v)


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


@dataclass(frozen=True, order=True)
class Range:

    start: int
    end: int
       
    def __len__(self):
        return max(self.end - self.start + 1, 0)
    
    def __contains__(self, x: int) -> bool:
        return self.start <= x <= self.end

    @classmethod
    def lw(cls, l, w) -> Range:
        return Range(l, l+w)


@dataclass
class Rectangle:
    top_left: Vec2
    w: int
    h: int

    @classmethod
    def ylr(cls, y: int, l: int, r: int) -> Rectangle:
        return Rectangle(Vec2(l, y), r-l+1, 1)


def sign(x: int) -> bool:
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0