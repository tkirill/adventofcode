import __main__
from pathlib import Path
import re
from typing import Any, Iterable
from dataclasses import dataclass


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


########################
### Sequence helpers ###
########################


def except_(it: Iterable, exclude):
    for a in it:
        if a != exclude:
            yield a


def columns(arr2d: list[list]):
    tmp = [[] for _ in range(len(arr2d[0]))]
    for row in arr2d:
        for i, v in enumerate(row):
            tmp[i].append(v)
    return tmp


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


@dataclass(frozen=True)
class Vec2:
    x: int = 0
    y: int = 0
    ydir: int = 1

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
    
    def __truediv__(self, other):
        return Vec2(self.x / other, self.y / other, self.ydir)
    
    def __floordiv__(self, other):
        return Vec2(self.x // other, self.y // other, self.ydir)
    
    def __mod__(self, other):
        return Vec2(self.x % other, self.y % other, self.ydir)
    
    def __pow__(self, other):
        return Vec2(self.x ** other, self.y ** other, self.ydir)
    
    def __neg__(self):
        return Vec2(-self.x, -self.y, self.ydir)
    
    def __abs__(self):
        return Vec2(abs(self.x), abs(self.y), self.ydir)
    
    def rotatelr(self, r: str):
        if self.ydir == 1:
            return Vec2(self.y, -self.x, self.ydir) if r == 'R' else Vec2(-self.y, self.x, self.ydir)
        return Vec2(-self.y, self.x, self.ydir) if r == 'R' else Vec2(self.y, -self.x, self.ydir)
    
    def mdist(self):
        return abs(self.x) + abs(self.y)
    
    def up(self):
        return self + Vec2(0, self.ydir)
    
    def down(self):
        return self - Vec2(0, self.ydir)
    
    def left(self):
        return self - Vec2(1, 0)
    
    def right(self):
        return self + Vec2(1, 0)
    
    def step(self, d: str):
        match(d):
            case 'L': return self.left()
            case 'R': return self.right()
            case 'U': return self.up()
            case 'D': return self.down()


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