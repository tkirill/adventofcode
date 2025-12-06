import dataclasses
from typing import Iterable, Optional
from itertools import takewhile

from aoc.vec2 import Vec2
from aoc.rectangle import Rectangle
from aoc import grid, walker


@dataclasses.dataclass
class Board[TValue]:

    values: list[list[TValue]]
    width: int = dataclasses.field(init=False)
    height: int = dataclasses.field(init=False)

    def __post_init__(self):
        self.height = len(self.values)
        self.width = len(self.values[0]) if self.values else 0

    def __contains__(self, item: Vec2 | walker.GridWalker) -> bool:
        if isinstance(item, Vec2):
            return 0 <= item.x < self.width and 0 <= item.y < self.height
        return 0 <= item.pos.x < self.width and 0 <= item.pos.y < self.height
    
    def __getitem__(self, key: Vec2 | walker.GridWalker) -> TValue:
        if isinstance(key, Vec2):
            return self.values[key.y][key.x]
        return self.values[key.pos.y][key.pos.x]
    
    def __setitem__(self, key: Vec2, value: TValue) -> TValue:
        self.values[key.y][key.x] = value


def near8[TValue](b: Board[TValue], p: Vec2 | Rectangle) -> Iterable[Vec2]:
    return filter(b.__contains__, grid.near8(p))


def near8v[TValue](b: Board[TValue], p: Vec2 | Rectangle) -> Iterable[tuple[Vec2, TValue]]:
    for p in near8(b, p):
        yield p, b[p]


def with_value[TValue](b: Board[TValue], positions: Iterable[Vec2]) -> Iterable[tuple[Vec2, TValue]]:
    for p in positions:
        yield p, b[p]


def cells[TValue](b: Board[TValue], by_columns: bool=False, _reversed: bool=False) -> Iterable[Vec2]:
    if not by_columns:
        for row in rows(b, _reversed):
            yield from row
    else:
        for col in cols(b, _reversed):
            yield from col


def cellsv[TValue](b: Board[TValue], by_columns: bool=False, _reversed: bool=False) -> Iterable[tuple[Vec2, TValue]]:
    yield from with_value(b, cells(b, by_columns, _reversed))


def irow[TValue](b: Board[TValue], row: int, _reversed: bool=False) -> Iterable[Vec2]:
    _range = range(b.width) if not _reversed else range(b.width-1, -1, -1)
    for col in _range:
        yield Vec2(col, row)


def icol[TValue](b: Board[TValue], col: int, _reversed: bool=False) -> Iterable[Vec2]:
    _range = range(b.height) if not _reversed else range(b.height-1, -1, -1)
    for row in _range:
        yield Vec2(col, row)


def rows[TValue](b: Board[TValue], _reversed: bool=False, reversed_row: bool=False) -> Iterable[Iterable[Vec2]]:
    _range = range(b.height) if not _reversed else range(b.height-1, -1, -1)
    for row in _range:
        yield irow(b, row, reversed_row)


def rowsv[TValue](
        b: Board[TValue],
        _reversed: bool=False,
        reversed_row: bool=False) -> Iterable[Iterable[tuple[Vec2, TValue]]]:
    for row in rows(b, _reversed, reversed_row):
        yield with_value(b, row)


def cols[TValue](b: Board[TValue], _reversed: bool=False, reversed_col: bool=False) -> Iterable[Iterable[Vec2]]:
    _range = range(b.width) if not _reversed else range(b.width-1, -1, -1)
    for col in _range:
        yield icol(b, col, reversed_col)


def colsv[TValue](
        b: Board[TValue],
        _reversed: bool=False,
        reversed_col: bool=False) -> Iterable[Iterable[tuple[Vec2, TValue]]]:
    for col in cols(b, _reversed, reversed_col):
        yield with_value(b, col)


def itranspose[TValue](b: Board[TValue]) -> Iterable[Iterable[TValue]]:
    for col in range(b.width):
        yield (b.values[row][col] for row in range(b.height))


def transpose[TValue](b: Board[TValue]) -> Board[TValue]:
    return Board([list(c) for c in itranspose(b)])


def beam[TValue](b: Board[TValue], start: Vec2, delta: Vec2, skip_start: bool=False) -> Iterable[Vec2]:
    return takewhile(b.__contains__, grid.beam(start, delta, skip_start=skip_start))


def beamv[TValue](b: Board[TValue], start: Vec2, delta: Vec2, skip_start: bool=False) -> Iterable[tuple[Vec2, TValue]]:
    yield from with_value(b, beam(b, start, delta, skip_start))


def swap[TValue](b: Board[TValue], src: Vec2, dst: Vec2):
    b[src], b[dst] = b[dst], b[src]


def wrap_contains(f):
    def wrapper(b, *args, **kwargs):
        return filter(b.__contains__, f(b, *args, **kwargs))
    return wrapper


def row_at[TValue](b: Board[TValue], at: int) -> Iterable[Vec2]:
    for col in range(b.width):
        yield Vec2(col, at)


def col_at[TValue](b: Board[TValue], at: int) -> Iterable[Vec2]:
    for row in range(b.height):
        yield Vec2(at, row)


def top[TValue](b: Board[TValue]) -> Iterable[Vec2]:
    return row_at(b, 0)


def bottom[TValue](b: Board[TValue]) -> Iterable[Vec2]:
    return row_at(b, b.height-1)


def first_column[TValue](b: Board[TValue]) -> Iterable[Vec2]:
    return col_at(b, 0)


def last_column[TValue](b: Board[TValue]) -> Iterable[Vec2]:
    return col_at(b, b.width-1)


def find[TValue](b: Board[TValue], expected: TValue) -> Iterable[Vec2]:
    for p, v in cellsv(b):
        if v == expected:
            yield p


def find_near8[TValue](b: Board[TValue], pos: Vec2, expected: TValue) -> Iterable[Vec2]:
    for p, v in near8v(b, pos):
        if v == expected:
            yield p


def count_near8[TValue](b: Board[TValue], pos: Vec2, expected: TValue) -> Iterable[Vec2]:
    return sum(1 for _ in find_near8(b, pos, expected))


def of_size[TValue](w: int, h: int, value: TValue) -> Board[TValue]:
    return Board([[value]*w for _ in range(h)])


def scanline[TValue](b: Board[TValue], is_inside) -> int:
    # https://en.wikipedia.org/wiki/Scanline_rendering
    total = 0
    for row in rowsv(b):
        is_inside = False
        for p, v in row:
            
            if v in markers:
                is_inside = not is_inside
            total += is_inside
    return total