import math

from aoc.io import readlines, read
from aoc import board


def star1():
    items = read(2025, 6)
    return sum(sum(a) if op == '+' else math.prod(a) for *a, op in zip(*items))


def star2():
    items = board.Board(readlines(2025, 6, strip_chars='\n'))
    total = 0
    args = []

    for col in board.colsv(items, _reversed=True):
        vals = ''.join(v for _, v in col).strip()
        if not vals:
            continue
        if vals[-1] not in ['+', '*']:
            args.append(int(vals))
            continue
        args.append(int(vals[:-1]))
        total += sum(args) if vals[-1] == '+' else math.prod(args)
        args.clear()
    return total
