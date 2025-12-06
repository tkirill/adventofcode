from aoc.io import read
from aoc.vec2 import Vec2
from aoc import grid, board


DIRECTIONS = [grid.RIGHT, grid.DOWN, grid.LEFT, grid.UP]


def dig(plan: list[tuple[int, int]]) -> board.Board[str]:
    cur = Vec2(0, 0)
    border = [cur]
    for direction, distance in plan:
        border.append(cur + direction*distance)
        cur = border[-1]
    return border


def star1():
    data = read(2023, 18)
    plan = [(grid.direction(_dir), dist) for _dir, dist, _ in data]
    edge = dig(plan)
    return grid.pick_theorem(edge, include_edge=True)
    

def star2():
    data = read(2023, 18)
    plan = [(int(color[2:-2], 16), DIRECTIONS[int(color[-2])]) for _, _, color in data]
    edge = dig(plan)
    return grid.pick_theorem(edge, include_edge=True)