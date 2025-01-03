from aoc.io import *
from aoc.primitives import *
from aoc import grid
from aoc import vec2
from typing import Iterable


def pull(len_: int, moves: Iterable[tuple[str, int]]):
    rope = [Vec2()] * len_
    visited = {rope[-1]}
    for d, n in moves:
        for _ in range(n):
            rope[0] = grid.screen.step(rope[0], d)
            for i in range(1, len(rope)):
                if vec2.cdist(rope[i], rope[i-1]) <= 1:
                    continue
                delta = rope[i-1] - rope[i]
                rope[i] = rope[i] + vec2.sign(delta)
            visited.add(rope[-1])
    return len(visited)


print('Star 1:', pull(2, read()))
print('Star 2:', pull(10, read()))