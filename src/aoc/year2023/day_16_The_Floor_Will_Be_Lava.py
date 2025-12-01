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
    near = partial(beam_step, maze)
    visited = {p.pos for p, _ in algorithm.bfs(start, near)}
    return len(visited)


def star2():
    maze = board.Board(read(2023, 16, sep=None, parse=list))
    start = (
        [walker.GridWalker(p, grid.DOWN) for p in board.top(maze)] +
        [walker.GridWalker(p, grid.UP) for p in board.bottom(maze)] +
        [walker.GridWalker(p, grid.RIGHT) for p in board.first_column(maze)] +
        [walker.GridWalker(p, grid.LEFT) for p in board.last_column(maze)]
    )
    near = partial(beam_step, maze)
    return max(len({p.pos for p, _ in algorithm.bfs(s, near)}) for s in start)
