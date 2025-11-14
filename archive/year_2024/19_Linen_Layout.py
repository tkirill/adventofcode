from aoc.io import *
from functools import cache


@cache
def count_ways(design: str) -> int:
    if not design:
        return 1
    return sum(count_ways(design[len(towel):]) for towel in towels if design.startswith(towel))


[towels], designs = readblocks(sep=r', ')
print('Star 1:', sum(count_ways(d) > 0 for d in designs))
print('Star 2:', sum(count_ways(d) for d in designs))