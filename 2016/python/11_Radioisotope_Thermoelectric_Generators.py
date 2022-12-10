from __future__ import annotations
from aoc import *
from typing import NamedTuple, Optional
from itertools import combinations


class Thing(NamedTuple):
    is_chip: bool
    element: str

    def as_generator(self):
        return Thing(False, self.element) if self.is_chip else self


class ThingList(NamedTuple):
    elements: tuple[Thing, ...]

    def is_stable(self) -> bool:
        generators = set(x for x in self.elements if not x.is_chip)
        return not generators or all(x.as_generator() in generators for x in self.elements if x.is_chip)
    
    def extract(self, ns: Iterable[int]) -> tuple[ThingList, ThingList]:
        tmp = list(self.elements)
        items = [tmp.pop(n) for n in sorted(ns, reverse=True)]
        return ThingList.from_iterable(items), ThingList.from_iterable(tmp)
    
    def neighbors(self) -> Iterable[tuple[ThingList, ThingList]]:
        for len_ in [1, 2]:
            for ns in combinations(range(len(self.elements)), len_):
                items, nxt = self.extract(ns)
                if items.is_stable() and nxt.is_stable():
                    yield items, nxt
    
    def add(self, items: ThingList) -> ThingList:
        tmp = list(self.elements)
        tmp.extend(items.elements)
        return ThingList.from_iterable(tmp)
    
    @classmethod
    def from_iterable(cls, elements: Iterable[Thing]) -> ThingList:
        return ThingList(tuple(sorted(elements)))


class State(NamedTuple):
    floors: tuple[ThingList, ...]
    elevator: int

    def set_floors(self, n1, nxt1, n2, nxt2):
        tmp = list(self.floors)
        tmp[n1] = nxt1
        tmp[n2] = nxt2
        return State.from_iterable(tmp, n2)

    def neighbors(self) -> Iterable[State]:
        from_floor = self.floors[self.elevator]
        for items, nxt_from_floor in from_floor.neighbors():
            if self.elevator > 0:
                tmp = self.floors[self.elevator-1].add(items)
                if tmp.is_stable():
                    yield self.set_floors(self.elevator, nxt_from_floor, self.elevator-1, tmp)
            if self.elevator < len(self.floors)-1:
                tmp = self.floors[self.elevator+1].add(items)
                if tmp.is_stable():
                    yield self.set_floors(self.elevator, nxt_from_floor, self.elevator+1, tmp)
    
    @classmethod
    def from_iterable(cls, floors: Iterable[ThingList], elevator: int) -> State:
        return State(tuple(floors), elevator)


ELEMENTS = ['thulium', 'plutonium', 'strontium', 'promethium', 'ruthenium']
ALL_CHIPS = [Thing(True, x) for x in ELEMENTS]
ALL_GENERATORS = [Thing(False, x) for x in ELEMENTS]
END = State.from_iterable([
    ThingList.from_iterable([]),
    ThingList.from_iterable([]),
    ThingList.from_iterable([]),
    ThingList.from_iterable(ALL_CHIPS + ALL_GENERATORS)
], 3)
START_FLOORS = [
    [Thing(False, 'thulium'), Thing(True, 'thulium'), Thing(False, 'plutonium'), Thing(False, 'strontium')],
    [Thing(True, 'plutonium'), Thing(True, 'strontium')],
    [Thing(False, 'promethium'), Thing(True, 'promethium'), Thing(False, 'ruthenium'), Thing(True, 'ruthenium')],
    []
]
START = State.from_iterable((ThingList.from_iterable(x) for x in START_FLOORS), 0)


def findmindist(start: State):
    q = [start]
    visited = {start}
    curdist = 0
    while q:
        nxt = list(q)
        q.clear()
        curdist += 1
        for cur in nxt:
            for n in cur.neighbors():
                if n == END:
                    return curdist
                if n not in visited:
                    visited.add(n)
                    q.append(n)


print('Star 1:', findmindist(START))
ELEMENTS.extend(['elerium', 'dilithium'])
ALL_CHIPS = [Thing(True, x) for x in ELEMENTS]
ALL_GENERATORS = [Thing(False, x) for x in ELEMENTS]
END = State.from_iterable([
    ThingList.from_iterable([]),
    ThingList.from_iterable([]),
    ThingList.from_iterable([]),
    ThingList.from_iterable(ALL_CHIPS + ALL_GENERATORS)
], 3)
START_FLOORS[0].extend([Thing(False, 'elerium'), Thing(True, 'elerium'), Thing(False, 'dilithium'), Thing(True, 'dilithium')])
START = State.from_iterable((ThingList.from_iterable(x) for x in START_FLOORS), 0)
print('Star 2:', findmindist(START))