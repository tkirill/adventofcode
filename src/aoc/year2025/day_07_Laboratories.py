from aoc.io import read
from aoc import board
from aoc.board import Board


def count_splitters(manifold: Board[str]) -> int:
    timelines = [0] * len(manifold.values[0])
    splitters = 0
    for row in board.rowsv(manifold):
        for pos, v in row:
            if v == 'S':
                timelines[pos.x] = 1
                break
            if v == '^' and timelines[pos.x]:
                splitters += 1
                timelines[pos.x-1] += timelines[pos.x]
                timelines[pos.x+1] += timelines[pos.x]
                timelines[pos.x] = 0
    return splitters, sum(timelines)


def star1():
    manifold = board.Board(read(2025, 7, sep=None, parse=list))
    splitters, _ = count_splitters(manifold)
    return splitters


def star2():
    manifold = board.Board(read(2025, 7, sep=None, parse=list))
    _, timelines = count_splitters(manifold)
    return timelines
