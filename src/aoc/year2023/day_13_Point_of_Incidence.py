from typing import Iterable, Optional

from aoc.io import readblocks
from aoc.board import Board
from aoc import board


def check_symmetry(row: list[str], pos: int, smudge_budget: int) -> bool:
    r = min(pos+1, len(row)-pos-1)
    smudges = 0
    for i in range(r):
        if row[pos-i] == row[pos+i+1]:
            continue
        if smudges == smudge_budget:
            return -1
        smudges += 1
    return smudges


def board_symmetry(rows: Iterable[list[str]], smudge_budget: int) -> Optional[int]:
    cur = []
    for i in range(0, len(rows[0])-1):
        smudges = check_symmetry(rows[0], i, smudge_budget)
        if smudges >= 0:
            cur.append((i, smudges))
    for row in rows[1:]:
        nxt = []
        for i, smudges in cur:
            ne = check_symmetry(row, i, smudge_budget - smudges)
            if ne >= 0:
                nxt.append((i, max(smudges, ne)))
        if not nxt:
            return None
        cur = nxt
    return next((i+1 for i, e in cur if e == smudge_budget), None)


def star1():
    patterns = [Board(p) for p in readblocks(2023, 13, sep=None, parse=list)]
    return sum(board_symmetry(p.values, 0) or 100 * board_symmetry(board.transpose(p).values, 0) for p in patterns)


def star2():
    patterns = [Board(p) for p in readblocks(2023, 13, sep=None, parse=list)]
    return sum(board_symmetry(p.values, 1) or 100 * board_symmetry(board.transpose(p).values, 1) for p in patterns)


if __name__ == '__main__':
    print('Star 1:', star1())
    print('Star 2:', star2())
