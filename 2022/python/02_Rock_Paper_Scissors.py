from aoc import *


def score1(a, b):
    bonus = 3 if b == a else 6 if b == (a+1)%3 else 0
    return b + 1 + bonus


def score2(a, b):
    return (a + b - 1 + len('ABC')) % len('ABC') + 1 + b * 3


strategy = [('ABC'.index(a), 'XYZ'.index(b)) for a, b in read()]
print('Star 1:', sum(score1(a, b) for a, b in strategy))
print('Star 2:', sum(score2(a, b) for a, b in strategy))