from aoc.io import read, allints
from aoc.math import product
from math import sqrt, floor, ceil


def count_wins(time: int, distance: int) -> int:
    # bruteforce:
    # return sum(1 for hold in range(time) if hold * (time - hold) > distance)
    x1 = (time - sqrt(time**2 - 4 * distance)) / 2
    x2 = (time + sqrt(time**2 - 4 * distance)) / 2
    return floor(x2) - ceil(x1) + 1


def star1():
    races = zip(*read(2023, 6, sep=None, parse=allints))
    return product(count_wins(t, d) for t, d in races)


def star2():
    races = zip(*read(2023, 6, sep=None, parse=lambda s: allints(s.replace(' ', ''))))
    return product(count_wins(t, d) for t, d in races)


if __name__ == '__main__':
    print('Star 1:', star1())
    print('Star 2:', star2())
