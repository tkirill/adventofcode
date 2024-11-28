from __future__ import annotations
from typing import NamedTuple


class Vec2(NamedTuple):

    x: int = 0
    y: int = 0

    def __add__(self, other: Vec2) -> Vec2:
        return Vec2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: Vec2) -> Vec2:
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, s: int) -> Vec2:
        return Vec2(self.x * s, self.y * s)
    
    def __neg__(self) -> Vec3:
        return Vec2(-self.x, -self.y)


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
