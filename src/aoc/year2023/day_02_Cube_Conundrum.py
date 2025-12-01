from collections import Counter
from itertools import batched
import re

from aoc.io import readlines


BUDGET = Counter({
    'red': 12,
    'green': 13,
    'blue': 14
})


def parse_game(line: str) -> tuple[int, list[Counter]]:
    id, sets = re.match(r'Game (\d+): (.*)', line).groups()
    counters = []
    for s in sets.split('; '):
        cubes = re.split(',? ', s)
        counter = Counter({color: int(quantity) for quantity, color in batched(cubes, 2)})
        counters.append(counter)
    return int(id), counters


def cubes_power(sets: list[Counter]) -> int:
    tmp = Counter()
    for s in sets:
        tmp |= s
    return tmp['red'] * tmp['blue'] * tmp['green']


def star1():
    games = dict(parse_game(line) for line in readlines(year=2023, day=2))
    return sum(id for id, sets in games.items() if all(s < BUDGET for s in sets))


def star2():
    games = dict(parse_game(line) for line in readlines(year=2023, day=2))
    return sum(cubes_power(s) for s in games.values())
