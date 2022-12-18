from __future__ import annotations
from aoc import *
import re
import math
import string
import itertools as itls
import more_itertools as mtls
from collections import Counter, defaultdict, namedtuple
from functools import cache
from pprint import pprint


class Rock(NamedTuple):
    parts: list[Vec2]

    def down(self) -> Rock:
        return Rock([x.down() for x in self.parts])
    
    def side(self, s: str):
        if s == '<':
            return Rock([x.left() for x in self.parts])
        return Rock([x.right() for x in self.parts])
    
    def adjust(self, d: Vec2) -> Rock:
        return Rock([x + d for x in self.parts])


@dataclass
class Cave:
    w: int
    h: int
    cells: set[Vec2]
    jetmoves: Iterable[str]

    def is_ok(self, rock: Rock) -> bool:
        return all(0 < r.x <= self.w and 0 < r.y and r not in self.cells for r in rock.parts)
    
    def splithalf(self) -> tuple[set, set]:
        assert self.h % 2 == 0
        half = self.h // 2
        delta = Vec2(-half, 0, 1)
        s1, s2 = set(), set()
        for v in self.cells:
            if v.y <= half:
                s1.add(v)
            else:
                s2.add(v-delta)
        return s1, s2


    def throw(self, rock: Rock):
        cur = rock

        while True:
            nxt = cur.side(next(self.jetmoves))
            if self.is_ok(nxt):
                cur = nxt
            nxt = cur.down()
            if self.is_ok(nxt):
                cur = nxt
            else:
                self.cells.update(cur.parts)
                self.h = max(self.h, max(v.y for v in cur.parts))
                return cur


def simulate1(n):
    cave = Cave(CAVEW, 0, set(), itls.cycle(JETMOVES))
    shapes = itls.cycle(SHAPES)
    for _ in range(n):
        r = next(shapes).adjust(INITDELTA + Vec2(0, cave.h, 1))
        cave.throw(r)
    return cave


def simulate2(n):
    cave = Cave(CAVEW, 0, set(), itls.cycle(JETMOVES))
    shapes = itls.cycle(SHAPES)
    for _ in range(INITIAL+REPEATING):
        r = next(shapes).adjust(INITDELTA + Vec2(0, cave.h, 1))
        cave.throw(r)
    init_h = cave.h
    for _ in range(REPEATING):
        r = next(shapes).adjust(INITDELTA + Vec2(0, cave.h, 1))
        cave.throw(r)
    repeating_h = cave.h - init_h
    curiter = INITIAL + REPEATING+REPEATING
    remiter = n - curiter
    total_h = cave.h + (remiter // REPEATING) * repeating_h
    remiter %= REPEATING
    for _ in range(remiter):
        r = next(shapes).adjust(INITDELTA + Vec2(0, cave.h, 1))
        cave.throw(r)
    return total_h + cave.h - init_h - repeating_h



JETMOVES = readraw()
SHAPES = [
    Rock([Vec2(i, 0, 1) for i in range(4)]),
    Rock([Vec2(1, 0, 1), Vec2(0, 1, 1), Vec2(1, 1, 1), Vec2(2, 1, 1), Vec2(1, 2, 1)]),
    Rock([Vec2(0, 0, 1), Vec2(1, 0, 1), Vec2(2, 0, 1), Vec2(2, 1, 1), Vec2(2, 2, 1)]),
    Rock([Vec2(0, i, 1) for i in range(4)]),
    Rock([Vec2(0, 0, 1), Vec2(1, 0, 1), Vec2(0, 1, 1), Vec2(1, 1, 1)])
]
INITDELTA = Vec2(3, 4, 1)
CAVEW = 7
ALPHABET = string.ascii_letters
INITIAL = 256
REPEATING = 1730
# INITIAL = 15
# REPEATING = 35

print('Star 1:', simulate1(2022).h)
print('Star 2:', simulate2(1000000000000))

def explore():
    lll = math.lcm(len(JETMOVES), len(SHAPES))
    print('JETMOVES:', len(JETMOVES), 'SHAPES', len(SHAPES), 'LCM:', lll)
    # cave = simulate1(lll*2)
    # halfh = cave.h // 2
    # print('cave H:', cave.h, 'half H:', halfh)
    # s1, s2 = cave.splithalf()
    # print('EQ?', s1 == s2)
    cave = Cave(CAVEW, 0, set(), itls.cycle(JETMOVES))
    shapes = itls.cycle(enumerate(SHAPES))
    path = []
    for _ in range(lll*3):
        i, r = next(shapes)
        r = r.adjust(INITDELTA + Vec2(0, cave.h, 1))
        f = cave.throw(r)
        c = ALPHABET[i * 8 + f.parts[0].x]
        path.append(c)
    spath = ''.join(path)
    open('o.txt', 'w').write(spath+'\n')
    for i in range(1000):
        if spath[i:i+100] in spath[i+100:]:
            print(i, spath[i:i+100])
            break


# explore()