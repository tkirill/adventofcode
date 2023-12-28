from __future__ import annotations
import __main__
from pathlib import Path
import re
from typing import Any, Iterable, TypeVar, Callable, Optional, NamedTuple, Hashable
from dataclasses import dataclass, field
from collections import deque
from itertools import takewhile, chain
from more_itertools import nth
import abc


TResult = TypeVar('TResult')
TValue = TypeVar('TValue')


###################
### Simple read ###
###################


def get_input_filename() -> Path:
    main = Path(__main__.__file__)
    n = re.match(r'\d\d', main.stem)
    input_filename = main.with_name(f'{n.group()}_input.txt')
    if not input_filename.exists():
        raise FileNotFoundError(str(input_filename))
    return input_filename


def readraw():
    input_filename = get_input_filename()
    with input_filename.open() as f:
        return f.read().strip()


def readlines() -> list[str]:
    input_filename = get_input_filename()
    with input_filename.open() as f:
        return [l.strip() for l in f]


def readsplit(sep='\s') -> list[list[str]]:
    return [re.split(sep, l) for l in readlines()]


def allints(s: str) -> list[int]:
    return [int(x.group()) for x in re.finditer(r'-?\d+', s)]


##################
### Smart read ###
##################


def parsevalue(s: str, parse=int) -> str | Any:
    try:
        return parse(s)
    except ValueError:
        return s


def parseline(l: str, sep=r'\s', parse=int) -> str | list[str | Any]:
    l = l.strip()
    if sep:
        parts = [parsevalue(s, parse=parse) for s in re.split(sep, l)]
        return parts[0] if len(parts) == 1 else parts
    return parsevalue(l, parse=parse)


def parselines(lines: list[str], sep=r'\s', parse=int) -> list[str | list[str | Any] | Any]:
    return [parseline(l, sep=sep, parse=parse) for l in lines]


def read(sep=r'\s', parse=int) -> list[str | list[str | Any]]:
    return [parseline(l, sep=sep, parse=parse) for l in readlines()]


def readblocks(sep=r'\s', parse=int):
    result = []
    tmp = []
    for l in readlines():
        if not l:
            result.append(tmp)
            tmp = []
        else:
            tmp.append(parseline(l, sep=sep, parse=parse))
    result.append(tmp)
    return result


#########################
### Text manipulation ###
#########################


def asciipos(c):
    return ord(c) - ord('a' if c.islower() else 'A')

def orddiff(a, b):
    return ord(b) - ord(a)


########################
### Sequence helpers ###
########################


def except_(it: Iterable, exclude):
    for a in it:
        if a != exclude:
            yield a


def circshift(arr: list, n: int) -> list:
    tmp = deque(arr)
    tmp.rotate(n)
    return list(tmp)


def callchain(func: Callable[[TResult], TResult], init: TResult, yield_init=False) -> Iterable[TResult]:
    cur = init
    if yield_init:
        yield cur
    while True:
        cur = func(cur)
        yield cur


def scanl(func: Callable[[TResult, TValue], TResult], init: TResult, values: Iterable[TValue]) -> Iterable[TResult]:
    yield init
    cur = init
    for s in values:
        cur = func(cur, s)
        yield cur


def min_and_max(s: Iterable[TValue]) -> tuple[TValue, TValue]:
    it = iter(s)
    vmin = next(it, None)
    vmax = vmin
    for v in it:
        vmin = min(vmin, v)
        vmax = max(vmax, v)
    return vmin, vmax


def detect_cycle(items: Iterable[Hashable]) -> tuple[int, int]:
    mem = {}
    pos = 0
    for cur in items:
        prev = mem.setdefault(cur, pos)
        if prev != pos:
            return prev, pos-prev
        pos += 1


def nth_with_cycle(items: Iterable[TValue], at: int) -> TValue:
    it = iter(items)
    mem = {}
    pos = 0
    for cur in it:
        if pos == at:
            return cur
        prev = mem.setdefault(cur, pos)
        if prev != pos:
            start, size = prev, pos-prev
            adjusted = (at-start) % size
            if not adjusted:
                return cur
            return nth(it, adjusted-1)
        pos += 1


