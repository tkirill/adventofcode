from functools import partial
from typing import Iterable

from aoc.io import read
from aoc.algorithm import dijkstra_initial
from aoc import board, walker, grid
from aoc.walker import GridWalker
from aoc.vec2 import Vec2


def near(city: board.Board[int], min_step: int, max_step: int, cur: GridWalker) -> Iterable[tuple[GridWalker, int]]:
    for t in 'CW', 'CCW':
        cw = walker.turn(cur, t)
        total = 0
        for i in range(max_step):
            cw = walker.step(cw)
            if cw not in city:
                break
            total += city[cw]
            if i >= min_step-1:
                yield cw, total


def star1():
    city = board.Board(read(2023, 17, sep=None, parse=lambda x: [int(s) for s in x]))
    dest = Vec2(city.width-1, city.height-1)
    start = [GridWalker(Vec2(), grid.RIGHT), GridWalker(Vec2(), grid.DOWN)]
    for w, d in dijkstra_initial(start, partial(near, city, 1, 3)):
        if w.pos == dest:
            return d


def star2():
    city = board.Board(read(2023, 17, sep=None, parse=lambda x: [int(s) for s in x]))
    dest = Vec2(city.width-1, city.height-1)
    start = [GridWalker(Vec2(), grid.RIGHT), GridWalker(Vec2(), grid.DOWN)]
    for w, d in dijkstra_initial(start, partial(near, city, 4, 10)):
        if w.pos == dest:
            return d