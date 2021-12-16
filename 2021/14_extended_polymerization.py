# https://adventofcode.com/2021/day/14
from utils import *
from collections import Counter, defaultdict


polymer, rules = read('14_input.txt', sep='->')
rules = dict(rules)


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