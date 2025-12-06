from typing import Iterable

from aoc.io import read
from aoc.vec2 import Vec2
from aoc import grid, board


def dig(plan: Iterable[list[str, int, str]]) -> board.Board[str]:
    cur = Vec2(0, 0)
    border = [cur]
    for direction, distance, _ in plan:
        delta = grid.direction(direction)
        border.extend(grid.beam(cur, delta, distance, skip_start=True))
        cur = border[-1]
    return border


def star1():
    plan = read(2023, 18)
    edge = dig(plan)
    return grid.pick_theorem(edge, include_edge=True)
    

def star2():
    pass