##########################
### Arithmetic helpers ###
##########################


def sign(x: TValue) -> TValue:
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


##################
### 2d helpers ###
##################


@dataclass(frozen=True)
class ComplexWalker:
    pos: complex = 0
    dir: complex = 1j

    def step(self, v: int=1):
        return ComplexWalker(self.pos + self.dir * v, self.dir)
    
    def rotatelr(self, d: str):
        return ComplexWalker(self.pos, self.dir * (1j if d == 'R' else -1j))
    
    def walkall(self, steps: Iterable[tuple[str, int]]):
        cur = self
        for d, v in steps:
            cur = cur.rotatelr(d).step(v)
        return cur
    
    def walk(self, steps: Iterable[tuple[str, int]]):
        cur = self
        for d, v in steps:
            cur = cur.rotatelr(d).step(v)
            yield cur
    
    def walk_by1(self, steps: Iterable[tuple[str, int]]):
        cur = self
        for d, v in steps:
            cur = cur.rotatelr(d)
            for _ in range(v):
                cur = cur.step()
                yield cur
    
    def mdist(self):
        return abs(self.pos.real) + abs(self.pos.imag)


class Vec2(NamedTuple):
    x: int = 0
    y: int = 0
    ydir: int = -1

    def __add__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y, self.ydir)
        return Vec2(self.x + other, self.y + other, self.ydir)

    def __sub__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x - other.x, self.y - other.y, self.ydir)
        return Vec2(self.x - other, self.y - other, self.ydir)

    def __mul__(self, other):
        return Vec2(self.x * other, self.y * other, self.ydir)
    
    def __rmul__(self, other):
        return Vec2(self.x * other, self.y * other, self.ydir)
    
    def __truediv__(self, other):
        return Vec2(self.x / other, self.y / other, self.ydir)
    
    def __floordiv__(self, other):
        return Vec2(self.x // other, self.y // other, self.ydir)
    
    def __mod__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x % other.x, self.y % other.y, self.ydir)
        return Vec2(self.x % other, self.y % other, self.ydir)
    
    def __pow__(self, other):
        return Vec2(self.x ** other, self.y ** other, self.ydir)
    
    def __neg__(self):
        return Vec2(-self.x, -self.y, self.ydir)
    
    def __abs__(self):
        return Vec2(abs(self.x), abs(self.y), self.ydir)
    
    def rotatelr(self, r: str) -> Vec2:
        if self.ydir == 1:
            return Vec2(self.y, -self.x, self.ydir) if r == 'R' else Vec2(-self.y, self.x, self.ydir)
        return Vec2(-self.y, self.x, self.ydir) if r == 'R' else Vec2(self.y, -self.x, self.ydir)
    
    def mdist(self, other: Optional[Vec2]=None) -> int:
        if other is None:
            other = Vec2()
        return abs(self.x-other.x) + abs(self.y-other.y)
    
    def cdist(self, other: Optional[Vec2]=None) -> int:
        if other is None:
            other = Vec2()
        return max(abs(self.x-other.x), abs(self.y-other.y))
    
    def sign(self) -> Vec2:
        return Vec2(sign(self.x), sign(self.y))
    
    def up(self, dist=1) -> Vec2:
        return self + Vec2(0, self.ydir * dist)
    
    def down(self, dist=1) -> Vec2:
        return self - Vec2(0, self.ydir * dist)
    
    def left(self, dist=1) -> Vec2:
        return self - Vec2(dist, 0)
    
    def right(self, dist=1) -> Vec2:
        return self + Vec2(dist, 0)
    
    def up_left(self) -> Vec2:
        return self + Vec2(-1, self.ydir)
    
    def up_right(self) -> Vec2:
        return self + Vec2(1, self.ydir)
    
    def down_left(self) -> Vec2:
        return self + Vec2(-1, -self.ydir)
    
    def down_right(self) -> Vec2:
        return self + Vec2(1, -self.ydir)
    
    def step(self, dir: str, dist=1) -> Vec2:
        match(dir):
            case 'L' | 'W': return self.left(dist)
            case 'R' | 'E': return self.right(dist)
            case 'U' | 'N': return self.up(dist)
            case 'D' | 'S': return self.down(dist)
    
    def beam_left(self) -> Iterable[Vec2]:
        return callchain(lambda x: x.left(), self)
    
    def beam_right(self) -> Iterable[Vec2]:
        return callchain(lambda x: x.right(), self)
    
    def beam_up(self) -> Iterable[Vec2]:
        return callchain(lambda x: x.up(), self)
    
    def beam_down(self) -> Iterable[Vec2]:
        return callchain(lambda x: x.down(), self)
    
    def beams4(self) -> list[Iterable[Vec2]]:
        return [self.beam_up(), self.beam_right(), self.beam_down(), self.beam_left()]
    
    def is_in_field(self, w: int , h: int) -> bool:
        return 0 <= self.x < w and 0 <= self.y < h
    
    def line_to(self, other: Vec2) -> Iterable[Vec2]:
        cur, delta = self, (other-self).sign()
        while cur != other:
            yield cur
            cur += delta
        yield cur
    
    def near4(self) -> Iterable[Vec2]:
        yield self.up()
        yield self.right()
        yield self.down()
        yield self.left()
    
    def near5(self) -> Iterable[Vec2]:
        yield from self.near4()
        yield self
    
    def near8(self) -> Iterable[Vec2]:
        yield from self.near4()
        yield self.up_left()
        yield self.up_right()
        yield self.down_right()
        yield self.down_left()
    
    def near9(self) -> Iterable[Vec2]:
        yield from self.near8()
        yield self
    
    def side_up(self) -> Iterable[Vec2]:
        yield self.up_left()
        yield self.up()
        yield self.up_right()
    
    def side_right(self) -> Iterable[Vec2]:
        yield self.up_right()
        yield self.right()
        yield self.down_right()
    
    def side_down(self) -> Iterable[Vec2]:
        yield self.down_left()
        yield self.down()
        yield self.down_right()
    
    def side_left(self) -> Iterable[Vec2]:
        yield self.down_left()
        yield self.left()
        yield self.up_left()
    
    def side(self, side: str) -> Iterable[Vec2]:
        match side:
            case 'U' | 'N': return self.side_up()
            case 'R' | 'E': return self.side_right()
            case 'D' | 'S': return self.side_down()
            case 'L' | 'W': return self.side_left()
    
    def bfs(self, near: Callable[[Vec2], Iterable[Vec2]]):
        yield from bfs(self, near)


