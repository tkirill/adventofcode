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


def scanl[TResult, TValue](func: Callable[[TResult, TValue], TResult], init: TResult, values: Iterable[TValue]) -> Iterable[TResult]:
    yield init
    cur = init
    for s in values:
        cur = func(cur, s)
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


def bfs[TValue](start: TValue, near: Callable[[TValue], Iterable[TValue]], track_visited: bool=True):
    q = [start]
    visited = {start}
    curdist = 0
    while q:
        qcopy = list(q)
        q.clear()
        for cur in qcopy:
            yield cur, curdist
            for n in near(cur):
                if not track_visited or n not in visited:
                    q.append(n)
                    if track_visited:
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


def asciipos(c):
    return ord(c) - ord('a' if c.islower() else 'A')


def orddiff(a, b):
    return ord(b) - ord(a)


def display2d(arr2d: list[list], true_val=None):
    for row in arr2d:
        print(''.join('#' if (true_val is not None and v==true_val) or (true_val is None and v) else '.' for v in row))