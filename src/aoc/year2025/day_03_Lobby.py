from aoc.io import readlines
from aoc import colutils


def joltage(bank: list[int], requested: int) -> int:
    selected = []
    for pos, value in enumerate(bank):
        remaining_batteries = len(bank) - pos
        while selected and len(selected) + remaining_batteries > requested and selected[-1] < value:
            selected.pop()
        if len(selected) < requested:
            selected.append(value)
    total = 0
    for r in selected:
        total = total * 10 + r
    return total


def star1():
    banks = readlines(2025, 3)
    banks = [[int(x) for x in b] for b in banks]
    return sum(joltage(b, 2) for b in banks)


def star2():
    banks = readlines(2025, 3)
    banks = [[int(x) for x in b] for b in banks]
    return sum(joltage(b, 12) for b in banks)
