from collections.abc import Iterable

from aoc.primitives import Interval


def intersect(first: Interval, other: Interval) -> Interval:
    return Interval(max(first.start, other.start), min(first.end, other.end))


def difference_many(first: Interval, others: Iterable[Interval]) -> Iterable[Interval]:
    cur = first.start
    for o in sorted(others):
        if o.start >= first.end:
            break
        if o.start > cur:
            yield Interval(cur, o.start)
        cur = max(cur, o.end)
    if first.start <= cur < first.end:
        yield Interval(cur, first.end)


def shift(first: Interval, delta: int) -> Interval:
    return Interval(first.start + delta, first.end + delta)