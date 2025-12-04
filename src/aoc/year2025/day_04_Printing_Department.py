from collections import deque

from aoc import board
from aoc.io import read
from aoc.board import Board


def star1():
    maze = Board(read(2025, 4, sep=None, parse=list))
    return sum(1 for p in board.find(maze, '@') if board.count_near8(maze, p, '@') < 4)


def star2():
    maze = Board(read(2025, 4, sep=None, parse=list))
    total = 0
    q = deque(board.find(maze, '@'))
    while q:
        cur = q.popleft()
        if maze[cur] == '@' and board.count_near8(maze, cur, '@') < 4:
            maze[cur] = '.'
            total += 1
            q.extend(board.find_near8(maze, cur, '@'))
    return total
