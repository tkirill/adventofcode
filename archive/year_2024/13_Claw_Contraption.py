from aoc.io import *
import numpy as np

def solve(button_a, button_b, prize):
    a = np.array([[button_a[0], button_b[0]], [button_a[1], button_b[1]]])
    b = np.array([prize[0], prize[1]])
    try:
        na, nb = map(round, np.linalg.solve(a, b))
    except np.linalg.LinAlgError:
        return None
    if na >= 0 and nb >= 0 and button_a[0] * na + button_b[0] * nb == prize[0] and button_a[1] * na + button_b[1] * nb == prize[1]:
        return na, nb
    return None


machines = readblocks(sep=None, parse=allints)
result = 0
for ba, bb, pr in machines:
    solution = solve(ba, bb, pr)
    if solution is None or any(x > 100 for x in solution):
        continue
    result += solution[0] * 3 + solution[1]
print('Star 1:', result)


result = 0
for ba, bb, pr in machines:
    pr[0] += 10000000000000
    pr[1] += 10000000000000
    solution = solve(ba, bb, pr)
    if solution is None:
        continue
    result += solution[0] * 3 + solution[1]
print('Star 2:', result)