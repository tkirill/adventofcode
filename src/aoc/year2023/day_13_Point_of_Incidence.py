from typing import Iterable, Optional
from collections import deque
from functools import partial

from aoc.io import readblocks
from aoc.board import Board
from aoc import board
from aoc.algorithm import bfs_initial


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


def near(p: Board[str], smudge_budget: int, cur: tuple[int, int, int]) -> Iterable[tuple[int, int]]:
    row, pos, smudges = cur
    if row == p.height-1:
        return
    ns = check_symmetry(p.values[row+1], pos, smudge_budget - smudges)
    if ns >= 0:
        yield row+1, pos, max(smudges, ns)


def board_symmetry_bfs(p: Board[str], smudge_budget: int) -> Optional[int]:
    initial = [(-1, i, 0) for i in range(0, len(p.values[0])-1)]
    for (row, pos, smudges), _ in bfs_initial(initial, partial(near, p, smudge_budget), track_visited=False):
        if row == p.height-1 and smudges == smudge_budget:
            return pos + 1
    return None


# More sane iterative solution
def board_symmetry(rows: Iterable[list[str]], smudge_budget: int) -> Optional[int]:
    cur = deque()
    for i in range(0, len(rows[0])-1):
        smudges = check_symmetry(rows[0], i, smudge_budget)
        if smudges >= 0:
            cur.append((i, smudges))
    for row in rows[1:]:
        for _ in range(len(cur)):
            i, smudges = cur.popleft()
            ne = check_symmetry(row, i, smudge_budget - smudges)
            if ne >= 0:
                cur.append((i, max(smudges, ne)))
        if not cur:
            return None
    return next((i+1 for i, e in cur if e == smudge_budget), None)


def star1():
    patterns = [Board(p) for p in readblocks(2023, 13, sep=None, parse=list)]
    return sum(board_symmetry_bfs(p, 0) or 100 * board_symmetry_bfs(board.transpose(p), 0) for p in patterns)


def star2():
    patterns = [Board(p) for p in readblocks(2023, 13, sep=None, parse=list)]
    return sum(board_symmetry_bfs(p, 1) or 100 * board_symmetry_bfs(board.transpose(p), 1) for p in patterns)
