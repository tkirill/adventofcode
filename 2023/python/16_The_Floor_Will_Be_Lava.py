from aoc import *


map = Field(read())


def near(cur: Walker2d):
    if cur.pos not in map:
        return

    match map[cur.pos]:
        case ".":
            yield cur.step()
        case "|" if cur.dir.x:
            yield cur.rotatelr("L").step()
            yield cur.rotatelr("R").step()
        case "|":
            yield cur.step()
        case "-" if cur.dir.y:
            yield cur.rotatelr("L").step()
            yield cur.rotatelr("R").step()
        case "-":
            yield cur.step()
        case "/" if cur.dir.x:
            yield cur.rotatelr("L").step()
        case "/":
            yield cur.rotatelr("R").step()
        case "\\" if cur.dir.x:
            yield cur.rotatelr("R").step()
        case "\\":
            yield cur.rotatelr("L").step()
        case _:
            raise cur


v = set(x.pos for x, d in bfs(Walker2d(dir=Vec2(1, 0)), near) if x.pos in map)
print(len(v))


dir = Vec2(0, 1)
max_energy = 0
for border in [map.row(0), map.column(map.w - 1), map.row(map.h - 1), map.column(0)]:
    for start in border:
        e = set(x.pos for x, _ in bfs(Walker2d(start, dir), near) if x.pos in map)
        max_energy = max(max_energy, len(e))
    dir = dir.rotatelr("R")
print(max_energy)
