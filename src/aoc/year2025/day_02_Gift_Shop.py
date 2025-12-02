import itertools

from aoc.io import read


def star1():
    ranges = itertools.batched(read(2025, 2, sep=r',|-')[0], 2)
    total = 0
    for a, b in ranges:
        for i in range(a, b+1):
            s = str(i)
            if len(s) % 2 == 0 and s[:len(s)//2] == s[len(s)//2:]:
                total += i
    return total


def star2():
    ranges = itertools.batched(read(2025, 2, sep=r',|-')[0], 2)
    total = 0
    visited = set()
    for a, b in ranges:
        for i in range(a, b+1):
            s = str(i)
            for j in range(1,len(s)):
                if len(s) % j == 0 and (len(s) // j) >= 2 and s not in visited and s == (s[:j] * (len(s) // j)):
                    total += i
                    visited.add(s)
    return total