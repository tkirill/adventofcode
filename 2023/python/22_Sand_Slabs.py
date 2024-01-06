from __future__ import annotations
from aoc import *
from dataclasses import dataclass


@dataclass
class Brick:
    start: Vec3
    end: Vec3
    bottom: int = field(init=False)
    top: int = field(init=False)
    left: int = field(init=False)
    right: int = field(init=False)
    forward: int = field(init=False)
    backward: int = field(init=False)

    def __post_init__(self):
        self.bottom = min(self.start.z, self.end.z)
        self.top = max(self.start.z, self.end.z)
        self.left = min(self.start.y, self.end.y)
        self.right = max(self.start.y, self.end.y)
        self.backward = min(self.start.x, self.end.x)
        self.forward = max(self.start.x, self.end.x)

    def fall(self) -> Brick:
        return Brick(self.start - Vec3(z=1), self.end - Vec3(z=1))

    def is_overlap_with(self, other: Brick) -> bool:
        return (
            self.bottom <= other.top
            and self.top >= other.bottom
            and self.left <= other.right
            and self.right >= other.left
            and self.backward <= other.forward
            and self.forward >= other.backward
        )

    @classmethod
    def from_coordinates(cls, x1, y1, z1, x2, y2, z2):
        return Brick(Vec3(x1, y1, z1), Vec3(x2, y2, z2))


def fall(bricks: list[Brick]) -> tuple[list[int], list[set[int]]]:
    new_bricks = []
    prev = []
    for cur in bricks:
        while cur.bottom != 1:
            nxt = cur.fall()
            under = [j for j, b in enumerate(new_bricks) if nxt.is_overlap_with(b)]
            if under:
                new_bricks.append(cur)
                prev.append(set(under))
                break
            cur = nxt
        else:
            new_bricks.append(cur)
            prev.append(set())
    return new_bricks, prev


def count_falls(prev: list[set[int]], start: int) -> int:
    fallen = set([start])
    changed = True
    while changed:
        changed = False
        for i, v in enumerate(prev):
            if i in fallen:
                continue
            if v and v <= fallen:
                fallen.add(i)
                changed = True
    return len(fallen) - 1


bricks = [Brick.from_coordinates(*x) for x in read(sep=",|~")]
bricks.sort(key=lambda b: b.bottom)
new_bricks, prev = fall(bricks)
important = [False] * len(new_bricks)
for v in prev:
    if len(v) == 1:
        important[list(v)[0]] = True
print("Star 1:", sum(1 for x in important if not x))
print("Star 2:", sum(count_falls(prev, i) for i in range(len(new_bricks))))
