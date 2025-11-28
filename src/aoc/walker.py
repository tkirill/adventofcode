import dataclasses

from aoc.vec2 import Vec2
from aoc import grid


@dataclasses.dataclass(frozen=True)
class GridWalker:

    pos: Vec2
    velocity: Vec2


def step(w: GridWalker) -> GridWalker:
    return dataclasses.replace(w, pos=w.pos+w.velocity)


def turn(w: GridWalker, d: str) -> GridWalker:
    return dataclasses.replace(w, velocity=grid.turn(w.velocity, d))
