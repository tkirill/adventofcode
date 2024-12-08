from aoc.io import *
from aoc.grid import *
from aoc import algo


map = Field(read())


def near(cur: GridWalker):
    if cur.pos not in map:
        return

    match map[cur.pos]:
        case ".":
            yield cur.step()
        case "|" if cur.velocity.x:
            yield cur.rotatelr("L").step()
            yield cur.rotatelr("R").step()
        case "|":
            yield cur.step()
        case "-" if cur.velocity.y:
            yield cur.rotatelr("L").step()
            yield cur.rotatelr("R").step()
        case "-":
            yield cur.step()
        case "/" if cur.velocity.x:
            yield cur.rotatelr("L").step()
        case "/":
            yield cur.rotatelr("R").step()
        case "\\" if cur.velocity.x:
            yield cur.rotatelr("R").step()
        case "\\":
            yield cur.rotatelr("L").step()
        case _:
            raise cur


v = set(x.pos for x, d in algo.bfs(GridWalker(velocity=map.grid.delta_right), near) if x.pos in map)
print('Star 1:', len(v))


dir = Vec2(0, 1)
max_energy = 0
for border in [map.row(0), map.column(map.w - 1), map.row(map.h - 1), map.column(0)]:
    for start in border:
        e = set(x.pos for x, _ in algo.bfs(GridWalker(start, dir), near) if x.pos in map)
        max_energy = max(max_energy, len(e))
    dir = map.grid.rotatelr(dir, "R")
print('Star 2:', max_energy)
