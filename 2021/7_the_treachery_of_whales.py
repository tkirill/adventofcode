# https://adventofcode.com/2021/day/7
from utils import *


def diff(x: int, y: int) -> int:
    return abs(x-y)


def sum_arith_prog(x: int, y: int) -> int:
    diff = abs(x-y)
    return ((1 + diff) * diff) // 2


def mincost(crabs: List[int], cost_func: Callable[[int, int], int]) -> int:
    def cost(pos):
        return sum(cost_func(x, pos) for x in crabs)
    return min(cost(x) for x in crabs)


print('Star 1:', mincost(read('7_input.txt'), diff))
print('Star 2:', mincost(read('7_input.txt'), sum_arith_prog))