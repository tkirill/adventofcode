from itertools import product
from collections import Counter


def read_input():
    grid = set()
    for y, l in enumerate(open('18_input.txt')):
        for x, c in enumerate(l.strip()):
            if c == '#':
                grid.add((x, y))
    return grid


def simulate(G):
    cnts = Counter((x+dx, y+dy) for x, y in G for dx, dy in product([-1, 0, 1], repeat=2) if dx or dy)
    nxt = set()
    for p, c in cnts.items():
        if any(x < 0 or x >= 100 for x in p):
            continue
        if p in G:
            if c in [2,3]:
                nxt.add(p)
        elif c == 3:
            nxt.add(p)
    return nxt


G = read_input()
for _ in range(100):
    G = simulate(G)
print('Star 1:', len(G))

G = read_input()
G.update(product([0, 99], repeat=2))
for _ in range(100):
    G = simulate(G)
    G.update(product([0, 99], repeat=2))
print('Star 2:', len(G))