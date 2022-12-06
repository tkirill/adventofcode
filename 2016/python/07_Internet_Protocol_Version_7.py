from aoc import *
import re
from itertools import chain
import more_itertools as mtls
from typing import Iterable


ips = read(sep=r'\[|\]')


def has_abba(s: str) -> bool:
    for a, b, c, d in mtls.windowed(s, 4):
        if a == d and b == c and a != b:
            return True


total = 0
for ip in ips:
    total += any(has_abba(s) for s in ip[::2]) and not any(has_abba(s) for s in ip[1::2])
print('Star 1:', total)


def find_all_aba(s: str) -> Iterable[str]:
    for a, b, c in mtls.windowed(s, 3):
        if a == c and a != b:
            yield a, b


total = 0
for ip in ips:
    for a, b in chain.from_iterable(find_all_aba(s) for s in ip[::2]):
        tmp = ''.join([b, a, b])
        if any(tmp in s for s in ip[1::2]):
            total += 1
            break
print('Star 2:', total)


### Alternative solution with re ###


total = 0
for ip in ips:
    total += any(re.search(r'(.)((?!\1).)\2\1', s) for s in ip[::2]) and not any(re.search(r'(.)((?!\1).)\2\1', s) for s in ip[1::2])
print('Star 1 (re):', total)


total = 0
for ip in ips:
    for _, a, b in chain.from_iterable(re.findall(r'(?=((.)((?!\2).)\2))', x) for x in ip[::2]):
        tmp = b+a+b
        if any(tmp in x for x in ip[1::2]):
            total += 1
            break
print('Star 2 (re):', total)