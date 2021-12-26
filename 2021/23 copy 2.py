from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any
import itertools
from heapq import heappush, heappop

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
COR1 = [101, 102, 201, 202]
COR2 = [103, 104, 203, 204]
COR3 = [105, 106, 205, 206]
COR4 = [107, 108, 207, 208]
CORS = COR1 + COR2 + COR3 + COR4

G = defaultdict(list)
for i in HALL[1:]:
    G[i].append(i-1)
    G[i-1].append(i)

for x, y in [(COR1[0], HALL[2]), (COR2[0], HALL[4]), (COR3[0], HALL[6]), (COR4[0], HALL[8])]:
    G[x].append(y)
    G[y].append(x)
for cor in [COR1, COR2, COR3, COR4]:
    for i in range(1, len(cor)):
        G[cor[i]].append(cor[i-1])
        G[cor[i-1]].append(cor[i])
DST = [COR1, COR1, COR1, COR1, COR2, COR2, COR2, COR2, COR3, COR3, COR3, COR3, COR4, COR4, COR4, COR4]

#############
#...........#
###A#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #B#A#D#C#
  #########

state = (
    COR1[0], COR2[3], COR3[2], COR4[1],
    COR1[3], COR2[2], COR3[0], COR3[1],
    COR2[0], COR2[1], COR4[2], COR4[3],
    COR1[1], COR1[2], COR3[3], COR4[0])


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


def get_room_pos(at, n):
    for pos in reversed(DST[n]):
        x = at.get(pos)
        if x is None:
            return pos
        if x // 4 != n // 4:
            return None


def step(state):
    at = {pos: n for n, pos in enumerate(state)}
    for n, pos in enumerate(state):
        if pos in DST[n] and all(x not in at or at[x] // 4 == n // 4 for x in DST[n]):
            # already at the correct room
            continue
        for npos, dist in moves(state, at, n):
            if npos == get_room_pos(at, n) \
                or pos in CORS and npos in HALL and npos not in [HALL[2], HALL[4], HALL[6], HALL[8]]:
                tmp = list(state)
                tmp[n] = npos
                yield tuple(tmp), dist*10**(n // 4)


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
                # print(cur, nstate)
                dist[nstate] = alt
                add_task(nstate, alt)
                if is_final(nstate) and alt < mindist:
                    mindist = alt

    print('Star 1:', mindist)


import timeit
print(timeit.timeit('main()', globals=globals(), number=1))