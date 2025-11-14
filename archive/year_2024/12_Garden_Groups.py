from aoc.io import *
from aoc.grid import *
from aoc.primitives import *
import itertools as itls


garden = Field(readlines())
blocks = []
visited = set()
for pos in garden.cells():
    if pos in visited:
        continue
    b = [p for p, _ in garden.bfs4(pos, lambda p1, p2: garden[p1] == garden[p2])]
    blocks.append(b)
    visited.update(b)

def price(b):
    p = [p for x in b for p in garden.grid.near4(x) if p not in garden or garden[p] != garden[x]]
    return len(b) * len(p)

print('Star 1:', sum(price(b) for b in blocks))


pos_to_block = {p: i for i, b in enumerate(blocks) for p in b}
sides = [0] * len(blocks)

def count_sides(rowsv: Iterable[Tuple[Vec2, str]], get_sides: Callable[[Vec2], Tuple[Vec2, Vec2]]):
    for row in rowsv:
        for _, g in itls.groupby(row, key=lambda x: x[1]):
            b = list(g)
            ups, downs = [], []
            for pos, v in b:
                u, d = get_sides(pos)
                ups.append(u not in garden or garden[u] != v)
                downs.append(d not in garden or garden[d] != v)
            block = pos_to_block[b[0][0]]
            sides[block] += sum(1 for sk, _ in itls.groupby(ups) if sk)
            sides[block] += sum(1 for sk, _ in itls.groupby(downs) if sk)

count_sides(garden.rowsv(), lambda x: (garden.grid.up(x), garden.grid.down(x)))
count_sides(garden.columnsv(), lambda x: (garden.grid.left(x), garden.grid.right(x)))
print('Star 2:', sum(len(b) * sides[i] for i, b in enumerate(blocks)))