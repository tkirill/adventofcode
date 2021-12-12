from utils import *
from itertools import count, chain


lines = readlines('11_input.txt')
grid = [[int(x) for x in line] for line in lines]


def increase(cells):
    for row, col, _ in cells:
        grid[row][col] += 1
        if grid[row][col] > 9:
            yield row, col


def step():
    q = list(increase(cells(grid)))
    flashed = set(q)
    while q:
        tmp = []
        for row, col in increase(chain.from_iterable(near8(r, c, grid) for r, c in q)):
            if (row, col) not in flashed:
                tmp.append((row, col))
                flashed.add((row, col))
        q = tmp
    for r, c in flashed:
        grid[r][c] = 0
    return len(flashed)


print('Star 1:', sum(step() for _ in range(100)))
for day in count(101):
    f = step()
    if f == len(grid) * len(grid[0]):
        print('Star 2:', day)
        break