from __future__ import annotations
from aoc.io import *
from aoc.primitives import *
from aoc.grid import *
from aoc.algo import callchain, bfs
from aoc import grid
from typing import NamedTuple
import dataclasses
from itertools import islice


class Blizzard(NamedTuple):
    pos: Vec2
    dir: Vec2


class State(NamedTuple):
    pos: Vec2
    time: int
    exit_visited: bool = False
    entry_visited_again: bool = False

    def near(self):
        bpos = blizzard_cache[self.time+1]
        exit_visited = self.exit_visited or self.pos == exit_
        entry_visited_again = self.entry_visited_again or self.exit_visited and self.pos == entry
        for n in grid.near4(screen, self.pos):
            if (n == entry or n == exit_) or 1 <= n.x <= field.w-2 and 1 <= n.y <= field.h-2 and n not in bpos:
                yield State(n, self.time+1, exit_visited, entry_visited_again)
        if self.pos not in bpos:
            yield State(self.pos, self.time+1, exit_visited, entry_visited_again)
    
    def print(self):
        for y in range(field.h):
            row = []
            for x in range(field.w):
                tmp = Vec2(x, y)
                if tmp == self.pos:
                    row.append('0')
                elif tmp == entry or tmp == exit_:
                    row.append('.')
                elif x == 0 or y == 0 or x == field.w-1 or y == field.h-1:
                    row.append('#')
                elif any(b.pos == tmp for b in self.blizzards):
                    row.append('W')
                else:
                    row.append('.')
            print(''.join(row))
                


BDIRS = {
    'v': Vec2(0, 1),
    '^': Vec2(0, -1),
    '>': Vec2(1, 0),
    '<': Vec2(-1, 0)
}


def read_input():
    field = Field(read(sep='None'))
    blizzards = []
    for pos, v in field.cellsv():
        if pos.y == 0 and v == '.':
            entry = pos
        elif pos.y == field.h-1 and v == '.':
            exit_ = pos
        elif v != '.' and v != '#':
            blizzards.append(Blizzard(pos, BDIRS[v]))
    return field, blizzards, entry, exit_


def move_blizzards(blizzards: list[Blizzard]) -> list[Blizzard]:
    result = []
    for b in blizzards:
        nxt = b.pos + b.dir
        if nxt.x == 0:
            nxt = dataclasses.replace(nxt, x=field.w-2)
        elif nxt.x == field.w-1:
            nxt = dataclasses.replace(nxt, x=1)
        elif nxt.y == 0:
            nxt = dataclasses.replace(nxt, y=field.h-2)
        elif nxt.y == field.h-1:
            nxt = dataclasses.replace(nxt, y=1)
        result.append(b._replace(pos=nxt))
    return result


def calc_blizzards(blizzards) -> Iterable[set[Vec2]]:
    for cur in callchain(move_blizzards, blizzards, yield_init=True):
        yield set(b.pos for b in cur)

        
field, blizzards, entry, exit_ = read_input()
blizzard_cache = list(islice(calc_blizzards(blizzards), 1000))

start = State(entry, 0, False)
part1 = False
for state, dist in bfs(start, lambda x: x.near()):
    if state.pos == exit_ and not part1:
        print('Star 1:', dist)
        part1 = True
    elif state.pos == exit_ and state.entry_visited_again:
        print('Star 2:', dist)
        break