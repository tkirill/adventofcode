from aoc.io import *
from aoc.grid import *
from aoc.primitives import *
from aoc import vec2


def count_cheats(max_cheat: int):
    cheats = 0
    for cur, curv in maze.cellsv():
        if curv == '#':
            continue
        for n, nv in maze.circlev(cur, max_cheat):
            if nv == '#':
                continue
            saves = dist_from_start[dest] - (dist_from_start[cur] + vec2.mdist(cur, n) + dist_from_dest[n])
            if saves >= 100:
                cheats += 1
    return cheats


maze = Field(read(sep=None, parse=list))
start = next(pos for pos, v in maze.cellsv() if v == 'S')
dest = next(pos for pos, v in maze.cellsv() if v == 'E')
dist_from_start = {pos: i for pos, i in maze.bfs4(start, lambda p1, p2: maze[p2] != '#')}
dist_from_dest = {pos: i for pos, i in maze.bfs4(dest, lambda p1, p2: maze[p2] != '#')}
print('Star 1:', count_cheats(2))
print('Star 2:', count_cheats(20))
