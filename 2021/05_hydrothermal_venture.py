# https://adventofcode.com/2021/day/5
from utils import *
from collections import Counter


def read_input2(allow_diagonal):
    for x1, y1, x2, y2 in read('5_input.txt', ',|->'):
        start, end = complex(x1, y1), complex(x2, y2)
        delta = complex(sign(x2-x1), sign(y2-y1))
        if delta.real and delta.imag and not allow_diagonal:
            continue
        yield start
        while start != end:
            start += delta
            yield start


print('Star 1:', sum(1 for _, v in Counter(read_input2(False)).items() if v > 1))
print('Star 2:', sum(1 for _, v in Counter(read_input2(True)).items() if v > 1))