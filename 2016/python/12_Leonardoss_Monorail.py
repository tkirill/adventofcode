from aoc import *
from collections import defaultdict


def run(app: list[list[str | int]], init=dict()) -> int:
    registers = defaultdict(int, init)
    ip = 0

    def get_val(x: str | int) -> int:
        return x if isinstance(x, int) else registers[x]

    while ip < len(app):
        cmd = app[ip]
        if cmd[0] == 'cpy':
            registers[cmd[2]] = get_val(cmd[1])
            ip += 1
        elif cmd[0] == 'inc':
            registers[cmd[1]] += 1
            ip += 1
        elif cmd[0] == 'dec':
            registers[cmd[1]] -= 1
            ip += 1
        elif cmd[0] == 'jnz':
            ip += cmd[2] if get_val(cmd[1]) != 0 else 1
    return registers['a']


print('Star 1:', run(read()))
print('Star 2:', run(read(), {'c': 1}))