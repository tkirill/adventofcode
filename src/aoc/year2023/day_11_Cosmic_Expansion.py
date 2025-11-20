from itertools import combinations

from aoc.io import read
from aoc import board
from aoc.board import Board
from aoc.vec2 import Vec2
from aoc import grid


def distance(a: Vec2, b: Vec2, empty_rows: list[int], empty_cols: list[int], coeff: int) -> int:
    result = grid.mdist(a, b)
    l, r = min(a.x, b.x), max(a.x, b.x)
    result += sum(coeff-1 for col in empty_cols if l <= col <= r)
    l, r = min(a.y, b.y), max(a.y, b.y)
    result += sum(coeff-1 for row in empty_rows if l <= row <= r)
    return result


def star1():
    universe = Board(read(2023, 11, sep=None, parse=list))
    galaxies = [p for p, v in board.cellsv(universe) if v == '#']
    empty_rows = [r for r, row in enumerate(universe.values) if all(c == '.' for c in row)]
    empty_cols = [c for c, col in enumerate(board.colsv(universe)) if all(v == '.' for _, v in col)]
    return sum(distance(a, b, empty_rows, empty_cols, 2) for a, b in combinations(galaxies, 2))


def star2():
    universe = Board(read(2023, 11, sep=None, parse=list))
    galaxies = [p for p, v in board.cellsv(universe) if v == '#']
    empty_rows = [r for r, row in enumerate(universe.values) if all(c == '.' for c in row)]
    empty_cols = [c for c, col in enumerate(board.colsv(universe)) if all(v == '.' for _, v in col)]
    return sum(distance(a, b, empty_rows, empty_cols, 1_000_000) for a, b in combinations(galaxies, 2))


if __name__ == '__main__':
    print('Star 1:', star1())
    print('Star 2:', star2())