class Vec3(NamedTuple):
    x: int = 0
    y: int = 0
    z: int = 0

    def up(self):
        return Vec3(self.x, self.y-1, self.z)
    
    def down(self):
        return Vec3(self.x, self.y+1, self.z)
    
    def left(self):
        return Vec3(self.x-1, self.y, self.z)
    
    def right(self):
        return Vec3(self.x+1, self.y, self.z)
    
    def forward(self):
        return Vec3(self.x, self.y, self.z+1)
    
    def backward(self):
        return Vec3(self.x, self.y, self.z-1)
    
    def near6(self):
        yield self.up()
        yield self.down()
        yield self.left()
        yield self.right()
        yield self.forward()
        yield self.backward()


class NearABC(abc.ABC):

    def near8(self):
        ...


@dataclass
class Rectangle(NearABC):
    top_left: Vec2
    bottom_right: Vec2
    width: int | float = field(init=False)
    height: int | float = field(init=False)

    def near8(self) -> Iterable[Vec2]:
        for y in range(self.top_left.y-1, self.bottom_right.y + 2):
            for x in range(self.top_left.x-1, self.bottom_right.x + 2):
                yield Vec2(x, y)
    
    @classmethod
    def xywh(cls, x: int, y: int, w: int, h: int) -> Rectangle:
        return Rectangle(Vec2(x, y), Vec2(x + w, y + h))
    
    @classmethod
    def ylr(cls, y: int, l: int, r: int) -> Rectangle:
        return Rectangle(Vec2(l, y), Vec2(r, y))


