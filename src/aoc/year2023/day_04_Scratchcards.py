from typing import Iterable

from aoc.io import read, allints


def read_cards() -> Iterable[tuple[int, int]]:
    for blocks in read(2023, 4, sep=r' ?[:|] '):
        _, id = blocks[0].split()
        winning, numbers = allints(blocks[1]), allints(blocks[2])
        won = sum(1 for n in numbers if n in winning)
        yield int(id), won


def star1():
    return sum(2**(won-1) for _, won in read_cards() if won)


def star2():
    cards = list(read_cards())
    counters = [0] + [1] * len(cards)
    for id, won in cards:
        for n in range(id+1, id+1+won):
            counters[n] += counters[id]
    return sum(counters)


if __name__ == '__main__':
    print('Star 1:', star1())
    print('Star 2:', star2())
