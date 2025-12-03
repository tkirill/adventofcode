from aoc.io import readlines
from aoc import colutils


def joltage(bank: list[int], batteries: int, start: int=0) -> int:
    for b in range(9, 0, -1):
        i = colutils.index(bank, b, start)
        if i == -1:
            continue
        if batteries == 1:
            return b
        j = joltage(bank, batteries-1, i+1)
        if j != -1:
            return b * 10**(batteries-1) + j
    return -1


def star1():
    banks = readlines(2025, 3)
    banks = [[int(x) for x in b] for b in banks]
    return sum(joltage(b, 2) for b in banks)


def star2():
    banks = readlines(2025, 3)
    banks = [[int(x) for x in b] for b in banks]
    return sum(joltage(b, 12) for b in banks)
