# https://adventofcode.com/2021/day/2
from utils import *
from typing import Iterable, Tuple


pos, aim = complex(0), 0
for d, v in read('2_input.txt', sep=' '):
    match d:
        case 'forward':
            pos += complex(v, aim*v)
        case 'down':
            aim += v
        case _:
            aim -= v
print('Star 1:', pos.real*aim)
print('Star 2:', pos.real*pos.imag)