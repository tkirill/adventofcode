from aoc.io import *
from collections import defaultdict
import graphlib


rules, updates = readblocks(sep=r'\||,')


def top_sort(update: list[int]) -> list[int]:
    graph = defaultdict(list)
    for a, b in rules:
        if a in update and b in update:
            graph[b].append(a)
    return list(graphlib.TopologicalSorter(graph).static_order())


result1 = 0
result2 = 0
for m in updates:
    s = top_sort(m)
    if s == m:
        result1 += m[len(m) // 2]
    else:
        result2 += s[len(s) // 2]
print('Star 1:', result1)
print('Star 2:', result2)