from dataclasses import dataclass
import functools
from typing import Iterable
import bisect


@dataclass(frozen=True)
class Interval:

    begin: int | float
    end: int | float

    def __post_init__(self):
        if self.begin > self.end:
            object.__setattr__(self, 'begin', float('+inf'))
            object.__setattr__(self, 'end', float('-inf'))

    def __contains__(self, key: int) -> bool:
        return self.begin <= key <= self.end
    
    def __and__(self, other: Interval) -> Interval:
        return Interval(max(self.begin, other.begin), min(self.end, other.end))
    
    def __or__(self, other: Interval) -> Interval:
        if not self:
            return self.other
        if not other:
            return self
        if not is_overlapped(self, other):
            raise ValueError('Union of non-overlapped intervals is undefined')
        return Interval(min(self.begin, other.begin), max(self.end, other.end))
    
    def __len__(self) -> int:
        return self.end - self.begin
    
    def __abs__(self) -> int:
        return max(abs(self.begin), abs(self.end))
    
    def __bool__(self) -> bool:
        return not self.is_empty
    
    def __lt__(self, other: Interval) -> bool:
        if not self or not other:
            raise ValueError('Comparison with empty interval is undefined')
        return self.end < other.begin
    
    @functools.cached_property
    def is_empty(self) -> bool:
        return self.begin > self.end
    

def is_overlapped(a: Interval, b: Interval) -> bool:
    return a.end >= b.begin and a.begin <= b.end


def intersect(a: Interval, b: Interval) -> Interval:
    return a & b


def union(a: Interval, b: Interval) -> Interval:
    return a | b


def hull(a: Interval, b: Interval) -> Interval:
    return Interval(min(a.begin, b.begin), max(a.end, b.end))


def union_overlapped(intervals: list[Interval | tuple[int, int] | list[int, int]]) -> list[Interval]:
    result = []
    for cur in intervals:
        if not isinstance(cur, Interval):
            cur = Interval(*cur)
        if not cur:
            continue
        if not result or not (result[-1] & cur):
            result.append(cur)
            continue
        result[-1] = result[-1] | cur
    return result


def of_length(begin: int, length: int) -> Interval:
    return Interval(begin, begin + length - 1)


def empty() -> Interval:
    return Interval(float('+inf'), float('-inf'))


def degenerate(x: int) -> Interval:
    return Interval(x, x)


def begin(a: Interval) -> int:
    return a.begin
