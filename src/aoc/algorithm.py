from typing import Iterable, Callable
from collections import deque
from itertools import islice
from aoc import pqueue


def filter_visited[TState](
        initial: Iterable[TState],
        near: Callable[[TState], Iterable[TState]]) -> Callable[[TState], Iterable[TState]]:
    visited = set(initial)

    def _near[TState](s: TState) -> Iterable[TState]:
        for n in near(s):
            if n not in visited:
                visited.add(n)
                yield n
    
    return _near


def bfs_initial[TState](
        initial: list[TState],
        near: Callable[[TState], Iterable[TState]],
        track_visited: bool=True) -> Iterable[tuple[TState, int]]:
    if track_visited:
        near = filter_visited(initial, near)
    yield from _bfs_impl(initial, near)


def bfs[TState](
        initial: TState,
        near: Callable[[TState], Iterable[TState]],
        track_visited: bool=True):
    yield from bfs_initial([initial], near, track_visited)


def _bfs_impl[TState](
        initial: Iterable[TState],
        near: Callable[[TState], Iterable[TState]]) -> Iterable[tuple[TState, int]]:
    q = deque(initial)
    curdist = 0
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            yield cur, curdist
            q.extend(near(cur))
        curdist += 1


def find_cycle[TValue](values: Iterable[TValue]) -> tuple[TValue, int, int]:
    seen = {}
    for i, v in enumerate(values):
        prev = seen.setdefault(v, i)
        if prev != i:
            return v, prev, i


def nth_with_cycle[TValue](values: Iterable[TValue], n: int) -> TValue:
    seen = {}
    it = iter(values)
    for i, v in enumerate(it):
        if i == n:
            return v
        prev = seen.setdefault(v, i)
        if prev != i:
            nn = (n - i) % (i - prev)
            if not nn:
                return v
            return next(islice(it, nn-1, nn))


def dijkstra[TNode](
        start: TNode,
        near: Callable[[TNode], Iterable[tuple[TNode, int]]]
        ) -> Iterable[tuple[TNode, int]]:
    return dijkstra_initial([start], near)


def dijkstra_initial[TNode](
        initial: list[TNode],
        near: Callable[[TNode], Iterable[tuple[TNode, int]]]
        ) -> Iterable[tuple[TNode, int]]:
    dist = {s: 0 for s in initial}
    prev = {s: None for s in initial}
    q = pqueue.PriorityQueue(dist.items())
    
    while q:
        u = q.pop()
        udist = dist[u]
        yield u, udist
        for v, cost in near(u):
            alt = udist + cost
            vdist = dist.get(v, None)
            if vdist is None or vdist > alt:
                dist[v] = alt
                prev[v] = u
                q.add(v, alt)
