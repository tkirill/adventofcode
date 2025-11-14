from __future__ import annotations
from typing import Optional
from collections.abc import Iterable
import math

from aoc.primitives import Vec2
import aoc.primitives


def mdist(first: Vec2, second: Vec2) -> int:
    return abs(first.x-second.x) + abs(first.y-second.y)


def cdist(first: Vec2, second: Optional[Vec2]=None) -> int:
    if second is None:
        second = Vec2()
    return max(abs(first.x-second.x), abs(first.y-second.y))


def sign(v: Vec2) -> Vec2:
    return Vec2(aoc.primitives.sign(v.x), aoc.primitives.sign(v.y))


def beam(start: Vec2, delta: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
    cur = start
    if not skip_start:
        yield cur
    while True:
        cur = cur + delta
        yield cur


def beam_to(start: Vec2, other: Vec2, skip_start: bool=False, skip_other: bool=False) -> Iterable[Vec2]:
    delta = normalize(other - start)
    for cur in beam(start, delta, skip_start=skip_start):
        if not skip_other or cur != other:
            yield cur


def range_to(start: Vec2, other: Vec2, skip_start: bool=False, skip_other: bool=False) -> Iterable[Vec2]:
    delta = normalize(other - start)
    for cur in beam(start, delta, skip_start=skip_start):
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
            if emit_center or dx and dy:
                yield Vec2(self.x + dx, self.y + dy)