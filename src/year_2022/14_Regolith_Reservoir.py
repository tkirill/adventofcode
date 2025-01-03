from __future__ import annotations
from aoc.io import *
from aoc.primitives import *
from aoc import grid
from aoc import algo
from aoc import vec2
from collections import defaultdict
from more_itertools import windowed, chunked, ilen


def read_cave():
    cave = defaultdict(int)
    for line in read(sep=' -> |,'):
        for p1, p2 in windowed(chunked(line, 2), 2):
            cave.update((p, 1) for p in vec2.range_to(Vec2(*p1), Vec2(*p2)))
    floor = max(v.y for v in cave.keys())
    return cave, floor


def sand(cave, floor):
    cur = Vec2(500, 0)
    if cave[cur]:
        return
    while True:
        yield cur
        d = grid.screen.down(cur)
        if d.y == floor:
            cave[cur] = 2
            break
        elif not cave[d]:
            cur = d
        elif not cave[grid.screen.left(d)]:
            cur = grid.screen.left(d)
        elif not cave[grid.screen.right(d)]:
            cur = grid.screen.right(d)
        else:
            cave[cur] = 2
            break


def simulate1(cave, floor):
    total = 0
    while True:
        for p in sand(cave, floor+1):
            if p.y == floor:
                return total
        total += 1


def simulate2(cave, floor):
    total = 0
    while True:
        if ilen(sand(cave, floor+2)) == 0:
            return total
        total += 1


cave, floor = read_cave()
print('Star 1:', simulate1(cave, floor))
cave, floor = read_cave()
print('Star 2:', simulate2(cave, floor))


### Alternative solution for part 2 using BFS ###


def simulate2_bfs(cave: defaultdict, floor):
    def is_open(pos: Vec2) -> bool:
        return pos.y != floor and pos not in cave

    def near(cur: Vec2):
        return filter(is_open, [grid.screen.down_left(cur), grid.screen.down(cur), grid.screen.down_right(cur)])

    return algo.bfs(Vec2(500, 0), near)


cave, floor = read_cave()
print('Star 2 (BFS):', ilen(simulate2_bfs(cave, floor+2)))