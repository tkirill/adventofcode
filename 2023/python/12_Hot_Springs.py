from aoc import *
from functools import cache


def read_records(copies):
    records = []
    for springs, *groups in read(sep="[ ,]"):
        blocks = filter(None, "?".join([springs] * copies).split("."))
        records.append([tuple(blocks), tuple(groups) * copies])
    return records


@cache
def get_possible_block(block: str, sizes: tuple) -> int:
    """Сколькими способами в блоке block можно получить x групп"""
    if not sizes:
        return 1 if "#" not in block else 0
    try:
        first = block.index("?")
    except ValueError:
        return 1 if (len(block),) == sizes else 0
    if first == sizes[0]:
        return get_possible_block(block[first + 1 :], sizes[1:])
    nxt = block[:first] + "#" + block[first + 1 :]
    total = get_possible_block(nxt, sizes)
    if first == 0:
        total += get_possible_block(block[1:], sizes)
    return total


@cache
def get_possible(blocks: tuple, sizes: tuple) -> int:
    """Количество вариантов получить комбинацию блоков размером sizes из блоков blocks"""
    if not blocks:
        return 0 if sizes else 1

    total = 0
    for i in range(len(sizes) + 1):
        tmp = get_possible_block(blocks[0], sizes[:i])
        if tmp:
            tmp2 = get_possible(blocks[1:], sizes[i:])
            total += tmp * tmp2
    return total


total = sum(get_possible(s, g) for s, g in read_records(1))
print("Star 1:", total)
total = sum(get_possible(s, g) for s, g in read_records(5))
print("Star 2:", total)
