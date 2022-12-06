from aoc import *


def find_first(s, len_):
    for i in range(len_-1, len(s)):
        if len(set(s[i-len_+1:i+1])) == len_:
            return i+1


line = read()[0]
print('Star 1:', find_first(line, 4))
print('Star 2:', find_first(line, 14))