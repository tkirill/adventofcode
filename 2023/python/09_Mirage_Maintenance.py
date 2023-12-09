from aoc import *
import itertools as itls


def extrapolate(l):
    diffs = []
    allzero = True
    for a, b in itls.pairwise(l):
        diffs.append(b - a)
        allzero = allzero and diffs[-1] == 0
    if allzero:
        return l[-1], l[-1]
    tmp = extrapolate(diffs)
    return l[-1] + tmp[0], l[0] - tmp[1]


lines = read()
result = [extrapolate(l) for l in lines]
print("Star 1:", sum(r[0] for r in result))
print("Star 2:", sum(r[1] for r in result))
