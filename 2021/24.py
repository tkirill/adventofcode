from utils import *
import operator
from functools import cache
from collections import defaultdict


OP = {
    'mul': operator.mul,
    'add': operator.add,
    'mod': operator.mod,
    'div': operator.floordiv,
    'eql': operator.eq
}


def myeval(src, z, input):
    reg = {'x': 0, 'y': 0, 'w': 0, 'z': z}
    for op in src:
        match op:
            case 'inp', r:
                reg[r] = input
            case 'mul', a, b:
                reg[a] *= b if isinstance(b, int) else reg[b]
            case 'add', a, b:
                reg[a] += b if isinstance(b, int) else reg[b]
            case 'mod', a, b:
                reg[a] %= b if isinstance(b, int) else reg[b]
            case 'div', a, b:
                reg[a] //= b if isinstance(b, int) else reg[b]
            case 'eql', a, b:
                reg[a] = int(reg[a] == (b if isinstance(b, int) else reg[b]))
            case _:
                raise Exception(f'Unknown op {op}')
    return reg['z']


def make_block(src):
    def block(z, input):
        return myeval(src, z, input)
    return block


def parse_blocks():
    blocks, buf = [], []
    for line in readlines('24_input.txt'):
        op = line.split(' ')
        if op[0] == 'inp' and buf:
            blocks.append(make_block(list(buf)))
            buf.clear()
        if len(op) == 3:
            op[2] = try_parse_int(op[2])
        buf.append(op)
    blocks.append(make_block(buf))
    return blocks


blocks = parse_blocks()
print('Number of blocks:', len(blocks))
zoptions = {0: ''}
for block in blocks:
    print(len(zoptions))
    tmp = dict()
    for prevz, input in zoptions.items():
        for n in range(1, 10):
            z = block(prevz, n)
            key = input + str(n)
            if z not in tmp or tmp[z] > key:
                tmp[z] = key
    zoptions = tmp
print(zoptions[0], len(zoptions[0]))


def backtrack(input, z):
    if len(input) == 14:
        if blocks[-1](z, input[-1]):
            return 0
        return int(reversed(''.join(str(x) for x in input)))
    block = blocks[len(input)]
    zoptions = dict()
    for x in range(1, 10):
        zoptions[block(z, x)] = x
    if len(zoptions) < 9:
        print(zoptions)
    for z, x in sorted(zoptions.items(), key=lambda x: x[1], reverse=True):
        input.append(x)
        tmp = backtrack(input, z)
        if tmp:
            return tmp
        input.pop()
# print(backtrack([], 0))