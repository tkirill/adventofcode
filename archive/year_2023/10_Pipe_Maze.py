from aoc.io import *
from aoc.grid import Field
from aoc import grid


OPPOSITE = {k: v for k, v in ["LR", "RL", "UD", "DU"]}
DIRS = {"|": "UD", "-": "LR", "7": "LD", "J": "LU", "F": "RD", "L": "RU", ".": "LRUD"}


map = Field(read(sep=None, parse=list))
start = next(pos for pos, v in map.cellsv() if v == "S")


def near(pos):
    for d in DIRS[map[pos]]:
        n = grid.screen.step(pos, d)
        if n in map and OPPOSITE[d] in DIRS[map[n]]:
            yield n


def rollback(prev, cur):
    path = []
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    return path


def findloop(start):
    prev = {start: None}
    q = [start]
    curdist = 0
    while q:
        qcopy = list(q)
        q.clear()
        for cur in qcopy:
            for n in near(cur):
                if n not in prev:
                    q.append(n)
                    prev[n] = cur
                elif prev[cur] != n:
                    return rollback(prev, n), rollback(prev, cur)
        curdist += 1


def allloops(start):
    for r in ["-", "|", "L", "J", "7", "F"]:
        map[start] = r
        l = findloop(start)
        if l is not None:
            return l


loop = allloops(start)
loop = set(loop[0]) | set(loop[1])
print("Star 1:", len(loop) // 2)


total = 0
for row in map.rowsv():
    is_inside = False
    for pos, v in row:
        if pos in loop:
            if map[pos] in ["|", "F", "7"]:
                is_inside = not is_inside
        else:
            total += is_inside
print("Star 2:", total)
