from utils import *


ps, folds = splitfalse(readlines('13_input.txt'))
points = set(map(tuple, parse2d(ps)))


def fold(f):
    dd, am = f.split('=')
    am = int(am)
    if dd[-1] == 'x':
        return set((am - (x - am), y) if x > am else (x, y) for x, y in points)
    return set((x, (am - (y - am))) if y > am else (x, y) for x, y in points)


points = fold(folds[0])
print('Star 1:', len(points))
for f in folds[1:]:
    points = fold(f)

output = [[' '] * 50 for _ in range(6)]
for x, y in points:
    output[y][x] = '#'
print('Star 2:')
for line in output:
    print(''.join(line))