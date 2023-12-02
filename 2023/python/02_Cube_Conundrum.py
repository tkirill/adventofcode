from aoc import *
from collections import defaultdict


BUDGET = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def is_possible(game):
    return all(BUDGET.get(color, 0) >= int(n) for n, color in game[1:])


def cubes_power(game):
    cubes = defaultdict(int)
    for n, color in game[1:]:
        cubes[color] = max(cubes[color], int(n))
    return cubes['red'] * cubes['green'] * cubes['blue']


games = read(sep=r'[:,;] ', parse=lambda x: x.split())
print('Star 1:', sum(int(g[0][1]) for g in games if is_possible(g)))
print('Star 2:', sum(cubes_power(g) for g in games))