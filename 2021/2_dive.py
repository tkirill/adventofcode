from typing import Iterable, Tuple


def read_lines() -> Iterable[Tuple[int, int]]:
    with open('2_input.txt') as f:
        for line in f:
            match line.split():
                case 'forward', v:
                    yield int(v), 0
                case 'down', v:
                    yield 0, int(v)
                case _:
                    yield 0, -int(v)


def star1():
    pos = [0, 0]
    for x, y in read_lines():
        pos[0] += x
        pos[1] += y
    print(pos[0]*pos[1])


print('Star 1:')
star1()


def star2():
    pos = [0, 0]
    aim = 0
    for x, y in read_lines():
        pos[0] += x
        pos[1] += x*aim
        aim += y
    print(pos[0]*pos[1])


print('Star 2:')
star2()