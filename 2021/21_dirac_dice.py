from utils import *
from collections import Counter, defaultdict
import re
import itertools
import functools


die = itertools.cycle(range(1, 101))
s1, s2 = 0, 0
p1, p2 = 7, 6

ii = 0
while s2 < 1000:
    r1 = next(die)+next(die)+next(die)
    ii += 3
    p1 = (p1 + r1 - 1)%10 + 1
    s1 += p1
    if s1 >= 1000:
        break

    r2 = next(die)+next(die)+next(die)
    ii += 3
    p2 = (p2 + r2 - 1)%10 + 1
    s2 += p2
    #print(ii, p1, p2, s1, s2)
print('Star 1:', min(s1, s2) * ii)


@functools.cache
def f2(p1, p2, s1, s2):
    w1, w2 = 0, 0
    for r1 in range(3, 10):
        tmpp1 = (p1 + r1 - 1)%10 + 1
        tmps1 = s1 + tmpp1
        if tmps1 >= 21:
            w1 += 3
            continue
        for r2 in range(3, 10):
            tmpp2 = (p2 + r2 - 1)%10 + 1
            tmps2 = s2 + tmpp2
            if tmps2 >= 21:
                w2 += 3
            else:
                tmpw1, tmpw2 = f(tmpp1, tmpp2, tmps1, tmps2)
                w1 += tmpw1
                w2 += tmpw2
    return w1, w2


freq = Counter(sum(x) for x in itertools.product(range(1, 4), repeat=3))
@functools.cache
def play(pos, score, player):
    w = [0, 0]
    npos = list(pos)
    nscore = list(score)
    for r in range(3, 10):
        npos[player] = (pos[player] + r - 1) % 10 + 1
        nscore[player] = score[player] + npos[player]
        if nscore[player] >= 21:
            w[player] += freq[r]
        else:
            sub1, sub2 = play(tuple(npos), tuple(nscore), (player + 1) % 2)
            w[0] += freq[r]*sub1
            w[1] += freq[r]*sub2
    return w


w1, w2 = play((7, 6), (0, 0), 0)
print('Star 2:', max(w1, w2))