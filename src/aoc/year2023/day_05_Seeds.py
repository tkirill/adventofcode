from itertools import batched
from typing import Iterable

from aoc.io import readblocks, allints
from aoc.interval import Interval
from aoc import interval


def read_maps() -> tuple[list[int], list[list[tuple[Interval, Interval]]]]:
    seeds, *map_blocks = readblocks(2023, 5, sep=None, parse=allints)
    maps = []
    for _, *block_intervals in map_blocks:
        cur = [(interval.of_length(src, _len), interval.of_length(dst, _len)) for dst, src, _len in block_intervals]
        cur.sort(key=lambda t: t[0].begin)
        maps.append(cur)
    return seeds[0], maps


def map_interval(seed: Interval, _map: list[tuple[Interval, Interval]]) -> Iterable[Interval]:
    cur = seed
    for src, dst in _map:
        overlap = cur & src
        if not overlap:
            continue
        shift = dst.begin - src.begin
        yield Interval(overlap.begin + shift, overlap.end + shift)
        if cur.begin < overlap.begin:
            yield Interval(cur.begin, overlap.begin-1)
        cur = Interval(overlap.end+1, cur.end)
    if cur:
        yield cur


def map_lowest_location(seed: Interval, maps: list[list[tuple[Interval, Interval]]]) -> int:
    if len(maps) == 1:
        return min(i.begin for i in map_interval(seed, maps[0]))
    return min(map_lowest_location(i, maps[1:]) for i in map_interval(seed, maps[0]))


def star1():
    seeds, maps = read_maps()
    return min(map_lowest_location(interval.degenerate(s), maps) for s in seeds)


def star2():
    seeds, maps = read_maps()
    return min(map_lowest_location(interval.of_length(s, _len), maps) for s, _len in batched(seeds, 2))
