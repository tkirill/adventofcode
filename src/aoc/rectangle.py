from dataclasses import dataclass

from aoc.vec2 import Vec2


@dataclass(frozen=True)
class Rectangle:
    top_left: Vec2
    width: int
    height: int

    @property
    def xmin(self) -> int:
        return self.top_left.x
    
    @property
    def xmax(self) -> int:
        return self.top_left.x + self.width
    
    @property
    def ymin(self) -> int:
        return self.top_left.y
    
    @property
    def ymax(self) -> int:
        return self.top_left.y + self.height
    
    @property
    def top_right(self) -> Vec2:
        return Vec2(self.xmax, self.ymin)
    
    @property
    def bottom_left(self) -> Vec2:
        return Vec2(self.xmin, self.ymax)
    
    @property
    def bottom_right(self) -> Vec2:
        return Vec2(self.xmax, self.ymax)
    
    @property
    def mid(self) -> Vec2:
        return Vec2((self.xmin+self.xmax)//2, (self.ymin+self.ymax)//2)
    
    @property
    def square(self) -> int:
        return (self.xmax-self.xmin+1)*(self.ymax-self.ymin+1)

    @classmethod
    def ylr(cls, y: int, l: int, r: int) -> Rectangle:
        return Rectangle(Vec2(l, y), r-l+1, 1)
    
    @classmethod
    def by_corners(cls, u: Vec2, v: Vec2) -> Rectangle:
        min_x, min_y = min(u.x, v.x), min(u.y, v.y)
        max_x, max_y = max(u.x, v.x), max(u.y, v.y)
        return Rectangle(Vec2(min_x, min_y), max_x-min_x, max_y-min_y)