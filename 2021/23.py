from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any
import itertools
from heapq import heappush, heappop

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')

HALL = list(range(len('...........')))
COR1 = [101, 102]
COR2 = [103, 104]
COR3 = [105, 106]
COR4 = [107, 108]
CORS = COR1 + COR2 + COR3 + COR4

G = defaultdict(list)
for i in HALL[1:]:
    G[i].append(i-1)
    G[i-1].append(i)

for x, y in [(COR1[0], HALL[2]), (COR2[0], HALL[4]), (COR3[0], HALL[6]), (COR4[0], HALL[8])]:
    G[x].append(y)
    G[y].append(x)
for x, y in [COR1, COR2, COR3, COR4]:
    G[x].append(y)
    G[y].append(x)
DST = [COR1, COR1, COR2, COR2, COR3, COR3, COR4, COR4]
state = (COR1[0], COR2[1], COR1[1], COR3[0], COR2[0], COR4[1], COR3[1], COR4[0])


def is_final(state):
    return all(pos in DST[i] for i, pos in enumerate(state))


def moves(state, at, n):
    visited = {state[n]}
    q = {state[n]}
    dist = 0
    while q:
        dist += 1
        nq = []
        for cur in q:
            for nxt in G[cur]:
                if nxt not in visited and nxt not in at:
                    yield nxt, dist
                    nq.append(nxt)
                    visited.add(nxt)
        q = nq


def step(state):
    at = {pos: n for n, pos in enumerate(state)}
    for n, pos in enumerate(state):
        if pos == DST[n][1] or pos == DST[n][0] and at[DST[n][1]] // 2 == n // 2:
            # already at the correct room
            continue
        if pos in HALL:
            room = [at.get(x) for x in DST[n]]
            if any(x is not None and x // 2 != n // 2 for x in room):
                continue
        for npos, dist in moves(state, at, n):
            if npos == DST[n][1] or npos == DST[n][0] and at.get(DST[n][1], 777) // 2 == n // 2 \
                or pos in CORS and npos in HALL and npos not in [HALL[2], HALL[4], HALL[6], HALL[8]]:
                tmp = list(state)
                tmp[n] = npos
                yield tuple(tmp), dist*10**(n // 2)


def main():
    dist = defaultdict(lambda: 1000*1000*1000*1000)
    dist[state] = 0
    mindist = 1000*1000*1000*1000
    add_task(state, 0)
    while pq:
        cur = pop_task()
        for nstate, w in step(cur):
            alt = dist[cur] + w
            if alt < dist[nstate]:
                dist[nstate] = alt
                add_task(nstate, alt)
                if is_final(nstate) and alt < mindist:
                    mindist = alt

    print('Star 1:', mindist)


import timeit
print(timeit.timeit('main()', globals=globals(), number=1))