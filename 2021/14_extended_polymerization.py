from utils import *
from collections import Counter, defaultdict
from itertools import count, repeat, product
import re
DIGITS = '0123456789'
ALPHA = 'abcdefghijklmnopqrstuvwxyz'


polymer, rules = splitfalse(readlines('14_input.txt'))
polymer = polymer[0]
rules = dict(r.split(' -> ') for r in rules)


def freq_diff(pairs):
    ccc = defaultdict(int)
    for pair, v in pairs.items():
        ccc[pair[0]] += v
    ccc[polymer[-1]] += 1
    ccc = sorted(ccc.items(), key=lambda x: x[1])
    return ccc[-1][1] - ccc[0][1]


pairs = Counter(''.join(p) for p in zip(polymer, polymer[1:]))
for day in range(40):
    if day == 10:
        print('Star 1:', freq_diff(pairs))
    tmp = defaultdict(int)
    for pair, v in pairs.items():
        rep = rules[pair]
        l, r = pair[0] + rep, rep + pair[1]
        tmp[l] += v
        tmp[r] += v
    pairs = tmp
print('Star 2:', freq_diff(pairs))