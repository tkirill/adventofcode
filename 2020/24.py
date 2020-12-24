from collections import Counter
from itertools import chain


STEPS = {'e': 2, 'se': 1+1j, 'sw': -1+1j, 'w': -2, 'nw': -1-1j, 'ne': 1-1j}


def parse_steps(line: str):
    pos = 0
    while pos < len(line):
        step = next(key for key in STEPS if line[pos:].startswith(key))
        yield STEPS[step]
        pos += len(step)


def read_tiles():
    for line in open('input.txt'):
        line = line.strip()
        yield sum(parse_steps(line))


def star1():
    print(sum(1 for x, v in Counter(read_tiles()).items() if v % 2))


def star2():
    blacks = set(x for x, v in Counter(read_tiles()).items() if v % 2)
    for round_n in range(0, 100):
        black_adj = Counter(chain.from_iterable((x + v for v in STEPS.values()) for x in blacks))
        blacks = set(x for x, v in black_adj.items() if v == 2 or (v == 1 and x in blacks))
    print(len(blacks))


print('Star 1:')
star1()
print('Star 2:')
star2()