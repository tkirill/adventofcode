from aoc.io import *


monkeys = dict(read(sep=r': '))
values = {}


def solve(cur: str) -> int | None:
    if cur in values:
        return values[cur]
    expr = monkeys[cur]
    if isinstance(expr, int):
        values[cur] = expr
        return expr
    if expr == 'INPUT':
        return None
    l, op, r = expr.split()
    lv, rv = solve(l), solve(r)
    if lv is None or rv is None:
        return None
    match op:
        case '+': return lv + rv
        case '-': return lv - rv
        case '*': return lv * rv
        case '/': return lv // rv
print('Star 1:', solve('root'))


monkeys['root'] = monkeys['root'][:5] + '=' + monkeys['root'][6:]
monkeys['humn'] = 'INPUT'
values = {}
def solve_for_humn(cur: str, expected: int) -> int:
    expr = monkeys[cur]
    if expr == 'INPUT':
        return expected
    l, op, r = expr.split()
    lv, rv = solve(l), solve(r)
    if lv is None:
        match op:
            case '=': return solve_for_humn(l, rv)
            case '+': return solve_for_humn(l, expected - rv)
            case '-': return solve_for_humn(l, expected + rv)
            case '*': return solve_for_humn(l, expected // rv)
            case '/': return solve_for_humn(l, expected * rv)
    match op:
        case '=': return solve_for_humn(r, lv)
        case '+': return solve_for_humn(r, expected - lv)
        case '-': return solve_for_humn(r, lv - expected)
        case '*': return solve_for_humn(r, expected // lv)
        case '/': return solve_for_humn(r, lv // expected)
print('Star 2:', solve_for_humn('root', 0))