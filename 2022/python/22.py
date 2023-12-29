from aoc import *
import re


DIRCOST = {Vec2(1, 0): 0, Vec2(0, 1): 1, Vec2(-1, 0): 2, Vec2(0, -1): 3}


def getcells(field: list[str]) -> dict[Vec2, bool]:
    cells = {}
    for y, row in enumerate(field):
        for x, c in enumerate(row):
            if c == "#":
                cells[Vec2(x + 1, y + 1)] = False
            elif c == ".":
                cells[Vec2(x + 1, y + 1)] = True
    return cells


def getmoves(moves: str) -> list[tuple[str, int]]:
    result = []
    for m in re.finditer(r"(\w)(\d+)", moves):
        d, v = m.groups()
        result.append((d, int(v)))
    return result


def make_tp(src: list[Vec2], sdir: Vec2, dst: list[Vec2], ddir: Vec2):
    for ss, dd in zip(src, dst):
        yield Walker2d(ss, sdir), Walker2d(dd, ddir)
    sdir = sdir.rotatelr("R").rotatelr("R")
    ddir = ddir.rotatelr("R").rotatelr("R")
    for ss, dd in zip(src, dst):
        yield Walker2d(dd, ddir), Walker2d(ss, sdir)


def hside(startx: int, y: int, reverse: bool = False) -> list[Vec2]:
    result = []
    for _ in range(50):
        result.append(Vec2(startx, y))
        startx += 1 if not reverse else -1
    return result


def vside(x: int, starty: int, reverse: bool = False) -> list[Vec2]:
    result = []
    for _ in range(50):
        result.append(Vec2(x, starty))
        starty += 1 if not reverse else -1
    return result


TP = dict(
    chain(
        # front <-> left
        make_tp(vside(51, 50, True), Vec2(-1, 0), vside(1, 101), Vec2(1, 0)),
        # front <-> right
        make_tp(vside(100, 1), Vec2(1, 0), vside(101, 1), Vec2(1, 0)),
        # front <-> top
        make_tp(hside(51, 50), Vec2(0, 1), hside(51, 51), Vec2(0, 1)),
        # front <-> bottom
        make_tp(hside(51, 1), Vec2(0, -1), vside(1, 151), Vec2(1, 0)),
        # top <-> left
        make_tp(vside(51, 100, True), Vec2(-1, 0), hside(50, 101, True), Vec2(0, 1)),
        # top <-> right
        make_tp(vside(100, 51), Vec2(1, 0), hside(101, 50), Vec2(0, -1)),
        # bottom <-> left
        make_tp(hside(1, 151), Vec2(0, -1), hside(1, 150), Vec2(0, -1)),
        # bottom <-> right
        make_tp(hside(1, 200), Vec2(0, 1), hside(101, 1), Vec2(0, 1)),
        # back <-> left
        make_tp(vside(51, 101), Vec2(-1, 0), vside(50, 101), Vec2(-1, 0)),
        # back <-> right
        make_tp(vside(100, 101), Vec2(1, 0), vside(150, 50, True), Vec2(-1, 0)),
        # back <-> top
        make_tp(hside(51, 101), Vec2(0, -1), hside(51, 100), Vec2(0, -1)),
        # back <-> bottom
        make_tp(hside(51, 150), Vec2(0, 1), vside(50, 151), Vec2(-1, 0)),
    )
)


def step1(field: dict[Vec2, bool], cur: Walker2d) -> Walker2d:
    nxt_walker = cur.step()
    while nxt_walker.pos not in field:
        nxt_walker = nxt_walker.step()
        nxt_walker = Walker2d(nxt_walker.pos % Vec2(W, H), nxt_walker.dir)
    return nxt_walker


def walk(
    field: dict[Vec2, bool],
    moves: list[tuple[str, int]],
    step: Callable[[Walker2d], Walker2d],
) -> int:
    walker = Walker2d(Vec2(51, 1))
    for turn, dist in moves:
        walker = walker.rotatelr(turn)
        for _ in range(dist):
            nxt_walker = step(field, walker)
            cell = field[nxt_walker.pos]
            if not cell:
                break
            walker = nxt_walker
    return walker.pos.y * 1000 + walker.pos.x * 4 + DIRCOST[walker.dir]


field, moves = readraw().split("\n\n")
field = field.splitlines()
W, H = len(field[0]) + 1, len(field) + 1
cells = getcells(field)
moves = getmoves("L" + moves)
print("Star 1:", walk(cells, moves, step1))
print("Star 2:", walk(cells, moves, lambda f, cur: TP.get(cur) or cur.step()))
