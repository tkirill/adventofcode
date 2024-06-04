from __future__ import annotations
from aoc import *
from collections import defaultdict
import random


class Graph:
    
    def __init__(self, vertices: Iterable[str], edges: dict[list[str]]):
        self.vertices = list(vertices)
        self.edges = {k: list(v) for k, v in edges.items()}
    
    
    def contract(self, a: str, b: str) -> str:
        tmp = a + b
        self.edges[tmp] = []
        for c in self.edges[a]:
            if c == b:
                continue
            self.edges[c].append(tmp)
            self.edges[tmp].append(c)
            self.edges[c][:] = (x for x in self.edges[c] if x != a)
        for c in self.edges[b]:
            if c == a:
                continue
            self.edges[c].append(tmp)
            self.edges[tmp].append(c)
            self.edges[c][:] = (x for x in self.edges[c] if x != b)
        del self.edges[a]
        del self.edges[b]
        self.vertices.remove(a)
        self.vertices.remove(b)
        self.vertices.append(tmp)
        return tmp
    
    
    @classmethod
    def read(cls) -> Graph:
        edges = defaultdict(list)
        vertices = set()
        for item in read(sep=r':? '):
            for x in item[1:]:
                edges[item[0]].append(x)
                edges[x].append(item[0])
                vertices.add(item[0])
                vertices.add(x)
        return Graph(vertices, edges)


# https://en.wikipedia.org/wiki/Karger%27s_algorithm
def karger(graph: Graph):
    sizes = dict()
    while len(graph.vertices) > 2:
        a = random.choice(graph.vertices)
        b = random.choice(graph.edges[a])
        tmp = graph.contract(a, b)
        sizes[tmp] = sizes.get(a, 1) + sizes.get(b, 1)
    print(len(graph.edges[graph.vertices[0]]))
    if len(graph.edges[graph.vertices[0]]) == 3:
        return sizes[graph.vertices[0]] * sizes[graph.vertices[1]]

random.seed()
while True:
    G = Graph.read()
    a = karger(G)
    if a is not None:
        print('Star 1:', a)
        break