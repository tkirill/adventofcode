import itertools

from aoc.io import read


def star1():
    ranges = itertools.batched(read(2025, 2, sep=r',|-')[0], 2)
    total = 0
    for a, b in ranges:
        for i in range(a, b+1):
            s = str(i)
            mid = len(s)//2
            if s[:mid] == s[mid:]:
                total += i
    return total


def star2():
    ranges = itertools.batched(read(2025, 2, sep=r',|-')[0], 2)
    total = 0
    for a, b in ranges:
        for i in range(a, b+1):
            s = str(i)
            if s in (s + s)[1:-1]:
                total += i
    return total