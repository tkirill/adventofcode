from aoc.io import *
from aoc.grid import *
from aoc.primitives import *
import networkx as nx
from collections import defaultdict


graph = defaultdict(set)
for a, b in read(sep='-'):
    graph[a].add(b)
    graph[b].add(a)

triples = set()
for x in graph:
    if x.startswith('t'):
        for tn in graph[x]:
            for tnn in graph[x] & graph[tn]:
                tmp = [x, tn, tnn]
                tmp.sort()
                triples.add(tuple(tmp))
print('Star 1:', len(triples))



ngraph = nx.Graph(read(sep='-'))
mmm = max(nx.find_cliques(ngraph), key=len)
print('Star 2:', ','.join(sorted(mmm)))