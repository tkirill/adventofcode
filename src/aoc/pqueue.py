from heapq import heappush, heappop
from typing import Iterable
import itertools


REMOVED = '<removed-task>'


class PriorityQueue[TValue]:

    pq: list[TValue]
    entry_finder: dict[tuple[int, int, TValue]]
    counter: Iterable[int]
    length: int

    def __init__(self, items: Iterable[tuple[TValue, int]]):
        self.pq = []
        self.entry_finder = dict()
        self.counter = itertools.count()
        self.length = 0
        for i, d in items:
            self.add(i, d)

    def add(self, task: TValue, priority: int=0):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            del self[task]
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)
        self.length += 1

    def __delitem__(self, task: TValue):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = REMOVED
        self.length -= 1
    
    def __len__(self) -> int:
        return self.length
    
    def __bool__(self) -> bool:
        return bool(self.length)

    def pop(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            _, _, task = heappop(self.pq)
            if task is not REMOVED:
                self.length -= 1
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')