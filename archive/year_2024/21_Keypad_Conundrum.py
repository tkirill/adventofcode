from aoc.io import *
from aoc.primitives import *
from aoc.grid import *
from aoc import algo
import itertools as itls
import functools


NUMERIC = Field([
    '789',
    '456',
    '123',
    ' 0A'
])
NUMERIC_POS = {v: pos for pos, v in NUMERIC.cellsv()}
DIRECTIONAL = Field([
    ' ^A',
    '<v>'
])
DIRECTIONAL_POS = {v: pos for pos, v in DIRECTIONAL.cellsv()}



@functools.cache
def near_robot(robot: int, robots_total: int, state: tuple[Vec2, str], dest_pos: Vec2):
    keyboard = NUMERIC if robot == 1 else DIRECTIONAL
    cur_pos, prev_dir = state
    if cur_pos == dest_pos:
        return [((cur_pos, 'A'), push_cost_robot(robot+1, robots_total, prev_dir, 'A'))]
    result = []
    for d in '^>v<':
        n = keyboard.grid.step(cur_pos, d)
        if n in keyboard and keyboard[n] != ' ':
            result.append(((n, d), push_cost_robot(robot+1, robots_total, prev_dir, d)))
    return result


@functools.cache
def push_cost_robot(robot: int, robots_total: int, prev: str, cur: str) -> int:
    keyboard = NUMERIC_POS if robot == 1 else DIRECTIONAL_POS
    prev_pos = keyboard[prev]
    cur_pos = keyboard[cur]
    if prev_pos == cur_pos:
        return 1
    if robot == robots_total:
        return next(i for pos, i in DIRECTIONAL.bfs4(prev_pos, lambda p1, p2: DIRECTIONAL[p2] != ' ') if pos == cur_pos) + 1
    dist, _ = algo.dijkstra((prev_pos, 'A'), lambda n: near_robot(robot, robots_total, n, cur_pos))
    return dist[(cur_pos, 'A')]


def get_code_cost(code: str, robots_total: int) -> int:
    return sum(push_cost_robot(1, robots_total, prev, cur) for prev, cur in itls.pairwise('A'+code))


codes = readlines()
print('Star 1:', sum(get_code_cost(code, 3) * allints(code)[0] for code in codes))
print('Star 2:', sum(get_code_cost(code, 26) * allints(code)[0] for code in codes))