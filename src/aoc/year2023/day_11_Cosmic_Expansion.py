from itertools import combinations, accumulate
from typing import Iterable

from aoc.io import read
from aoc import board
from aoc.board import Board
from aoc.vec2 import Vec2
from aoc import grid


def find_galaxies(universe: Board[str]) -> tuple[list[Vec2], list[int], list[bool]]:
    galaxies, is_empty_row, is_empty_col = [], [1] * universe.height, [1] * universe.width
    for p, v in board.cellsv(universe):
        if v == '#':
            galaxies.append(p)
            is_empty_row[p.y] = 0
            is_empty_col[p.x] = 0
    return galaxies, list(accumulate(is_empty_row)), list(accumulate(is_empty_col))


def distance(a: Vec2, b: Vec2, empty_rows: list[int], empty_cols: list[int], coeff: int) -> int:
    result = grid.mdist(a, b)
    l, r = min(a.x, b.x), max(a.x, b.x)
    result += (empty_cols[r] - empty_cols[l]) * (coeff-1)
    l, r = min(a.y, b.y), max(a.y, b.y)
    result += (empty_rows[r] - empty_rows[l]) * (coeff-1)
    return result


def star1():
    universe = Board(read(2023, 11, sep=None, parse=list))
    galaxies, empty_rows, empty_cols = find_galaxies(universe)
    return sum(distance(a, b, empty_rows, empty_cols, 2) for a, b in combinations(galaxies, 2))


def star2():
    universe = Board(read(2023, 11, sep=None, parse=list))
    galaxies, empty_rows, empty_cols = find_galaxies(universe)
    return sum(distance(a, b, empty_rows, empty_cols, 1_000_000) for a, b in combinations(galaxies, 2))


if __name__ == '__main__':
    print('Star 1:', star1())
    print('Star 2:', star2())
