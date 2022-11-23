from typing import Iterable


line = open('03_input.txt').readline().strip()

def walk(s) -> Iterable[tuple[int, int]]:
    x, y = 0, 0
    yield x, y
    for c in s:
        if c == '>':
            x += 1
        elif c == '<':
            x -= 1
        elif c == '^':
            y += 1
        else:
            y -=1
        yield x, y

print('Star 1:', len(set(walk(line))))
print('Star 2:', len(set(walk(line[::2])) | set(walk(line[1::2]))))