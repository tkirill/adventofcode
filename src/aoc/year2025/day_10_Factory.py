from typing import Iterable
import functools
from aoc.io import read, readblocks, readlines, readraw, allints
from aoc import board, algorithm, colutils, grid, interval, mathutils, pqueue, rectangle, unionfind, vec2, walker
from aoc.board import Board
from aoc.vec2 import Vec2
from aoc.interval import Interval
from aoc.pqueue import PriorityQueue
from aoc.rectangle import Rectangle
from aoc.unionfind import UnionFind
from aoc.walker import GridWalker


def parse_machine(line: str) -> tuple[int, list[int]]:
    expected, *buttons, wiring = line.split()
    expected = int(''.join('1' if c == '#' else '0' for c in expected[-1:0:-1]), 2)
    bbb = []
    for bs in buttons:
        b = 0
        for x in allints(bs):
            b |= 1 << x
        bbb.append(b)
    return expected, bbb


def parse_machine2(line: str) -> tuple[tuple[int], list[list[int]]]:
    _, *buttons, expected = line.split()
    expected = tuple(allints(expected))
    bbb = [allints(b) for b in buttons]
    return expected, bbb


def near(buttons: list[int], lights: int) -> Iterable[tuple[int]]:
    for b in buttons:
        yield lights ^ b


def star1():
    machines = read(2025, 10, sep=None, parse=parse_machine)
    result = 0
    for expected, buttons in machines:
        for l, d in algorithm.bfs(0, functools.partial(near, buttons)):
            if l == expected:
                result += d
                break
    return result


def star2():
    pass