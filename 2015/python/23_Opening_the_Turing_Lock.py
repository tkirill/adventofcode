from aoc import *


def run(app, registers):
    ip = 0
    while 0 <= ip < len(app):
        cur = app[ip]
        if cur[0] == 'hlf':
            registers[cur[1]] //= 2
            ip += 1
        elif cur[0] == 'tpl':
            registers[cur[1]] *= 3
            ip += 1
        elif cur[0] == 'inc':
            registers[cur[1]] += 1
            ip += 1
        elif cur[0] == 'jmp':
            ip += cur[1]
        elif cur[0] == 'jie':
            ip += cur[2] if registers[cur[1]] % 2 == 0 else 1
        elif cur[0] == 'jio':
            ip += cur[2] if registers[cur[1]] == 1 else 1
    return registers


app = read(sep='\s|, ')
print('Star 1:', run(app, {'a': 0, 'b': 0})['b'])
print('Star 2:', run(app, {'a': 1, 'b': 0})['b'])