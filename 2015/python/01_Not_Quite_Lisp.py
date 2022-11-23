from typing import Iterable


def walk(s) -> Iterable[int]:
    floor = 0
    for c in s:
        floor += 1 if c == '(' else -1
        yield floor

line = open('01_input.txt').readline().strip()
floors = list(walk(line))

print('Star 1:', floors[-1])
print('Star 2:', floors.index(-1)+1)