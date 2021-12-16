# https://adventofcode.com/2021/day/12
from utils import *
from collections import defaultdict


G = defaultdict(list)
for l, r in read('12_input.txt', sep='-'):
    G[l].append(r)
    G[r].append(l)


def backtrack(cur: str, visited: set[str], can_repeat: bool):
    if cur == 'end':
        return 1
    counter = 0
    for n in G[cur]:
        if n.isupper():
            counter += backtrack(n, visited, can_repeat)
        elif n not in visited:
            visited.add(n)
            counter += backtrack(n, visited, can_repeat)
            visited.remove(n)
        elif can_repeat:
            counter += backtrack(n, visited, False)
    return counter


print('Star 1:', backtrack('start', {'start'}, False))
print('Star 2:', backtrack('start', {'start'}, True))