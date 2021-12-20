from itertools import combinations
from utils import *
import numpy as np


X = np.array([
    [1, 0, 0],
    [0, 0, -1],
    [0, 1, 0]])
Y = np.array([
    [0, 0, 1],
    [0, 1, 0],
    [-1, 0, 0]])
Z = np.array([
    [0, -1, 0],
    [1, 0, 0],
    [0, 0, 1]])
ROTATIONS = [
    np.eye(3, dtype=int), Z, Z@Z, Z@Z@Z,
    X, X@Z, X@Z@Z, X@Z@Z@Z,
    X@X, X@X@Z, X@X@Z@Z, X@X@Z@Z@Z,
    X@X@X, X@X@X@Z, X@X@X@Z@Z, X@X@X@Z@Z@Z,
    Y, Y@Z, Y@Z@Z, Y@Z@Z@Z,
    Y@Y@Y, Y@Y@Y@Z, Y@Y@Y@Z@Z, Y@Y@Y@Z@Z@Z
]


def is_shifted(s1, s2):
    set1 = set(map(tuple, s1))
    for x, y in product(s1, s2):
        delta = x - y
        counter = 0
        for v in s2+delta:
            if tuple(v) in set1:
                counter += 1
                if counter == 12:
                    return delta


scans = [np.array(x[1:]) for x in read('19_input.txt')]
intersections = [[] for _ in range(len(scans))]
q, visited = [0], {0}
while q:
    cur = q.pop()
    for i in range(len(scans)):
        if i != cur and i not in visited:
            for r in ROTATIONS:
                tmp = (r @ scans[i].transpose()).transpose()
                delta = is_shifted(scans[cur], tmp)
                if delta is not None:
                    print(cur, i, delta)
                    print(r)
                    print()
                    intersections[cur].append((i, r, delta))
                    q.append(i)
                    visited.add(i)
                    break

scanners, beacons = [(0, 0, 0)]*len(scans), set()
q = [(0, np.eye(3, dtype=int), np.zeros(3, dtype=int))]
while q:
    n, r, s = q.pop()
    tmp = (r @ scans[n].transpose()).transpose() + s
    beacons |= set(map(tuple, tmp))
    for nn, nr, ns in intersections[n]:
        q.append((nn, r@nr, (r@ns.transpose())+s))
        scanners[nn] = (r@ns.transpose()).transpose() + s
print('Star 1:', len(beacons))
print('Star 2:', max(np.abs(x-y).sum() for x, y in combinations(scanners, 2)))
