from __future__ import annotations
from aoc import *
from dataclasses import dataclass
from hashlib import md5


DDD = 'UDLR'


@dataclass(frozen=True)
class State:
    path: str
    pos: Vec2

    def near(self) -> Iterable[State]:
        tmp = md5(self.path.encode('ascii')).hexdigest()
        for i, n in enumerate([self.pos.up(), self.pos.down(), self.pos.left(), self.pos.right()]):
            if n.is_in_field(4, 4) and not tmp[i].isdigit() and not tmp[i] == 'a':
                yield State(self.path + DDD[i], n)


start = State(readraw(), Vec2())
print('Star 1:', next(dist for s, dist in bfs(start, lambda x: x.near()) if s.pos == Vec2(3, 3)))