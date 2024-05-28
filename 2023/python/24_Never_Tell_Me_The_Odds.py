from aoc import *
import itertools as itls
import numpy as np


def equation_2d(x, y, z, dx, dy, dz):
    return [-dy, dx], dx * y - dy * x


def find_intersection(e1, e2):
    a = np.array([e1[0], e2[0]])
    b = np.array([e1[1], e2[1]])
    try:
        return np.linalg.solve(a, b)
    except np.linalg.LinAlgError:
        return None


def is_in_future(h, pos):
    x1, y1, z1, dx, dy, dz = h
    x2, y2 = pos
    return (dx == 0 or (x2 - x1) / dx > 0) and (dy == 0 or (y2 - y1) / dy > 0)


hails = [allints(l) for l in readlines()]
equations = [equation_2d(*h) for h in hails]
star1 = 0
AREA = [200000000000000, 400000000000000]
for e1, e2 in itls.combinations(range(len(equations)), 2):
    i = find_intersection(equations[e1], equations[e2])
    if (
        i is not None
        and all(AREA[0] <= x <= AREA[1] for x in i)
        and is_in_future(hails[e1], i)
        and is_in_future(hails[e2], i)
    ):
        star1 += 1
print("Star 1:", star1)


a = []
b = []
i = 0
for j in range(1, 5):
    xi, yi, zi, dxi, dyi, dzi = hails[i]
    xj, yj, zj, dxj, dyj, dzj = hails[j]
    a.append([dyi - dyj, dxj - dxi, yj - yi, xi - xj])
    b.append(xi * dyi - yi * dxi + yj * dxj - xj * dyj)
X, Y, DX, DY = np.linalg.solve(a, b)

a = []
b = []
for i in range(1, 3):
    xi, yi, zi, dxi, dyi, dzi = hails[i]
    ti = (xi - X) / (DX - dxi)
    a.append([1, ti])
    b.append(zi + ti * dzi)
Z, DZ = np.linalg.solve(a, b)
print("Star 2:", int(X + Y + Z))
