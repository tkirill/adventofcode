from collections.abc import Iterable

from aoc.primitives import Range


def intersect(first: Range, other: Range) -> Range:
    return Range(max(first.start, other.start), min(first.end, other.end))


def difference_many(first: Range, others: Iterable[Range]) -> Iterable[Range]:
    cur = first.start
    for o in sorted(others):
        if o.start >= first.end:
            break
        if o.start > cur:
            yield Range(cur, o.start)
        cur = max(cur, o.end)
    if first.start <= cur < first.end:
        yield Range(cur, first.end)


def shift(first: Range, delta: int) -> Range:
    return Range(first.start + delta, first.end + delta)