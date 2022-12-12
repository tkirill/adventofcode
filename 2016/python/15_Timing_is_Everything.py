from aoc import *
from itertools import count


def is_pass(lag: int) -> bool:
    cur = lag
    for d in discs:
        cur += 1
        if (d[1] + cur) % d[0]:
            return False
    return True


discs = [(x[1], x[-1]) for x in read(sep=None, parse=allints)]
print('Star 1:', next(filter(is_pass, count())))
discs.append((11, 0))
print('Star 2:', next(filter(is_pass, count())))