from aoc import *
from itertools import starmap
from more_itertools import ilen


cubes = set(starmap(Vec3, read(sep=',')))
borders = [max(c[dim] for c in cubes)+1 for dim in range(3)]


def near_empty(cur: Vec3) -> Iterable[Vec3]:
    for n in cur.near6():
        if all(-1 <= n[i] <= borders[i] for i in range(3)) and n not in cubes:
            yield n


print('Star 1:', sum(ilen((n for n in x.near6() if n not in cubes)) for x in cubes))
print('Star 2:', sum(ilen(filter(cubes.__contains__, x.near6())) for x, _ in bfs(Vec3(), near_empty)))