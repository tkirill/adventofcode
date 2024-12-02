from aoc.io import *
from aoc.algo import sign
from collections import Counter
from itertools import pairwise


def is_ok(x, s):
    return sign(x) == s and 1 <= abs(x) <= 3


def is_report_ok(r):
    dd = [b-a for a, b in pairwise(r)]
    if not dd[0]:
        return False
    ds = sign(dd[0])
    return all(is_ok(x, ds) for x in dd)


def problem_dampener(r):
    for i in range(len(r)):
        rc = list(r)
        del rc[i]
        if is_report_ok(rc):
            return True
    return False


items = read(sep=r'\s', parse=int, skip_empty=True)
print('Star 1:', sum(1 for r in items if is_report_ok(r)))
print('Star 2:', sum(1 for r in items if is_report_ok(r) or problem_dampener(r)))