from aoc import *


def run(app: list[tuple[str, int] | str]) -> Iterable[int]:
    regx = 1
    for cmd in app:
        yield regx
        if cmd[0] == 'addx':
            yield regx
            regx += cmd[1]


def record(app):
    signal_strength = 0
    screen = []
    for cycle, regx in enumerate(run(app)):
        cycle += 1
        if cycle == 20 or (cycle-20) % 40 == 0:
            signal_strength += cycle * regx
        if (cycle-1) % 40 == 0:
            screen.append([])
        
        curpixel = (cycle - 1) % 40
        if regx-1 <= curpixel <= regx+1:
            screen[-1].append('#')
        else:
            screen[-1].append('.')
    return signal_strength, screen


signal_stregth, screen = record(read())
print('Star 1:', signal_stregth)
print('Star 2:')
display2d(screen, '#')