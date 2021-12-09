from utils import *


lines = [[int(x) for x in line] for line in readlines('9_input.txt')]
low_points_sum = 0
basins = []


def dfs(row, col):
    q = [(row, col)]
    visited = {(row, col)}
    while q:
        r, c = q.pop()
        for nr, nc in near(r, c, lines):
            if (nr, nc) not in visited and lines[nr][nc] != 9:
                q.append((nr, nc))
                visited.add((nr, nc))
    return len(visited)


for row in range(len(lines)):
    for col in range(len(lines[0])):
        if all(x > lines[row][col] for x in nearvals(row, col, lines)):
            low_points_sum += lines[row][col] + 1
            basins.append(dfs(row, col))
basins.sort()


print('Star 1:', low_points_sum)
print('Star 2:', basins[-3]*basins[-2]*basins[-1])