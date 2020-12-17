from collections import defaultdict
from itertools import product


def adj(cell, dimensions):
    for delta in product([-1, 0, 1], repeat=dimensions):
        x = tuple(a+b for a, b in zip(cell, delta))
        if x != cell:
            yield x


def simulate(field):
    dimensions = len(next(iter(field)))
    for cycle in range(6):
        nf = set()
        for cell in field:
            a = sum(1 for x in adj(cell, dimensions) if x in field)
            if a == 2 or a == 3:
                nf.add(cell)
            for neigh in adj(cell, dimensions):
                if neigh in field:
                    continue
                a = sum(1 for x in adj(neigh, dimensions) if x in field)
                if a == 3:
                    nf.add(neigh)
        field = nf
    return len(field)


def star1():
    lines = [line.strip() for line in open('input.txt')]
    field = set()
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == '#':
                field.add((row, col, 0))
    print(simulate(field))


def star2():
    lines = [line.strip() for line in open('input.txt')]
    field = set()
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == '#':
                field.add((row, col, 0, 0))
    print(simulate(field))


print('Star 1:')
star1()
print('Star 2:')
star2()