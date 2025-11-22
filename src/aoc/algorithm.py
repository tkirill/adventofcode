from typing import Iterable, Callable
from collections import deque


def bfs_initial[TState](initial: Iterable[TState], near: Callable[[TState], Iterable[TState]], track_visited: bool=True):
    q = deque(initial)
    visited = set(q) if track_visited else None
    curdist = 0
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            yield cur, curdist
            for n in near(cur):
                if not track_visited or n not in visited:
                    q.append(n)
                    if track_visited:
                        visited.add(n)
        curdist += 1
    