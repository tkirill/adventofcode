from aoc.io import *
from functools import cache


@cache
def count_single(x, blinks):
    if blinks == 0:
        return 1
    if x == 0:
        return count_single(1, blinks-1)
    s = str(x)
    if len(s) % 2 == 0:
        a, b = s[:len(s) // 2], s[len(s) // 2:]
        return count_single(int(a), blinks-1) + count_single(int(b), blinks-1)
    return count_single(x * 2024, blinks-1)


stones = allints(readlines()[0])
print('Star 2:', sum(count_single(x, 25) for x in stones))
print('Star 1:', sum(count_single(x, 75) for x in stones))