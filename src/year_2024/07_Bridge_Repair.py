from aoc.io import *
import itertools as itls


def can_combine(items, ops):
    expected = items[0]
    values = items[1:]
    for cur_ops in itls.product(ops, repeat=len(values) - 1):
        result = values[0]
        for op, v in zip(cur_ops, values[1:]):
            if op == '+':
                result += v
            elif op == '*':
                result *= v
            else:
                result = int(str(result) + str(v))
            if result > expected:
                break
        if result == expected:
            return True
    return False


items = read(sep=r':?\s', parse=int, skip_empty=True)
print('Star 1:', sum(i[0] for i in items if can_combine(i, '+*')))
print('Star 2:', sum(i[0] for i in items if can_combine(i, '+*|')))