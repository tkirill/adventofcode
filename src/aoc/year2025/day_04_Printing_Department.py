from collections import Counter

from aoc import board
from aoc.io import read
from aoc.board import Board


def star1():
    maze = Board(read(2025, 4, sep=None, parse=list))
    counts = Counter()
    for pos, v in board.cellsv(maze):
        if v == '@':
            counts.update(board.near8(maze, pos))
    return sum(1 for p, v in board.cellsv(maze) if v == '@' and counts[p] < 4)


def star2():
    maze = Board(read(2025, 4, sep=None, parse=list))
    total = 0
    while True:
        counts = Counter()
        for pos, v in board.cellsv(maze):
            if v == '@':
                counts.update(board.near8(maze, pos))
        removed = 0
        for p, v in board.cellsv(maze):
            if v == '@' and counts[p] < 4:
                maze[p] = '.'
                removed += 1
        if not removed:
            return total
        else:
            total += removed