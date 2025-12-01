import re
from collections import defaultdict
from typing import Iterable

from aoc.io import read
from aoc.board import Board
from aoc.rectangle import Rectangle
from aoc import board


def find_numbers(schema: Board[str]) -> Iterable[Rectangle, int]:
    for row, line in enumerate(schema.values):
        for nm in re.finditer('\d+', line):
            yield Rectangle.ylr(row, nm.start(), nm.end()-1), int(nm.group())


def star1():
    schema = Board(read(year=2023, day=3))
    total = 0
    for r, n in find_numbers(schema):
        if any(not str.isdigit(v) and v != '.' for _, v in board.near8v(schema, r)):
            total += n
    return total


def star2():
    schema = Board(read(year=2023, day=3))
    gears = defaultdict(list)
    for r, n in find_numbers(schema):
        for p, v in board.near8v(schema, r):
            if v == '*':
                gears[p].append(n)
    return sum(numbers[0] * numbers[1] for numbers in gears.values() if len(numbers) == 2)
