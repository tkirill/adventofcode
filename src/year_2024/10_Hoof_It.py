from aoc.io import *
from aoc.primitives import *
from aoc.grid import *


maze = Field(read(sep=None, parse=lambda s: [int(x) for x in s]))
score1, score2 = 0, 0
for pos, v in maze.cellsv():
    if v != 0:
        continue
    nines = [pos for pos, _ in maze.bfs4(pos, lambda p1, p2: maze[p2]-maze[p1] == 1, track_visited=False) if maze[pos] == 9]
    score1 += len(set(nines))
    score2 += len(nines)
print('Star 1:', score1)
print('Star 2:', score2)
