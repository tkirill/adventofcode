from aoc import *
from functools import cmp_to_key
from itertools import chain


def cmp_lists(a: list, b: list)-> bool:
    for i in range(min(len(a), len(b))):
        x, y = a[i], b[i]
        if isinstance(x, int) and isinstance(y, int):
            if x < y:
                return True
            if x > y:
                return False
        elif isinstance(x, list) and isinstance(y, list):
            tmp = cmp_lists(x, y)
            if tmp is not None:
                return tmp
        elif isinstance(x, int):
            tmp = cmp_lists([x], y)
            if tmp is not None:
                return tmp
        elif isinstance(y, int):
            tmp = cmp_lists(x, [y])
            if tmp is not None:
                return tmp
    if len(a) < len(b):
        return True
    if len(a) > len(b):
        return False
    return None


def cmppackets(a, b):
    match(cmp_lists(a, b)):
        case True: return -1
        case False: return 1
        case _: return 0


blocks = readblocks(parse=eval)
print('Star 1:', sum(i+1 for i, b in enumerate(blocks) if cmp_lists(*b)))

packets = list(chain.from_iterable(blocks))
packets.append([[2]])
packets.append([[6]])
packets.sort(key=cmp_to_key(cmppackets))
print('Star 2:', (packets.index([[2]])+1) * (packets.index([[6]])+1))