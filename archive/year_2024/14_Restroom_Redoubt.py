from aoc.io import *
from aoc.primitives import *
from aoc.grid import *
from collections import Counter


W, H = 101, 103


def quadrant(pos: Vec2, w: int, h: int):
    mx, my = w // 2, h // 2
    if 0 <= pos.x < mx and 0 <= pos.y < my:
        return 0
    if mx < pos.x < w and 0 <= pos.y < my:
        return 1
    if mx < pos.x < w and my < pos.y < h:
        return 2
    if 0 <= pos.x < mx and my < pos.y < h:
        return 3
    return 5


robots = [GridWalker(Vec2(x, y), Vec2(vx, vy)) for x, y, vx, vy in read(sep=None, parse=allints)]
for _ in range(100):
    robots = [r.step().mod_by(W, H) for r in robots]

result = 1
for k, v in Counter(quadrant(x.pos, W, H) for x in robots).items():
    if k != 5:
        result *= v
print('Star 1:', result)


def print_robots(robots):
    arr = [['.'] * W for _ in range(H)]
    for r in robots:
        arr[r.pos.y][r.pos.x] = '#'
    for r in arr:
        yield ''.join(r)


robots = [GridWalker(Vec2(x, y), Vec2(vx, vy)) for x, y, vx, vy in read(sep=None, parse=allints)]
pattern = '#' * 10
for i in range(10000):
    if any(pattern in s for s in print_robots(robots)):
        print('Star 2:', i)
        print()
        for s in print_robots(robots):
            print(s)
        break
    robots = [r.step().mod_by(W, H) for r in robots]