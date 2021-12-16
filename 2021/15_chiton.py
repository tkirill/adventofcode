# https://adventofcode.com/2021/day/15
from utils import *

grid = [[int(x) for x in line] for line in readlines('15_input.txt')]

def dijkstra(grid):
    dist = {(r, c): 1000*1000 for r, c, _ in cells(grid)}
    dist[(0, 0)] = 0
    prev = dict()
    q = [(0, 0)]

    while q:
        q.sort(key=lambda x: dist[x], reverse=True)
        cur = q.pop()
        for r, c, risk in near(cur[0], cur[1], grid):
            alt = dist[cur] + risk
            if alt < dist[(r, c)]:
                dist[(r, c)] = alt
                prev[(r, c)] = cur
                q.append((r, c))
    cur = (len(grid)-1, len(grid[0])-1)
    total = 0
    while cur:
        total += grid[cur[0]][cur[1]]
        cur = prev.get(cur)
    return total - grid[0][0]

print('Star 1:', dijkstra(grid))

new_grid = [[0]*len(grid[0])*5 for _ in range(len(grid)*5)]
for row in range(len(new_grid)):
    for col in range(len(new_grid[0])):
        delta = row // len(grid) + col // len(grid[0])
        new_grid[row][col] = (grid[row%len(grid)][col%len(grid[0])] + delta - 1) % 9 + 1
print('Star 2:', dijkstra(new_grid))