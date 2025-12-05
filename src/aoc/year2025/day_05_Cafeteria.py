from aoc.io import readblocks
from aoc import interval


def star1():
    ranges, ings = readblocks(2025, 5, sep=r'-')
    total = 0
    for i in ings:
        if any(l <= i <= r for l, r in ranges):
            total +=1
    return total

def star2():
    ranges, _ = readblocks(2025, 5, sep=r'-')
    ranges.sort()
    merged = interval.union_overlapped(ranges)
    return sum(len(i)+1 for i in merged)