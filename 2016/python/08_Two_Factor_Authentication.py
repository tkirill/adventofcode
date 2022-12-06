from aoc import *


def draw(field, instructions):
    for i in instructions:
        if i.startswith('rect'):
            x, y = allints(i)
            for xx in range(x):
                for yy in range(y):
                    field[yy][xx] = True
        elif i.startswith('rotate row'):
            y, n = allints(i)
            field[y] = circshift(field[y], n)
        elif i.startswith('rotate column'):
            x, n = allints(i)
            tmp = circshift(columns(field)[x], n)
            setcolumn(field, x, tmp)



instructions = readlines()
field = [[False]*50 for _ in range(6)]
draw(field, instructions)
print('Star 1:', count2d(field))
print('Star 2:')
display2d(field)