@dataclass(frozen=True, order=True)
class Range:
    start: int
    end: int
    
    def intersect(self, other: Range) -> Range:
        return Range(max(self.start, other.start), min(self.end, other.end))
    
    def difference_many(self, others: Iterable[Range]) -> Iterable[Range]:
        cur = self.start
        for o in sorted(others):
            if o.start >= self.end:
                break
            if o.start > cur:
                yield Range(cur, o.start)
            cur = max(cur, o.end)
        if self.start <= cur < self.end:
            yield Range(cur, self.end)
    
    def shift(self, delta: int) -> Range:
        return Range(self.start + delta, self.end + delta)
    
    def __len__(self):
        return max(self.end - self.start + 1, 0)
    
    def __contains__(self, x: int) -> bool:
        return self.start <= x <= self.end

    @classmethod
    def lw(cls, l, w) -> Range:
        return Range(l, l+w)


class Field:

    def __init__(self, arr: list[list[TValue]]):
        self.arr = arr
        self.w = len(arr[0])
        self.h = len(arr)
    
    def rows(self) -> Iterable[Iterable[Vec2]]:
        return (self.row(y) for y in range(self.h))
    
    def row(self, y: int) -> Iterable[Vec2]:
        return (Vec2(x, y) for x in range(self.w))
    
    def columns(self) -> Iterable[Iterable[Vec2]]:
        return (self.column(x) for x in range(self.w))
    
    def column(self, x: int) -> Iterable[Vec2]:
        return (Vec2(x, y) for y in range(self.h))
    
    def rowsv(self) -> Iterable[Iterable[tuple[Vec2, TValue]]]:
        return (self.rowv(y) for y in range(self.h))
    
    def rowv(self, y: int) -> Iterable[tuple[Vec2, TValue]]:
        return self.getmany(self.row(y))
    
    def columnsv(self) -> Iterable[Iterable[tuple[Vec2, TValue]]]:
        return (self.columnv(x) for x in range(self.w))
    
    def columnv(self, x: int) -> Iterable[tuple[Vec2, TValue]]:
        return self.getmany(self.column(x))
    
    def beam_up(self, at: Vec2) -> Iterable[Vec2]:
        return takewhile(self.contains, at.beam_up())
    
    def beam_down(self, at: Vec2) -> Iterable[Vec2]:
        return takewhile(self.contains, at.beam_down())
    
    def beam_left(self, at: Vec2) -> Iterable[Vec2]:
        return takewhile(self.contains, at.beam_left())
    
    def beam_right(self, at: Vec2) -> Iterable[Vec2]:
        return takewhile(self.contains, at.beam_right())
    
    def beams4(self, at: Vec2) -> list[Iterable[Vec2]]:
        return [self.beam_up(at), self.beam_right(at), self.beam_down(at), self.beam_left(at)]
    
    def beam_upv(self, at: Vec2) -> Iterable[Vec2]:
        return self.getmany(self.beam_up(at))
    
    def beam_downv(self, at: Vec2) -> Iterable[Vec2]:
        return self.getmany(self.beam_down(at))
    
    def beam_leftv(self, at: Vec2) -> Iterable[Vec2]:
        return self.getmany(self.beam_left(at))
    
    def beam_rightv(self, at: Vec2) -> Iterable[Vec2]:
        return self.getmany(self.beam_right(at))
    
    def beams4v(self, at: Vec2) -> list[Iterable[Vec2]]:
        return [self.getmany(x) for x in self.beams4(at)]
    
    def near4(self, at: Vec2) -> Iterable[Vec2]:
        return filter(self.contains, at.near4())
    
    def near4v(self, at: Vec2) -> Iterable[Vec2]:
        return self.getmany(self.near4(at))
    
    def near5(self, at: Vec2) -> Iterable[Vec2]:
        return filter(self.contains, at.near5())
    
    def near5v(self, at: Vec2) -> Iterable[Vec2]:
        return self.getmany(self.near5(at))
    
    def near8(self, at: NearABC) -> Iterable[Vec2]:
        return filter(self.contains, at.near8())
    
    def near8v(self, at: NearABC) -> Iterable[tuple[Vec2, TValue]]:
        return self.getmany(self.near8(at))
    
    def near9(self, at: Vec2) -> Iterable[Vec2]:
        return filter(self.contains, at.near9())
    
    def near9v(self, at: Vec2) -> Iterable[Vec2]:
        return self.getmany(self.near9((self.w, self.h)))
    
    def getmany(self, keys: Iterable[Vec2]) -> Iterable[tuple[Vec2, TValue]]:
        return ((pos, self[pos]) for pos in keys)
    
    def cells(self) -> Iterable[Vec2]:
        return chain.from_iterable(self.rows())
    
    def cellsv(self) -> Iterable[tuple[Vec2, TValue]]:
        return chain.from_iterable(self.rowsv())
    
    def contains(self, key: Vec2) -> bool:
        return key in self
    
    def bfs4(self, start: Vec2, nfilter: Optional[Callable[[Vec2, Vec2], bool]]=None) -> Iterable[tuple[Vec2, int]]:
        def nearfunc(cur):
            return filter(lambda n: nfilter(cur, n), self.near4(cur))
        near = self.near4 if nfilter is None else nearfunc
        yield from start.bfs(near)
    
    def transpose(self) -> Field:
        return Field([[v for _, v in c] for c in self.columnsv()])

    def __getitem__(self, key: Vec2) -> TValue:
        return self.arr[key.y][key.x]
    
    def __setitem__(self, key: Vec2, value: TValue):
        self.arr[key.y][key.x] = value
    
    def __contains__(self, key: Vec2) -> bool:
        return key.is_in_field(self.w, self.h)


