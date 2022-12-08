from aoc import *
from collections import defaultdict


def read_input():
    rules = dict()
    bins = defaultdict(list)
    for i in read():
        if i[0] == 'value':
            bins[i[-1]].append(i[1])
        else:
            rules[i[1]] = i[5], i[6], i[-2], i[-1]
    return rules, bins


rules, bins = read_input()
output = defaultdict(list)

while bins:
    for k, vals in list(bins.items()):
        if len(vals) == 2:
            del bins[k]
            x, y = sorted(vals)
            if x == 17 and y == 61:
                print('Star 1:', k)
            lowt, lown, hight, highn = rules[k]
            (output if lowt == 'output' else bins)[lown].append(x)
            (output if hight == 'output' else bins)[highn].append(y)
print('Star 2:', output[0][0] * output[1][0] * output[2][0])