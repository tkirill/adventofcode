from aoc.io import *
from collections.abc import Iterable
from collections import defaultdict


def combo(registers: list[int], operand: int) -> int:
    if 0 <= operand <= 3:
        return operand
    return registers[operand-4]


def execute(registers: list[int], app: list[int]) -> Iterable[int]:
    ip = 0
    while ip < len(app):
        operand = app[ip+1]
        match app[ip]:
            case 0:  # adv
                registers[0] = registers[0] // (2 ** combo(registers, operand))
                ip += 2
            case 1:  # bxl
                registers[1] ^= operand
                ip += 2
            case 2:  # bst
                registers[1] = combo(registers, operand) % 8
                ip += 2
            case 3:  # jnz
                if registers[0]:
                    ip = operand
                else:
                    ip += 2
            case 4:  # bxc
                registers[1] ^= registers[2]
                ip += 2
            case 5:  # out
                yield combo(registers, operand) % 8
                ip += 2
            case 6:  # bdv
                registers[1] = registers[0] // (2 ** combo(registers, operand))
                ip += 2
            case 7:  # cdv
                registers[2] = registers[0] // (2 ** combo(registers, operand))
                ip += 2


[[a], [b], [c]], [app] = readblocks(sep=None, parse=allints)
registers = [a, b, c]
print('Star 1:', ','.join(str(x) for x in execute(registers, app)))


variants = defaultdict(list)
for i in range((2**11)):
    registers = [i, 0, 0]
    result = list(execute(registers, app))
    variants[result[0]].append(f'{i:010b}')
candidates = [variants[x] for x in app]

cur = candidates[0]
for cur_candidates in candidates[1:]:
    nxt = []
    for candiate in cur_candidates:
        for c in cur:
            if c[:7] == candiate[3:]:
                nxt.append(candiate[:3] + c)
    cur = nxt
print('Star 2:', int(cur[0], 2))

# Application code:

# b = a % 8
# b ^= 0x101
# c = a // (2 ** b)
# b ^= 0x110
# a //= 8
# b ^= c
# yield b % 8
# goto 0 if a != 0 else exit

# b = a & 0x111
# b ^= 0x101
# c = a >> b
# b ^= 0x110
# a >>= 3
# b ^= c
# yield b & 0x111
# goto 0 if a != 0 else exit