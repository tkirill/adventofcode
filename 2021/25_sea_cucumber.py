from utils import *
from itertools import count


grid = [list(s) for s in readlines('25_input.txt')]
H, W = len(grid), len(grid[0])
horq, verq = [], []
for r, c, v in cells(grid):
    if v == '.':
        if grid[r][c-1] == '>':
            horq.append((r, c))
        elif grid[r-1][c] == 'v':
            verq.append((r, c))


for step in count(1):
    if not horq and not verq:
        print('Star 1:', step)
        break
    tmp = []
    for r, c in horq:
        grid[r][c] = '>'
        grid[r][c-1] = '.'

        pc, ppc, nc = (W+c-1)%W, (W+c-2)%W, (c+1)%W
        if grid[r-1][pc] == 'v':
            verq.append((r, pc))
        elif grid[r][ppc] == '>':
            tmp.append((r, pc))
        if grid[r][nc] == '.' and grid[r-1][nc] != 'v':
            tmp.append((r, nc))
    horq = tmp
    tmp = []
    for r, c in verq:
        grid[r][c] = 'v'
        grid[r-1][c] = '.'

        pr, ppr, nr = (H+r-1)%H, (H+r-2)%H, (r+1)%H
        if grid[pr][c-1] == '>':
            horq.append((pr, c))
        elif grid[ppr][c] == 'v':
            tmp.append((pr, c))
        if grid[nr][c] == '.' and grid[nr][c-1] != '>':
            tmp.append((nr, c))
    verq = tmp