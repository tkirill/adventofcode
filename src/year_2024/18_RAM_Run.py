from aoc.io import *
from aoc.grid import *
from aoc.primitives import *
from aoc import algo


bytes =[Vec2(x, y) for x, y in read(sep=',')]
first_kilobyte = set(bytes[:1024])
maze = []
for y in range(71):
    maze.append([])
    for x in range(71):
        maze[-1].append('#' if Vec2(x, y) in first_kilobyte else '.')
maze = Field(maze)
print('Star 1:', next(i for pos, i in maze.bfs4(Vec2(0, 0), lambda p1, p2: maze[p2] != '#') if pos == Vec2(70,70)))

for b in bytes[1024:]:
    maze[b] = '#'
    if any(pos == Vec2(70, 70) for pos, _ in maze.bfs4(Vec2(0, 0), lambda p1, p2: maze[p2] != '#') if pos == Vec2(70,70)):
        continue
    print(f'Star 2: {b.x},{b.y}')
    break