from collections.abc import Sequence, Callable, Iterable, Hashable
from more_itertools import nth
from pqdict import pqdict

def transpose[TValue](s: Sequence[Sequence[TValue]]) -> list[list[TValue]]:
    result = []
    if not s:
        return result
    for c in range(len(s[0])):
        result.append([row[c] for row in s])
    return result


def callchain[TResult](func: Callable[[TResult], TResult], init: TResult, yield_init=False) -> Iterable[TResult]:
    cur = init
    if yield_init:
        yield cur
    while True:
        cur = func(cur)
        yield cur


def detect_cycle(items: Iterable[Hashable]) -> tuple[int, int]:
    mem = {}
    pos = 0
    for cur in items:
        prev = mem.setdefault(cur, pos)
        if prev != pos:
            return prev, pos-prev
        pos += 1


def nth_with_cycle[TValue](items: Iterable[TValue], at: int) -> TValue:
    it = iter(items)
    mem = {}
    pos = 0
    for cur in it:
        if pos == at:
            return cur
        prev = mem.setdefault(cur, pos)
        if prev != pos:
            start, size = prev, pos-prev
            adjusted = (at-start) % size
            if not adjusted:
                return cur
            return nth(it, adjusted-1)
        pos += 1


def bfs[TValue](start: TValue, near: Callable[[TValue], Iterable[TValue]]):
    q = [start]
    visited = {start}
    curdist = 0
    while q:
        qcopy = list(q)
        q.clear()
        for cur in qcopy:
            yield cur, curdist
            for n in near(cur):
                if n not in visited:
                    q.append(n)
                    visited.add(n)
        curdist += 1


def dijkstra[TValue](
    start: TValue | Iterable[TValue],
    near: Callable[[TValue], Iterable[tuple[TValue, int]]],
):
    if isinstance(start, Iterable):
        dist = {s: 0 for s in start}
        prev = {s: None for s in start}
    else:
        dist = {start: 0}
        prev = {start: None}
    q = pqdict(dist)

    while q:
        cur = q.pop()
        for n, ndist in near(cur):
            alt = dist[cur] + ndist
            ex = dist.get(n)
            if ex is None or ex > alt:
                dist[n] = alt
                q[n] = alt
                prev[n] = cur
    return dist, prev