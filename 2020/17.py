from collections import Counter
from itertools import product, chain


def adj(cell, dimensions):
    for delta in product([-1, 0, 1], repeat=dimensions):
        x = tuple(a+b for a, b in zip(cell, delta))
        if x != cell:
            yield x


def simulate(field):
    dimensions = len(next(iter(field)))
    for cycle in range(6):
        counts = Counter(chain.from_iterable(adj(cell, dimensions) for cell in field))
        field = set(k for k, v in counts.items() if v == 3 or v == 2 and k in field)
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