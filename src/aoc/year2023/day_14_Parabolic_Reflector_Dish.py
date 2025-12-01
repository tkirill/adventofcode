from typing import Iterable
from itertools import takewhile
from more_itertools import last, consume

from aoc.io import read
from aoc.board import Board
from aoc import board
from aoc import grid
from aoc.vec2 import Vec2
from aoc.algorithm import nth_with_cycle


def tilt(platform: Board[str], delta: Vec2, by_columns: bool, _reversed: bool) -> Iterable[Vec2]:
    for p, v in board.cellsv(platform, by_columns=by_columns, _reversed=_reversed):
        if v != 'O':
            continue
        dst = last(takewhile(lambda x: x[1] == '.', board.beamv(platform, p, delta, skip_start=True)), None)
        if dst is None:
            yield p
            continue
        board.swap(platform, p, dst[0])
        yield dst[0]


def tilt_cycle(platform: Board[str]) -> Iterable[int]:
    while True:
        consume(tilt(platform, grid.UP, by_columns=False, _reversed=False))
        consume(tilt(platform, grid.LEFT, by_columns=True, _reversed=False))
        consume(tilt(platform, grid.DOWN, by_columns=False, _reversed=True))
        key, weight = 0, 0
        for r in tilt(platform, grid.RIGHT, by_columns=True, _reversed=True):
            key += r.y * 1000 + r.x
            weight += platform.height - r.y
        yield key, weight


def star1():
    platform = Board(read(2023, 14, sep=None, parse=list))
    return sum(platform.height - r.y for r in tilt(platform, grid.UP, by_columns=False, _reversed=False))


def star2():
    platform = Board(read(2023, 14, sep=None, parse=list))
    return nth_with_cycle(tilt_cycle(platform), 1_000_000_000-1)[1]
