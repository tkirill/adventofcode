from aoc.io import *
from aoc.primitives import *
from aoc import grid
from collections import Counter, deque
from more_itertools import flatten, nth, ilen
from itertools import takewhile


def read_elves():
    elves = set()
    for y, row in enumerate(readlines()):
        for x, c in enumerate(row):
            if c == '#':
                elves.add(Vec2(x, y))
    return elves


def round(elves: set[Vec2], directions: list[str]):
    nears = Counter(flatten(grid.screen.near8(e) for e in elves))

    def propose_move(elf: Vec2):
        if elf not in nears:
            return elf
        for d in directions:
            if all(n not in elves for n in grid.screen.side(elf, d)):
                return grid.screen.step(elf, d)
        return elf

    moves = {e: propose_move(e) for e in elves}
    count_moves = Counter(moves.values())

    nxt_elves = set()
    top_left, bottom_right = None, None
    moved = 0
    for elf, nxt_elf in moves.items():
        tmp = nxt_elf if count_moves[nxt_elf] == 1 else elf
        moved += tmp != elf
        nxt_elves.add(tmp)
        top_left = Vec2(min(top_left.x, tmp.x), min(top_left.y, tmp.y)) if top_left is not None else tmp
        bottom_right = Vec2(max(bottom_right.x, tmp.x), max(bottom_right.y, tmp.y)) if bottom_right is not None else tmp
    return nxt_elves, top_left, bottom_right, moved

def simulate(elves):
    cur = elves
    dirs_cycle = deque('NSWE')
    while True:
        cur, tl, br, moved = round(cur, dirs_cycle)
        yield cur, tl, br, moved
        dirs_cycle.rotate(-1)


def printelves(elves, tl, br):
    for y in range(tl.y, br.y+1):
        s = []
        for x in range(tl.x, br.x+1):
            s.append('#' if Vec2(x, y) in elves else '.')
        print(''.join(s))



elves = read_elves()
cur, tl, br, moved = nth(simulate(elves), 9)
print('Star 1:', (br.y - tl.y + 1) * (br.x - tl.x + 1) - len(cur))
print('Star 2:', ilen(takewhile(lambda r: r[-1] > 0, simulate(elves)))+1)