from aoc.io import read


def compute(s: str) -> int:
    total = 0
    for c in s:
        total += ord(c)
        total *= 17
        total %= 256
    return total


def star1():
    steps = read(year=2023, day=15, sep=',', parse=str)[0]
    return sum(compute(s) for s in steps)


def star2():
    pass


if __name__ == '__main__':
    print('Star 1:', star1())
    print('Star 2:', star2())
