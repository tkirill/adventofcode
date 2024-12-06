from aoc.io import *
from aoc.primitives import *
from aoc.grid import *
from aoc import algo
import sys
from collections import deque

sys.setrecursionlimit(2000)


def near(maze: Field, cur: Vec2) -> list[Vec2]:

    def impl():
        match maze[cur]:
            case '.':
                yield from maze.grid.near4(cur)
                return
            case '>':
                yield maze.grid.right(cur)
                return
            case '<':
                yield maze.grid.left(cur)
                return
            case '^':
                yield maze.grid.up(cur)
                return
            case 'v':
                yield maze.grid.down(cur)
                return
    
    return [p for p in impl() if p in maze and maze[p] != '#']


def find_junctions(maze: Field, src: Vec2, dst: Vec2) -> Iterable[tuple[Vec2, int]]:

    def nearrr(cur) -> Iterable[Vec2]:
        nears = near(maze, cur)
        if cur != src and len(nears) > 2:
            return []
        return nears

    for n, d in algo.bfs(src, nearrr):
        if len(near(maze, n)) > 2 or n == dst:
            yield n, d


def compaction(maze: Field, src: Vec2, dst: Vec2) -> dict[Vec2, dict[Vec2, int]]:
    compacted = dict()
    dq = deque([src])
    while dq:
        cur = dq.popleft()
        compacted[cur] = dict()
        for j, d in find_junctions(maze, cur, dst):
            curd = compacted[cur].get(j, 0)
            if d > curd:
                compacted[cur][j] = d
        for j in compacted[cur]:
            if j not in compacted:
                dq.append(j)
    return compacted


def find_longest_path(graph: dict[Vec2, dict[Vec2, int]], src: Vec2, dst: Vec2) -> Optional[int]:
    def dfs(cur: Vec2, visited: set[Vec2]) -> Optional[int]:
        if cur == dst:
            return 0
        visited.add(cur)
        max_dst = None
        for n, d in graph[cur].items():
            if n in visited:
                continue
            c = dfs(n, visited)
            if c is not None and (max_dst is None or c+d > max_dst):
                max_dst = c+d
        visited.remove(cur)
        return max_dst
    return dfs(src, set())


maze = Field(read(parse=list))
src = next(p for p, v in maze.rowv(0) if v == '.')
dst = next(p for p, v in maze.rowv(maze.h-1) if v == '.')
compacted = compaction(maze, src, dst)
print('Star 1:', find_longest_path(compacted, src, dst))
maze = Field(read(parse=lambda s: list(re.sub('[<>v^]', '.', s))))
compacted = compaction(maze, src, dst)
print('Star 2:', find_longest_path(compacted, src, dst))