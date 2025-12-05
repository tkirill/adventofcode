from aoc.io import readblocks


def star1():
    ranges, ings = readblocks(2025, 5, sep=r'-')
    total = 0
    for i in ings:
        if any(l <= i <= r for l, r in ranges):
            total +=1
    return total

def star2():
    pass