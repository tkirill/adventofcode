# https://adventofcode.com/2021/day/1
from utils import *
from typing import List


def count_increases(s: list, gap=1) -> int:
    return sum(s[i] > s[i-gap] for i in range(gap, len(s)))


print('Star 1:', count_increases(read('1_input.txt')))
print('Star 2:', count_increases(read('1_input.txt'), 3))