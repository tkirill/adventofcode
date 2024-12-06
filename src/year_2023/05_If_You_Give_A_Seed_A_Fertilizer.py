from aoc.io import *
from aoc.primitives import *
import more_itertools as mitls


blocks = readblocks()
maps = []
for b in blocks[1:]:
    maps.append([])
    for dst, src, ll in b[1:]:
        maps[-1].append((Range.lw(src, ll), dst - src))
    maps[-1].sort()


def find_lowest_location(seeds) -> int:
    for m in maps:
        nxt = []
        for r in seeds:
            for src, shift in m:
                i = r.intersect(src).shift(shift)
                if len(i) > 0:
                    nxt.append(i)
            nxt.extend(r.difference_many(src for src, _ in m))
        seeds = nxt
    return min(x.start for x in seeds)


seeds = [Range.lw(x, 1) for x in blocks[0][0][1:]]
print("Star 1:", find_lowest_location(seeds))
seeds = [Range.lw(x, y) for x, y in mitls.chunked(blocks[0][0][1:], 2)]
print("Star 2:", find_lowest_location(seeds))
