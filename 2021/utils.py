from enum import auto
from typing import Callable, Iterable, Optional, List, TypeVar, Tuple, Union
from itertools import product, chain
import re


T = TypeVar('T')


def try_parse_int(s: str) -> Union[str, int]:
    try:
        return int(s)
    except ValueError:
        return s


def autoflatten(x: List[T]) -> Union[T, List[T]]:
    if len(x) == 1:
        return x[0]
    return x


def read(filename: str, sep: str=',', val: Callable[[str], T]=try_parse_int) -> List[Union[T, List[Union[T, List[T]]]]]:
    result = []
    for block in splitfalse(readlines(filename)):
        lines = []
        for line in block:
            tmp = [val(x.strip()) for x in re.split(sep, line.strip()) if x]
            lines.append(autoflatten(tmp))
        result.append(autoflatten(lines))
    return autoflatten(result)



def parse1d(line: str, sep: Optional[str]=',') -> List[int]:
    return [int(x) for x in line.split(sep)]


def parse2d(lines: Iterable[str], sep: Optional[str]=',') -> List[List[int]]:
    return [parse1d(line, sep) for line in lines]


def readlines(filename) -> List[str]:
    with open(filename) as f:
        return f.read().splitlines()


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


def ingrid(grid: List[List[T]], row: int, col: int) -> bool:
    return 0 <= row < len(grid) and 0 <= col < len(grid[row])


def near(row: int, col: int, grid: List[List[T]]) -> Iterable[T]:
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = row + dr, col + dc
        if ingrid(grid, r, c):
            yield r, c, grid[r][c]


def near8(row: int, col: int, grid: List[List[T]]) -> Iterable[T]:
    for dr, dc in product([-1, 0, 1], repeat=2):
        r, c = row + dr, col + dc
        if ingrid(grid, r, c):
            yield r, c, grid[r][c]


def cells(grid: List[List[T]]) -> Iterable[Tuple[int, int, T]]:
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            yield row, col, grid[row][col]


def flatten(list_of_lists: List[List[T]]) -> List[T]:
    return chain.from_iterable(list_of_lists)