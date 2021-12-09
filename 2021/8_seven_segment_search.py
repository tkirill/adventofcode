from utils import *
from collections import Counter
from itertools import permutations
from typing import Dict, List, Tuple


DIGITS = {s: i for i, s in enumerate([
    'abcefg',  # 0
    'cf',  # 1
    'acdeg',  # 2
    'acdfg',  # 3
    'bcdf',  # 4
    'abdfg',  # 5
    'abdefg',  # 6
    'acf',  # 7
    'abcdefg',  # 8
    'abcdfg'  # 9
])}


def read_input() -> List[Tuple[List[str], List[str]]]:
    lines = [x.split(' | ') for x in readlines('8_input.txt')]
    for ds, os in lines:
        yield ds.split(), os.split()


def read_digit(wiring: Dict[str, str], d: str) -> Optional[int]:
    fixed = ''.join(sorted(wiring[x] for x in d))
    return DIGITS.get(fixed)


def decode(ds: List[str], os: List[str]) -> int:
    for perm in permutations('abcdefg'):
        wiring = {k: v for k, v in zip('abcdefg', perm)}
        if all(read_digit(wiring, d) is not None for d in ds):
            return int(''.join(str(read_digit(wiring, o)) for o in os))


def star1():
    c = Counter(len(x) for _, os in read_input() for x in os)
    print(c[7]+c[4]+c[3]+c[2])


def star2():
    lines = read_input()
    print(sum(decode(ds, os) for ds, os in lines))


print('Star 1:')
star1()
print('Star 2:')
star2()