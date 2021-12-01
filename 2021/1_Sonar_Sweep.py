# https://adventofcode.com/2021/day/1

from typing import List


def read_input() -> List[int]:
    with open('1_input.txt') as f:
        return [int(x) for x in f]


def count_increases(s: list, gap=1) -> int:
    return sum(s[i] > s[i-gap] for i in range(gap, len(s)))


def star1():
    lines = read_input()
    print(count_increases(lines))


print('Star 1:')
star1()


def star2():
    lines = read_input()
    print(count_increases(lines, gap=3))


print('Star 2:')
star2()