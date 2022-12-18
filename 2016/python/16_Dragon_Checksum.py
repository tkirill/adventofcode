from aoc import *

TRANS = str.maketrans({'0': '1', '1': '0'})

def step(s: str) -> str:
    return ''.join([s, '0', s[::-1].translate(TRANS)])


def checksum(s: str) -> str:
    while len(s) % 2 == 0:
        s = ''.join('1' if s[i] == s[i+1] else '0' for i in range(0, len(s), 2))
    return s


def fill(init: str, len_: int) -> str:
    cur = init
    while len(cur) < len_:
        cur = step(cur)
    return checksum(cur[:len_])


print('Star 1:', fill(readraw(), 272))
print('Star 2:', fill(readraw(), 35651584))