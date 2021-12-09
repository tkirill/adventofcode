from typing import Callable, Iterable, Optional, List, TypeVar


T = TypeVar('T')


def parse1d(line: str, sep: Optional[str]=',') -> List[int]:
    return [int(x) for x in line.split(sep)]


def parse2d(lines: Iterable[str], sep: Optional[str]=',') -> List[List[int]]:
    return [parse1d(line, sep) for line in lines]


def readlines(filename) -> List[str]:
    with open(filename) as f:
        return f.read().splitlines()


def read(filename, sep: Optional[str]=',') -> List[List[int]]:
    return parse2d(readlines(filename), sep)


def read1(filename, sep: Optional[str]=',') -> List[List[int]]:
    return read(filename, sep)[0]


def splitfalse(items: Iterable[T], pred: Optional[Callable[[T],bool]]=None) -> List[List[T]]:
    buf = []
    for item in items:
        if pred and pred(item) or not pred and item:
            buf.append(item)
        elif buf:
            yield buf
            buf = []
    if buf:
        yield buf


def column(a: List[List[T]], col: int) -> List[T]:
    return [row[col] for row in a]


def sign(x: int) -> int:
    return x // abs(x) if x else 0


def near(row: int, col: int, grid: List[List[T]]) -> Iterable[T]:
    if row > 0:
        yield row-1, col
    if row < len(grid)-1:
        yield row+1, col
    if col > 0:
        yield row, col-1
    if col < len(grid[row])-1:
        yield row, col+1


def nearvals(row: int, col: int, grid: List[List[T]]) -> List[T]:
    return [grid[r][c] for r, c in near(row, col, grid)]