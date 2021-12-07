from utils import *


def diff(x, y):
    return abs(x-y)


def sum_arith_prog(x, y):
    diff = abs(x-y)
    return ((1+diff)*diff) // 2


def mincost(lines, cost_func):
    def cost(pos):
        return sum(cost_func(x, pos) for x in lines)
    return min(cost(x) for x in lines)


numbers = parse1d(readlines('7_input.txt')[0], ',')
print('Star 1:', mincost(numbers, diff))
print('Star 2:', mincost(numbers, sum_arith_prog))