from aoc import *
import re
from itertools import count


def read_input():
    a, b = re.search('row (\d+), column (\d+)',readraw()).groups()
    return int(a), int(b)


erow, ecol = read_input()
cur = 20151125
for start_row in count(2):
    for row, col in zip(range(start_row, -1, -1), range(1, start_row+1)):
        cur = (cur * 252533) % 33554393
        if row == erow and col == ecol:
            print('Star 1:', cur)