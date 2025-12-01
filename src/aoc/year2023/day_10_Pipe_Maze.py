from typing import Iterable
from itertools import pairwise

from aoc.io import read
from aoc import board
from aoc import grid
from aoc.vec2 import Vec2
from aoc.board import Board


DIRECTIONS = {
    '|': [grid.UP, grid.DOWN],
    '-': [grid.LEFT, grid.RIGHT],
    'L': [grid.UP, grid.RIGHT],
    'J': [grid.UP, grid.LEFT],
    '7': [grid.DOWN, grid.LEFT],
    'F': [grid.DOWN, grid.RIGHT],
    'S': [grid.UP, grid.DOWN, grid.LEFT, grid.RIGHT]
}


JOINTS = {
    grid.UP: ['S', '|', '7', 'F'],
    grid.DOWN: ['S', '|', 'J', 'L'],
    grid.LEFT: ['S', '-', 'L', 'F'],
    grid.RIGHT: ['S', '-', '7', 'J']
}


def check_step(b: Board[str], cur: Vec2, direction: Vec2) -> bool:
    nxt = cur + direction
    if nxt not in b:
        return False
    return b[nxt] in JOINTS[direction]


def walk(b: Board[str], start: Vec2) -> Iterable[Vec2]:
    cur_direction = next(d for d in DIRECTIONS['S'] if check_step(b, start, d))
    yield start, None
    cur = start + cur_direction
    while cur != start:
        yield cur, cur_direction
        incoming = grid.opposite(cur_direction)
        cur_direction = next(d for d in DIRECTIONS[b[cur]] if d != incoming)
        cur += cur_direction


def scanline(b: Board[str], loop: set[Vec2]) -> int:
    # https://en.wikipedia.org/wiki/Scanline_rendering
    total = 0
    for row in board.rows(b):
        is_inside = False
        for p in row:
            if p in loop:
                # On my input S must be counted here. Not true in general.
                if b[p] in ['|', 'F', '7', 'S']:
                    is_inside = not is_inside
            else:
                total += is_inside
    return total


def pick_theorem(b: Board[str], loop: list[Vec2]) -> int:
    b = len(loop)
    # Shoelace formula: https://en.wikipedia.org/wiki/Shoelace_formula
    A = 0
    for cur, nxt in pairwise(loop):
        A += (cur.y + nxt.y) * (cur.x - nxt.x)
    A += (loop[-1].y + loop[0].y) * (loop[-1].x - loop[0].x)
    A //= 2
    # Pick's theorem: https://en.wikipedia.org/wiki/Pick%27s_theorem
    return A - b // 2 + 1


def star1():
    maze = Board(read(2023, 10, sep=None, parse=list))
    start = board.find(maze, 'S')
    loop_len = sum(1 for _ in walk(maze, start))
    return loop_len // 2


def star2():
    maze = Board(read(2023, 10, sep=None, parse=list))
    start = board.find(maze, 'S')
    loop = [p for p, _ in walk(maze, start)]
    #return scanline(maze, set(loop))
    return pick_theorem(maze, loop)
