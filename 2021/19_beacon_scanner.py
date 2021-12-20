from utils import *
from itertools import combinations
from functools import reduce


# https://stackoverflow.com/a/16467849/458723
def roll(v):
    '''Roll over X 90 degree counter-clockwise'''
    return (v[0],v[2],-v[1])


def turn(v):
    '''Turn over Z 90 degree counter-clockwise'''
    return (-v[1],v[0],v[2])


def orientations(v):
    '''All 24 orientations'''
    for around_x in range(4):
        for around_z in range(4):
            yield v
            v = turn(v)
        v = roll(v)
    v = roll(turn(v))
    for around_z in range(4):
        yield v
        v = turn(v)
    v = roll(roll(v))
    for around_z in range(4):
        yield v
        v = turn(v)


def deltav(a, b):
    return [y-x for x, y in zip(a, b)]


def addv(a, b):
    return tuple(x+y for x, y in zip(a, b))


def shift(a, delta):
    return [addv(x, delta) for x in a]


def find_delta(a: set, b: list):
    for orient in zip(*[orientations(x) for x in b]):
        for x in orient:
            for y in a:
                delta = deltav(x, y)
                shifted = set(shift(orient, delta))
                if len(a & shifted) >= 12:
                    a |= shifted
                    return a, delta


def manh(a, b):
    return sum(abs(x-y) for x, y in zip(a, b))


scans = [x[1:] for x in read('19_input.txt')]
scanners = [(0, 0, 0)]
beacons = {tuple(x) for x in scans[0]}
merged = {0}
while len(merged) < len(scans):
    for i in range(len(scans)):
        if i in merged:
            continue
        print(len(merged), i)
        tmp = find_delta(beacons, scans[i])
        if tmp is not None:
            beacons, s = tmp
            merged.add(i)
            scanners.append(s)
print('Star 1:', len(beacons))
print('Star 2:', max(manh(a, b) for a, b in combinations(scanners, 2)))