from typing import Iterable, Callable
from collections import deque


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
        initial: list[TState],
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
