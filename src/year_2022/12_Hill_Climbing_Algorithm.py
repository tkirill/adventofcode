from aoc.io import *
from aoc.grid import Field
from aoc.algo import orddiff
        

grid = Field(read(sep=None, parse=list))
start = next(pos for pos, v in grid.cellsv() if v == 'S')
dest = next(pos for pos, v in grid.cellsv() if v == 'E')
grid[start] = 'a'
grid[dest] = 'z'

bfs = grid.bfs4(start, lambda f, t: orddiff(grid[f], grid[t]) <= 1)
print('Star 1:', next(dist for x, dist in bfs if x == dest))
bfs = grid.bfs4(dest, lambda f, t: orddiff(grid[t], grid[f]) <= 1)
print('Star 2:', next(dist for x, dist in bfs if grid[x] == 'a'))