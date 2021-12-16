# https://adventofcode.com/2021/day/16
from utils import *
from functools import reduce
import operator


line = readlines('16_input.txt')[0]
line = ''.join(f'{int(x,16):04b}' for x in line)
pos = 0
sumver = 0


def reads(n):
    global pos
    r = line[pos:pos+n]
    pos += n
    return r


def read_int(n):
    return int(reads(n), 2)


def read_literal():
    global pos
    blocks = []
    while line[pos] == '1':
        pos += 1
        blocks.append(reads(4))
    pos += 1
    blocks.append(reads(4))
    return int(''.join(blocks), 2)


def read_packet():
    global pos, sumver
    ver, typ = read_int(3), read_int(3)
    sumver += ver

    if typ == 4:
        return read_literal()

    id = reads(1)
    children = []
    if id == '0':
        length = read_int(15)
        eop = pos + length
        while pos < eop:
            children.append(read_packet())
    else:
        length = read_int(11)
        for _ in range(length):
            children.append(read_packet())

    if typ == 0:
        return sum(children)
    elif typ == 1:
        return reduce(operator.mul, children)
    elif typ == 2:
        return min(children)
    elif typ == 3:
        return max(children)
    elif typ == 5:
        return 1 if children[0] > children[1] else 0
    elif typ == 6:
        return 1 if children[0] < children[1] else 0
    elif typ == 7:
        return 1 if children[0] == children[1] else 0


val = read_packet()
print('Star 1:', sumver)
print('Star 2:', val)