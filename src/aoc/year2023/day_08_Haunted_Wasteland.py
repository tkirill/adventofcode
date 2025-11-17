from itertools import cycle
import math

from aoc.io import readblocks


def walk(instructions, network, start):
    cur = start
    yield cur
    for turn in cycle(instructions):
        cur = network[cur][turn]
        yield cur


def star1():
    [instructions], nodes = readblocks(2023, 8, sep=r'[ =,()]+')
    network = {h: {'L': l, 'R': r} for h, l, r in nodes}
    return next(i for i, cur in enumerate(walk(instructions, network, 'AAA')) if cur == 'ZZZ')


def star2():
    [instructions], nodes = readblocks(2023, 8, sep=r'[ =,()]+')
    network = {h: {'L': l, 'R': r} for h, l, r in nodes}
    cycles = []
    for start in network.keys():
        if start[-1] != 'A':
            continue
        c = next(i for i, cur in enumerate(walk(instructions, network, start)) if cur[-1] == 'Z')
        cycles.append(c)
    return math.lcm(*cycles)


if __name__ == '__main__':
    print('Star 1:', star1())
    print('Star 2:', star2())
