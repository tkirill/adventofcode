from __future__ import annotations
from aoc.io import *
from aoc.primitives import *


ROW = 2000000
LIMIT = 4000000


def read_input():
    data = []
    for sx, sy, bx, by in read(sep=None, parse=allints):
        data.append((Vec2(sx, sy), Vec2(bx, by)))
    return data


def exclude_single(s: Vec2, b: Vec2, y: int) -> tuple[int, int]:
    dx = s.mdist(b) - abs(s.y - y)
    return (s.x-dx, s.x+dx) if dx >= 0 else None


def merge_all(data: list[tuple[Vec2, Vec2]], y: int) -> Iterable[tuple[int, int]]:
    intervals = sorted(filter(None, (exclude_single(s, b, y) for s, b in data)))
    cur = list(intervals[0])
    for l, r in intervals[1:]:
        if l > cur[1]:
            yield cur
            cur = [l, r]
        elif r > cur[1]:
            cur[1] = r
    yield cur


def try_find_beacon(data: list[tuple[Vec2, Vec2]], y: int, limit: int) -> Optional[Vec2]:
    intervals = sorted(filter(None, (exclude_single(s, b, y) for s, b in data)))
    
    cur = [0, limit]
    for l, r in intervals:
        if r < cur[0] or l > cur[1]:
            continue
        if l > cur[0]:
            return Vec2(l-1, y)
        cur[0] = r + 1
        if cur[0] > cur[1]:
            break


data = read_input()
tmp = sum(r-l+1 for l, r in merge_all(data, ROW)) - len(set(b for s, b in data if b.y == ROW))
print('Star 1:', tmp)
tmp = next(filter(None, (try_find_beacon(data, y, LIMIT) for y in range(LIMIT+1))))
print('Star 2:', tmp.x * LIMIT + tmp.y)