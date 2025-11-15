from dataclasses import dataclass


@dataclass(frozen=True)
class Vec2:

    x: int = 0
    y: int = 0

    def __add__(self, other: Vec2 | int) -> Vec2:
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y)
        return Vec2(self.x + other, self.y + other)
    
    def __sub__(self, other: Vec2 | int) -> Vec2:
        if isinstance(other, Vec2):
            return Vec2(self.x - other.x, self.y - other.y)
        return Vec2(self.x - other, self.y - other)

    def __mul__(self, s: int) -> Vec2:
        return Vec2(self.x * s, self.y * s)
    
    def __rmul__(self, s: int) -> Vec2:
        return Vec2(self.x * s, self.y * s)
    
    def __neg__(self) -> Vec2:
        return Vec2(-self.x, -self.y)
    
    def __abs__(self) -> Vec2:
        return Vec2(abs(self.x), abs(self.y))
    
    def __mod__(self, other: Vec2 | int) -> Vec2:
        if isinstance(other, Vec2):
            return Vec2(self.x % other.x, self.y % other.y)
        return Vec2(self.x % other, self.y % other)
