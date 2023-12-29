from aoc import *


def near1(
    island: Field(read(parse=list)), cur: tuple[Walker2d, int]
) -> Iterable[tuple[Walker2d, int]]:
    for r in "LR":
        nxt = cur[0].rotatelr(r).step()
        if nxt.pos in island:
            yield (nxt, 1), island[nxt.pos]
    if cur[1] < 3:
        nxt = cur[0].step()
        if nxt.pos in island:
            yield (nxt, cur[1] + 1), island[nxt.pos]


def near2(
    island: Field(read(parse=list)), cur: tuple[Walker2d, int]
) -> Iterable[tuple[Walker2d, int]]:
    if cur[1] >= 4:
        for r in "LR":
            total = 0
            nxt = cur[0].rotatelr(r)
            for _ in range(4):
                nxt = nxt.step()
                if nxt.pos not in island:
                    break
                total += island[nxt.pos]
            else:
                yield (nxt, 4), total
    if cur[1] < 10:
        nxt = cur[0].step()
        if nxt.pos in island:
            yield (nxt, cur[1] + 1), island[nxt.pos]


island = Field([[int(c) for c in l] for l in readlines()])
start = [(Walker2d(dir=d), 0) for d in [Vec2(1, 0), Vec2(0, 1)]]
dist, prev = dijkstra(start, lambda c: near1(island, c))
print(
    "Star 1:",
    min(v for k, v in dist.items() if k[0].pos == Vec2(island.w - 1, island.h - 1)),
)

dist, prev = dijkstra(start, lambda c: near2(island, c))
print(
    "Star 2:",
    min(
        v
        for k, v in dist.items()
        if k[1] >= 4 and k[0].pos == Vec2(island.w - 1, island.h - 1)
    ),
)
