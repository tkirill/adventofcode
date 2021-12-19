from utils import *
from itertools import combinations
from math import comb, floor, ceil
import functools


def is_leaf(a):
    return isinstance(a, list) and all(isinstance(x, int) for x in a)


def infix(root):
    result = []
    def sub(root):
        if isinstance(root[0], int):
            result.append((root, 0))
        else:
            sub(root[0])
        if isinstance(root[1], int):
            result.append((root, 1))
        else:
            sub(root[1])
    sub(root)
    return result


def explode(a):
    inf = infix(a)
    def sub2(root, lvl):
        for i in [0, 1]:
            if lvl >= 3 and is_leaf(root[i]):
                tmp = root[i]
                root[i] = 0
                pos = next(i for i in range(len(inf)) if id(inf[i][0]) == id(tmp))
                if pos > 0:
                    l, p = inf[pos-1]
                    l[p] += tmp[0]
                if pos < len(inf)-2:
                    l, p = inf[pos+2]
                    l[p] += tmp[1]
                return True
            elif isinstance(root[i], list) and sub2(root[i], lvl+1):
                return True
        return False
    exploded = sub2(a, 0)
    return exploded


def split(a):
    def sub(root):
        if isinstance(root[0], int) and root[0] >= 10:
            root[0] = [floor(root[0] / 2), ceil(root[0] / 2)]
            return True
        elif isinstance(root[0], list) and sub(root[0]):
            return True
        elif isinstance(root[1], int) and root[1] >= 10:
            root[1] = [floor(root[1] / 2), ceil(root[1] / 2)]
            return True
        elif isinstance(root[1], list) and sub(root[1]):
            return True
        return False
    return sub(a)


def reduce(a):
    reduced = explode(a) or split(a)
    while reduced:
        reduced = explode(a) or split(a)


def add(a, b):
    tmp = [eval(repr(a)), eval(repr(b))]
    reduce(tmp)
    return tmp


def magnitude(a):
    if isinstance(a, int):
        return a
    return 3*magnitude(a[0]) + 2*magnitude(a[1])


lines = [eval(line) for line in readlines('18_input.txt')]
s = functools.reduce(add, lines)
print('Star 1:', magnitude(s))
print('Star 2:', max(max(magnitude(add(a, b)), magnitude(add(b, a))) for a, b in combinations(lines, 2)))