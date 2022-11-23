import re
from typing import Iterable
import numpy as np


def read_commands() -> Iterable[tuple[str, int, int, int, int]]:
    for line in open('06_input.txt'):
        command, x1, y1, x2, y2 = re.match(r'([a-z ]+?) (\d+),(\d+) through (\d+),(\d+)', line).groups()
        yield command, (slice(int(x1), int(x2)+1), slice(int(y1), int(y2)+1))


commands = list(read_commands())

field = np.full((1000, 1000), False)
for cmd in commands:
    command, region = cmd
    if command == 'turn on':
        field[region] = True
    elif command == 'turn off':
        field[region] = False
    else:
        field[region] ^= True
print(field.sum())

field = np.full((1000, 1000), 0)
for cmd in commands:
    command, region = cmd
    if command == 'turn on':
        field[region] += 1
    elif command == 'turn off':
        field[region] -= 1
        field[field < 0] = 0
    else:
        field[region] += 2
print(field.sum())