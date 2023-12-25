from aoc import *
from collections import Counter
from itertools import count


class TileStat:
    '''Stores how many garden plots could the Elf reach in each possible number of steps.
    
    Number of plots reachable in N steps could be calculated using this formula:

        number_of_plots[N] = visited[N] + number_of_plots[steps-2]

    where visited[N] is how many garden plots was visited first time in N steps.
    '''
    def __init__(self, garden: Field, start: Vec2):
        tmp = Counter(d for _, d in garden.bfs4(start, lambda c, n: garden[n] != '#'))
        self.by_step = [0] * (max(tmp.keys()) + 1)
        self.by_step[0], self.by_step[1] = tmp[0], tmp[1]
        self.max_by_parity = [0, 1]
        for i in range(2, len(self.by_step)):
            self.by_step[i] = tmp[i] + self.by_step[i-2]
            self.max_by_parity[i%2] = max(self.max_by_parity[i%2], i)
    
    def count_at(self, steps: int) -> int:
        if steps > max(self.max_by_parity):
            steps = self.max_by_parity[steps%2]
        return self.by_step[steps]


garden = Field(read())
start = next(pos for pos, v in garden.cellsv() if v == "S")
stat = TileStat(garden, start)
print('Star 1:', stat.count_at(64))


# Part 2 solution is based on specific properties of input:
#
#   1) Garden is a square.
#   2) Start position is at the center.
#   3) There is straigh lines of empty tiles from the start to all 4 borders.
#   4) Each tile at the border of the garden is empty.
#
# These properties mean that we will enter new copies of the garden always at the center of a border or at the corner:
#
# ...   ...   ...
# ...   ...   ...
# ...   ...   ...
#     ⌜  ^  ⌝ 
#      \ | /
# ...   ...   ...
# ...<- .S. ->...
# ...   ...   ...
#      / | \
#     ⌞  v  ⌟
# ...   ...   ...
# ...   ...   ...
# ...   ...   ...
#
# Then we can show these facts:
# 
#     1) We enter k-th horizontal/vertical copy of the garden after `(2 * k - 1) * n + k` steps. k start from 1.
#     2) We enter k-th diagonal copy of the garden after `(2 * k + 2) * n + k + 2` steps. And there are k+1 copies. k start from 0.
#
# To get the answer we use code from part 1 for each copy of the garden.

STEPS_NUMBER = 26_501_365
assert garden.w % 2 == 1
assert garden.w == garden.h

n = garden.w // 2
total = TileStat(garden, Vec2(n, n)).count_at(STEPS_NUMBER)
for start in [Vec2(0, n), Vec2(n, garden.h-1), Vec2(garden.w-1, n), Vec2(n, 0)]:
    stat = TileStat(garden, start)
    for k in count(1):
        enter = (2 * k - 1) * n + k
        if enter > STEPS_NUMBER:
            break
        total += stat.count_at(STEPS_NUMBER-enter)
for start in [Vec2(garden.w-1, garden.h-1), Vec2(0, garden.h-1), Vec2(0, 0), Vec2(garden.w-1, 0)]:
    stat = TileStat(garden, start)
    for k in count():
        enter = (2 * k + 2) * n + k + 2
        if enter > STEPS_NUMBER:
            break
        total += stat.count_at(STEPS_NUMBER - enter) * (k+1)
print('Star 2:', total)