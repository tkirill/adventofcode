from typing import Iterable

from aoc.io import read


def rotate(items: list[tuple[str, int]]) -> Iterable[tuple[int, int]]:
    cur = 50
    for direction, distance in items:
        zero_clicks, dist = divmod(distance, 100)
        prev = cur
        cur += dist if direction == 'R' else -dist
        zero_clicks += (cur <= 0 < prev) or (100 <= cur)
        cur %= 100
        yield cur, zero_clicks


def star1():
    it = read(year=2025, day=1, parse=lambda x: (x[0], int(x[1:])))
    return sum(1 for cur, _ in rotate(it) if cur == 0)


def star2():
    it = read(year=2025, day=1, parse=lambda x: (x[0], int(x[1:])))
    return sum(zc for _, zc in rotate(it))