DIRS = 'NESW'


def dir_turnlr(cur: str, t: str):
    id = DIRS.index(cur)
    delta = 1 if t == 'R' else 3
    return DIRS[(id+delta)%4]


@dataclass(frozen=True)
class Walker2d:
    pos: Vec2 = Vec2() 
    dir: Vec2 = Vec2(0, 1)

    def rotatelr(self, r):
        return Walker2d(self.pos, self.dir.rotatelr(r))
    
    def step(self, v: int=1):
        return Walker2d(self.pos + self.dir * v, self.dir)
    
    def walkall(self, steps: Iterable[tuple[str, int]]):
        cur = self
        for d, v in steps:
            cur = cur.rotatelr(d).step(v)
        return cur
    
    def walk(self, steps: Iterable[tuple[str, int]]):
        cur = self
        for d, v in steps:
            cur = cur.rotatelr(d).step(v)
            yield cur
    
    def walk_by1(self, steps: Iterable[tuple[str, int]]):
        cur = self
        for d, v in steps:
            cur = cur.rotatelr(d)
            for _ in range(v):
                cur = cur.step()
                yield cur
    
    def mdist(self):
        return self.pos.mdist()


def columns(arr2d: list[list]):
    tmp = [[] for _ in range(len(arr2d[0]))]
    for row in arr2d:
        for i, v in enumerate(row):
            tmp[i].append(v)
    return tmp


def setcolumn(arr2d: list[list], x: int, col: list):
    for y, v in enumerate(col):
        arr2d[y][x] = v


def filter2d(arr2d: list[list], val=None):
    for y, row in enumerate(arr2d):
        for x, act in enumerate(row):
            if (val is None and bool(act)) or (val is not None and act == val):
                yield x, y, act


def count2d(arr2d: list[list], val=None):
    return sum(1 for _ in filter2d(arr2d, val))


def display2d(arr2d: list[list], true_val=None):
    for row in arr2d:
        print(''.join('#' if (true_val is not None and v==true_val) or (true_val is None and v) else '.' for v in row))


def cells(field: list[list]):
    for y, row in enumerate(field):
        for x, v in enumerate(row):
            yield x, y, v


#############
### Other ###
#############
def bfs(start: TValue, near: Callable[[TValue], Iterable[TValue]]):
    q = [start]
    visited = {start}
    curdist = 0
    while q:
        qcopy = list(q)
        q.clear()
        for cur in qcopy:
            yield cur, curdist
            for n in near(cur):
                if n not in visited:
                    q.append(n)
                    visited.add(n)
        curdist += 1