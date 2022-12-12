from aoc import *


favnumber = read()[0]
def is_open(pos: Vec2):
    x, y = pos.x, pos.y
    tmp = (x*x + 3*x + 2*x*y + y + y*y + favnumber)
    return bin(tmp)[2:].count('1') % 2 == 0


def near(pos: Vec2):
    for n in pos.near4():
        if n.x >= 0 and n.y >= 0 and is_open(n):
            yield n


start = Vec2(1, 1)
print('Star 1:', next(dist for v, dist in start.bfs(near) if v == Vec2(31, 39)))
near50 = set(v for v, dist in start.bfs(near) if dist <= 50)
print('Star 2:', len(near50))