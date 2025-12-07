from typing import Iterable
from functools import partial, cache

from aoc.io import read
from aoc import board, grid, vec2, algorithm
from aoc.vec2 import Vec2
from aoc.board import Board


@board.wrap_contains
def tachyon_step(manifold: Board[str], pos: Vec2) -> Iterable[Vec2]:
    if manifold[pos] != '^':
        yield pos + grid.DOWN
        return
    yield pos + grid.LEFT
    yield pos + grid.RIGHT


def timelines(manifold: Board[str], pos: Vec2) -> int:
    @cache
    def timelines_step(pos: Vec2) -> int:
        if manifold[pos] == '^':
            return timelines_step(pos + grid.LEFT) + timelines_step(pos + grid.RIGHT)
        if pos.y == manifold.height-1:
            return 1
        return timelines_step(pos+grid.DOWN)
    return timelines_step(pos)


def star1():
    manifold = board.Board(read(2025, 7, sep=None, parse=list))
    start = next(board.find(manifold, 'S'))
    return sum(1 for p, _ in algorithm.bfs(start, partial(tachyon_step, manifold)) if manifold[p] == '^')


def star2():
    manifold = board.Board(read(2025, 7, sep=None, parse=list))
    start = next(board.find(manifold, 'S'))
    return timelines(manifold, start)