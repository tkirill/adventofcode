from typing import Iterable
from itertools import takewhile
from more_itertools import last

from aoc.io import read
from aoc.board import Board
from aoc import board
from aoc import grid


def tilt(platform: Board[str]) -> Iterable[int]:
    for p, v in board.cellsv(platform):
        if v != 'O':
            continue
        dst = last(takewhile(lambda x: x[1] == '.', board.beamv(platform, p, grid.UP, skip_start=True)), None)
        if dst is None:
            yield platform.height - p.y
            continue
        board.swap(platform, p, dst[0])
        yield platform.height - dst[0].y


def star1():
    platform = Board(read(2023, 14, sep=None, parse=list))
    return sum(tilt(platform))


def star2():
    pass


if __name__ == '__main__':
    print('Star 1:', star1())
    print('Star 2:', star2())
