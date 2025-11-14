from aoc.io import readlines
from typing import Sequence, Iterable
from itertools import chain


DIGITS = '123456789'
DIGIT_WORDS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def find_first_positions(line: str, digits: Sequence[str]) -> Iterable[tuple[int, int]]:
    return [(line.find(d), i+1) for i, d in enumerate(digits) if d in line]


def find_last_positions(line: str, digits: Sequence[str]) -> Iterable[tuple[int, int]]:
    return [(line.rfind(d), i+1) for i, d in enumerate(digits) if d in line]


def star1():
    total = 0
    for l in readlines(year=2023, day=1):
        first, last = min(find_first_positions(l, DIGITS)), max(find_last_positions(l, DIGITS))
        total += first[1]*10 + last[1]
    return total


def star2():
    total = 0
    for l in readlines(year=2023, day=1):
        first = min(chain(find_first_positions(l, DIGITS), find_first_positions(l, DIGIT_WORDS)))
        last = max(chain(find_last_positions(l, DIGITS), find_last_positions(l, DIGIT_WORDS)))
        total += first[1]*10 + last[1]
    return total


if __name__ == '__main__':
    print('Star 1:', star1())
    print('Star 2:', star2())