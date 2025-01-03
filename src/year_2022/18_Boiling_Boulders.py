from aoc.io import *
from aoc.primitives import *
from aoc import algo, vec3
from itertools import starmap
from collections.abc import Iterable
from more_itertools import ilen


cubes = set(starmap(Vec3, read(sep=',')))
borders = [max(c[dim] for c in cubes)+1 for dim in range(3)]


def near_empty(cur: Vec3) -> Iterable[Vec3]:
    for n in vec3.near6(cur):
        if all(-1 <= n[i] <= borders[i] for i in range(3)) and n not in cubes:
            yield n


print('Star 1:', sum(ilen((n for n in vec3.near6(x) if n not in cubes)) for x in cubes))
print('Star 2:', sum(ilen(filter(cubes.__contains__, vec3.near6(x))) for x, _ in algo.bfs(Vec3(), near_empty)))