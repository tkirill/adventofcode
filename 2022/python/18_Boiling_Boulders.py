from aoc import *
import re
import math
import string
import itertools as itls
import more_itertools as mtls
from functools import cache
from collections import Counter, defaultdict
from typing import NamedTuple
from dataclasses import dataclass
from pprint import pprint


def near(cube: tuple[int, int, int]) -> Iterable[tuple[int, int, int]]:
    for dim in range(3):
        for delta in [-1, 1]:
            tmp = list(cube)
            tmp[dim] += delta
            yield tuple(tmp)


def count_visible(cubes: set[tuple[int, int, int]]) -> int:
    total = 0
    for cur in cubes:
        for n in near(cur):
            if n not in cubes:
                total += 1
    return total


def count_reachable(cubes: set[tuple[int, int, int]]) -> int:
    borders = [max(c[dim] for c in cubes)+1 for dim in range(3)]

    def near_empty(cur: tuple[int, int, int]) -> Iterable[tuple[int, int, int]]:
        for n in near(cur):
            if all(-1 <= n[i] <= borders[i] for i in range(3)) and n not in cubes:
                yield n

    total = 0
    for cur, _ in bfs((0, 0, 0), near_empty):
        total += mtls.ilen(filter(cubes.__contains__, near(cur)))
    return total


cubes = set(map(tuple, read(sep=',')))
print('Star 1:', count_visible(cubes))
print('Star 2:', count_reachable(cubes))