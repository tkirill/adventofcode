from typing import Iterable

from aoc.io import read
from aoc import board, algorithm, grid, walker
from aoc.vec2 import Vec2
from functools import partial


@board.wrap_contains
def beam_step(maze: board.Board[str], beam: walker.GridWalker) -> Iterable[walker.GridWalker]:
    match maze[beam.pos]:
        case '.':
            yield walker.step(beam)
        case '-':
            if beam.velocity in [grid.LEFT, grid.RIGHT]:
                yield walker.step(beam)
            else:
                yield walker.step(walker.turn(beam, 'CCW'))
                yield walker.step(walker.turn(beam, 'CW'))
        case '|':
            if beam.velocity in [grid.UP, grid.DOWN]:
                yield walker.step(beam)
            else:
                yield walker.step(walker.turn(beam, 'CCW'))
                yield walker.step(walker.turn(beam, 'CW'))
        case '/':
            if beam.velocity in [grid.UP, grid.DOWN]:
                yield walker.step(walker.turn(beam, 'CW'))
            else:
                yield walker.step(walker.turn(beam, 'CCW'))
        case '\\':
            if beam.velocity in [grid.UP, grid.DOWN]:
                yield walker.step(walker.turn(beam, 'CCW'))
            else:
                yield walker.step(walker.turn(beam, 'CW'))


def star1():
    maze = board.Board(read(2023, 16, sep=None, parse=list))
    start = walker.GridWalker(Vec2(0, 0), grid.RIGHT)
    visited = {p.pos for p, _ in algorithm.bfs(start, partial(beam_step, maze))}
    return len(visited)


def star2():
    pass


if __name__ == '__main__':
    print('Star 1:', star1())
    print('Star 2:', star2())
