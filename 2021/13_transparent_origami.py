# https://adventofcode.com/2021/day/13
from utils import *


points, folds = read('13_input.txt', sep=',|=')


def fold(dd, am):
    if dd[-1] == 'x':
        return set((am - (x - am), y) if x > am else (x, y) for x, y in points)
    return set((x, (am - (y - am))) if y > am else (x, y) for x, y in points)


points = fold(*folds[0])
print('Star 1:', len(points))
for f in folds[1:]:
    points = fold(*f)

output = [[' '] * 50 for _ in range(6)]
for x, y in points:
    output[y][x] = '#'
print('Star 2:')
for line in output:
    print(''.join(line))