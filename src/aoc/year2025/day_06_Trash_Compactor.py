from aoc.io import readlines, read
from aoc import board


def star1():
    items = read(2025, 6)
    total = 0
    for *a, op in zip(*items):
        match op:
            case '+':
                total += sum(a)
            case '*':
                tmp = 1
                for x in a:
                    tmp *= x
                total += tmp
    return total


def star2():
    items = board.Board(readlines(2025, 6, strip_chars='\n'))
    total = 0
    args = []

    for col in board.colsv(items, _reversed=True):
        vals = ''.join(v for _, v in col)
        if all(x == ' ' for x in vals):
            continue
        if '+' not in vals and '*' not in vals:
            args.append(int(vals))
            continue
        args.append(int(vals[:-1]))
        match vals[-1]:
            case '+':
                total += sum(args)
            case '*':
                tmp = 1
                for x in args:
                    tmp *= x
                total += tmp
        args.clear()
    return total
