import re
from collections import defaultdict
from itertools import permutations, pairwise


def read_input():
    g = defaultdict(int)
    v = set()
    for line in open('13_input.txt'):
        a, op, w, b = re.match(r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)', line).groups()
        g[(a, b)] = int(w) if op == 'gain' else -int(w)
        v.add(a)
        v.add(b)
    return g, v


def calc(p):
    return sum(G[a, b] for a, b in pairwise(p)) + G[(p[-1], p[0])] + sum(G[a, b] for a, b in pairwise(reversed(p))) + G[(p[0], p[-1])]


G, V = read_input()
print('Star 1:', max(calc(p) for p in permutations(V)))
V.add('Me')
print('Star 2:', max(calc(p) for p in permutations(V)))