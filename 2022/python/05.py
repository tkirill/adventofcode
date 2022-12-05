from aoc import *


def read_input():
    b1, b2 = readblocks(sep=None)
    
    lines = b1[:-1]
    lines.reverse()
    stacks = [list(except_(c, ' ')) for c in columns(lines)[1::4]]

    moves = [(x[1], x[3], x[5]) for x in parselines(b2)]

    return stacks, moves


stacks, moves = read_input()
for v, s, d in moves:
    for _ in range(v):
        stacks[d-1].append(stacks[s-1].pop())
print('Star 1:', ''.join(x[-1] for x in stacks))

stacks, moves = read_input()
for v, s, d in moves:
    tmp = []
    for _ in range(v):
        tmp.append(stacks[s-1].pop())
    stacks[d-1].extend(reversed(tmp))
print('Star 2:', ''.join(x[-1] for x in stacks))