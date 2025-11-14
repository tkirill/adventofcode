from aoc.io import *
import itertools as itls
import math


moves, map = readblocks(sep="[ =,()]+")
moves = moves[0]
adj = {}
for src, dst1, dst2 in map:
    adj[src] = dst1, dst2


def walk(start):
    cur = start
    for step in itls.cycle((moves)):
        yield cur
        cur = adj[cur][0 if step == "L" else 1]
    yield cur


def get_period(start):
    for i, cur in enumerate(walk(start)):
        if cur[-1] == "Z":
            return i


print("Star 1:", next(i for i, x in enumerate(walk("AAA")) if x == "ZZZ"))
starts = [x for x in adj.keys() if x[-1] == "A"]
periods = [get_period(x) for x in starts]
print("Star 2:", math.lcm(*periods))
