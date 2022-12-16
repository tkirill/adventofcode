from aoc import *
from collections import defaultdict
import itertools as itls
import re


def read_input():
    start = defaultdict(list)
    valves = dict()
    for l in readlines():
        v, r = re.search(r'Valve (..) has flow rate=(\d+)', l).groups()
        ns = re.split(r'to valve[s]? ', l)[-1].split(', ')
        start[v] = ns
        valves[v] = int(r)
    return start, valves


def collapse_zeroes(cave, valves) -> dict[list[tuple[str, int]]]:
    result = defaultdict(list)
    for v, f in valves.items():
        if f > 0 or v == 'AA':
            for o, d in bfs(v, cave.get):
                if v != o and valves[o] > 0:
                    result[v].append((o, d))
    return result


def score(path: dict[str, int], budget: int):
    return sum(valves[v] * (budget-t) for v, t in path.items())


def getmask(path: dict[str, int]):
    result = 0
    for v in path:
        result |= masks[v]
    return result


cave, valves = read_input()
cave2 = collapse_zeroes(cave, valves)
masks = {k: 1 << i for i, k in enumerate(cave2)}


dp = {}
def findmax(cur: str, curtime: int, path: dict[str, int], budget: int):
    mask, s = getmask(path), score(path, budget)
    cached = dp.get(mask, 0)
    if cached < s:
        dp[mask] = s
    for n, dist in cave2[cur]:
        if curtime + dist + 1 <= budget and n not in path:
            path[n] = curtime + dist + 1
            findmax(n, curtime + dist + 1, path, budget)
            del path[n]


findmax('AA', 0, {}, 30)
print('Star 1:', max(dp.values()))
dp.clear()
findmax('AA', 0, {}, 26)
print('Star 2:', max(s1[1] + s2[1] for s1, s2 in itls.combinations(dp.items(), 2) if not (s1[0] & s2[0])))