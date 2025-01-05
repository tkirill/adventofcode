from aoc.io import *
from aoc.primitives import *
from aoc.grid import *
from pqdict import pqdict
from collections import defaultdict, deque


def dijkstra_all_paths(
    start: GridWalker,
    near: Callable[[GridWalker], Iterable[tuple[GridWalker, int]]]
):
    dist = {start: 0}
    prev = defaultdict(set)
    q = pqdict(dist)

    while q:
        cur = q.pop()
        for n, ndist in near(cur):
            alt = dist[cur] + ndist
            ex = dist.get(n)
            if ex is None or ex > alt:
                dist[n] = alt
                q[n] = alt
                prev[n].add(cur)
            elif ex == alt:
                prev[n].add(cur)
    return dist, prev


def near(cur: GridWalker):
    nxt = cur.step()
    if nxt.pos in maze and maze[nxt.pos] != '#':
        yield nxt, 1
    yield cur.rotatelr('L'), 1000
    yield cur.rotatelr('R'), 1000


maze = Field(read(sep=None, parse=list))
start = GridWalker(next(pos for pos, v in maze.cellsv() if v == 'S'), maze.grid.delta_right)
dest = next(pos for pos, v in maze.cellsv() if v == 'E')
dist, prev = dijkstra_all_paths(start, near)
best = min(v for k, v in dist.items() if k.pos == dest)
print('Star 1:', best)

visited = set()
def build_path(prev, dest):
    q = deque([dest])
    while q:
        cur = q.popleft()
        visited.add(cur.pos)
        q.extend(prev[cur])
for k, v in dist.items():
    if k.pos == dest and v == best:
        build_path(prev, k)
print('Star 2:', len(visited))