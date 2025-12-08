import itertools, more_itertools, functools
from collections import deque, Counter, defaultdict

from aoc.io import read, readblocks, readlines, readraw
from aoc.vec2 import Vec2
from aoc.board import Board
from aoc.walker import GridWalker
from aoc.interval import Interval
from aoc.pqueue import PriorityQueue
from aoc import vec2, board, algorithm, colutils, grid, interval, mathutils, pqueue, rectangle, walker
from aoc.unionfind import UnionFind
import math
import heapq


def eudist(a, b):
    return math.sqrt(sum((bc-ac)**2 for ac, bc in zip(a, b)))


def star1():
    boxes = read(2025, 8, sep=r',')
    circuits = UnionFind(len(boxes))
    pairs = heapq.nsmallest(1000, itertools.combinations(range(len(boxes)), 2), key=lambda x: eudist(boxes[x[0]], boxes[x[1]]))
    for i, j in pairs:
        if circuits.connected(i, j):
            continue
        circuits.union(i, j)
    roots = Counter(circuits.find(i) for i in range(len(boxes)))
    return math.prod(heapq.nlargest(3, roots.values()))


def star2():
    boxes = read(2025, 8, sep=r',')
    circuits = UnionFind(len(boxes))
    pairs = list(itertools.combinations(range(len(boxes)), 2))
    pairs.sort(key=lambda x: eudist(boxes[x[0]], boxes[x[1]]))
    roots = set(range(len(boxes)))
    for i, j in pairs:
        ri, rj = circuits.find(i), circuits.find(j)
        if ri == rj:
            continue
        circuits.union(i, j)
        roots.remove(ri)
        roots.remove(rj)
        roots.add(circuits.find(i))
        if len(roots) == 1:
            return boxes[i][0] * boxes[j][0]
