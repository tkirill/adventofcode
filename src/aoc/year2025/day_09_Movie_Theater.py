from itertools import combinations, pairwise

from aoc.io import read
from aoc import grid, board
from aoc.vec2 import Vec2
from aoc.board import Board


def star1():
    tiles = read(2025, 9, sep=',')
    return max((abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1) for a, b in combinations(tiles, 2))


def star2():
    pass