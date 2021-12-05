from utils import *
from collections import Counter


def read_input(allow_diagonal):
    lines = readlines('5_input.txt')
    for line in lines:
        start, end = [parse1d(x, ',') for x in line.split(' -> ')]
        dx, dy = [sign(end[pos] - start[pos]) for pos in [0, 1]]
        if dx and dy and not allow_diagonal:
            continue
        yield tuple(start)
        while start != end:
            start[0] += dx
            start[1] += dy
            yield tuple(start)


print('Star 1:', sum(1 for _, v in Counter(read_input(False)).items() if v > 1))
print('Star 2:', sum(1 for _, v in Counter(read_input(True)).items() if v > 1))