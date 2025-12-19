from itertools import combinations, pairwise

from aoc.io import read
from aoc import grid, board
from aoc.vec2 import Vec2
from aoc.board import Board
from aoc import rectangle
from aoc import polygon

# 1452422268


def star1():
    tiles = read(2025, 9, sep=',')
    return max((abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1) for a, b in combinations(tiles, 2))


def star2():
    tiles = [Vec2(x, y) for x, y in read(2025, 9, sep=',')]
    floor = polygon.Polygon(tiles)
    result = 0
    for u, v in combinations(tiles, 2):
        r = rectangle.Rectangle.by_corners(u, v)
        if polygon.rectangle_inside(floor, r):
            result = max(result, r.square)
    return result