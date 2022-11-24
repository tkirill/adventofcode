import re
import string
from collections import defaultdict, Counter
import itertools as itls


ENG = string.ascii_lowercase


def read_input():
    for l in open('15_input.txt'):
        l = l.strip()
        name, cap, dur, flav, tex, cal = re.match(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)', l).groups()
        yield {'name': name, 'cap': int(cap), 'dur': int(dur), 'flav': int(flav), 'tex': int(tex), 'cal': int(cal)}


def calc(ings, ns):
    scores = [0] * 5
    for i, n in zip(ings, ns):
        scores[0] += i['cap'] * n
        scores[1] += i['dur'] * n
        scores[2] += i['flav'] * n
        scores[3] += i['tex'] * n
        scores[4] += i['cal'] * n
    if any(x < 0 for x in scores):
        return 0
    # print(scores, ns)
    r = scores[0]
    for x in scores[1:4]:
        r *= x
    return r



ings = list(read_input())
s1 = 0
for n1 in range(101):
    for n2 in range(101-n1):
        for n3 in range(101-n1-n2):
            n4 = 100-n1-n2-n3
            ns = [n1, n2, n3, n4]
            s1 = max(s1, calc(ings, ns))

print('Star 1:', s1)

s1 = 0
for n1 in range(101):
    for n2 in range(101-n1):
        for n3 in range(101-n1-n2):
            n4 = 100-n1-n2-n3
            ns = [n1, n2, n3, n4]
            if sum(i['cal']*n for i, n in zip(ings, ns)) != 500:
                continue
            s1 = max(s1, calc(ings, ns))

print('Star 2:', s1)