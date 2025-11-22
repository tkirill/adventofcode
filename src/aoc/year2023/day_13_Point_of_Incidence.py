from typing import Iterable, Optional

from aoc.io import readblocks
from aoc.board import Board
from aoc import board


def check_symmetry(row: list[str], pos: int, error_budget: int) -> bool:
    r = min(pos+1, len(row)-pos-1)
    for i in range(r):
        if row[pos-i] == row[pos+i+1]:
            continue
        if error_budget:
            error_budget -= 1
        else:
            return False
    return True


def board_symmetry(rows: Iterable[list[str]], error_budget: int) -> Optional[int]:
    cur = [i for i in range(0, len(rows[0])-1) if check_symmetry(rows[0], i, error_budget)]
    for row in rows[1:]:
        cur = [i for i in cur if check_symmetry(row, i, error_budget)]
        if not cur:
            return None
    return cur[0]+1


def star1():
    patterns = [Board(p) for p in readblocks(2023, 13, sep=None, parse=list)]
    total = 0 
    for p in patterns:
        s = board_symmetry(p.values, 0)
        if s is not None:
            total += s
        else:
            total += 100 * board_symmetry([[v for _, v in col] for col in board.colsv(p)], 0)
    return total


def star2():
    pass


if __name__ == '__main__':
    print('Star 1:', star1())
    print('Star 2:', star2())
