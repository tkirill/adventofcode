from aoc.io import *
from aoc.grid import Field
from itertools import chain


def find_line(pattern: Field, smudge_number: int) -> int | None:
    for i in range(1, pattern.h):
        l = chain.from_iterable(pattern.items[i - 1 : None : -1])
        r = chain.from_iterable(pattern.items[i:])
        diff = sum(1 for ll, rr in zip(l, r) if ll != rr)
        if diff == smudge_number:
            return i
    return None


def score(pattern: Field, smudge_number: int) -> int:
    line = find_line(pattern, smudge_number)
    if line is not None:
        return 100 * line
    return find_line(pattern.transpose(), smudge_number)


patterns = [Field(b) for b in readblocks()]
print("Star 1:", sum(score(p, 0) for p in patterns))
print("Star 2:", sum(score(p, 1) for p in patterns))
