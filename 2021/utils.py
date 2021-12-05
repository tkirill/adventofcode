from typing import Callable, Iterable, Optional, List, TypeVar


T = TypeVar('T')


def readlines(filename) -> List[str]:
    with open(filename) as f:
        return f.read().splitlines()


def parse1d(line: str, sep: Optional[str]=None) -> List[int]:
    return [int(x) for x in line.split(sep)]


def parse2d(lines: Iterable[str], sep: Optional[str]=None) -> List[List[int]]:
    return [parse1d(line, sep) for line in lines]


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