from aoc.io import read
from functools import cache


@cache
def arrangements(springs: str, groups: tuple[int], groups_len: int) -> int:
    if not springs:
        return not groups
    if not groups:
        return springs.find('#') == -1
    if len(springs) < groups[0]:
        return 0
    if len(springs) < groups_len + len(groups) - 1:
        return 0
    if springs[0] == '.':
        return arrangements(springs.lstrip('.'), groups, groups_len)
    total = 0
    if springs[0] == '?':
        total += arrangements(springs[1:], groups, groups_len)
    if springs.find('.', 0, groups[0]) == -1 and (len(springs) == groups[0] or springs[groups[0]] != '#'):
        total += arrangements(springs[groups[0]+1:], groups[1:], groups_len-groups[0])
    return total


def star1():
    records = read(2023, 12, sep=r' |,')
    return sum(arrangements(springs, tuple(groups), sum(groups)) for springs, *groups in records)


def star2():
    records = [('?'.join([s]*5), tuple(g*5)) for s, *g in read(2023, 12, sep=r' |,')]
    return sum(arrangements(springs, groups, sum(groups)) for springs, groups in records)
