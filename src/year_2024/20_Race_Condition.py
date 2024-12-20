from aoc.io import *
from aoc.grid import *
from aoc.primitives import *
from aoc import algo
import itertools as itls
import more_itertools as mtls
import functools as ftls


def count_cheats(max_cheat: int):
    cheats = 0
    for cur, curv in maze.cellsv():
        if curv == '#':
            continue
        for n, nv in maze.circlev(cur, max_cheat):
            if nv == '#':
                continue
            saves = dist_from_start[dest] - (dist_from_start[cur] + cur.mdist(n) + dist_from_dest[n])
            if saves >= 100:
                cheats += 1
    return cheats


maze = Field(read(sep=None, parse=list))
start = next(pos for pos, v in maze.cellsv() if v == 'S')
dest = next(pos for pos, v in maze.cellsv() if v == 'E')
dist_from_start = {pos: i for pos, i in maze.bfs4(start, lambda p1, p2: maze[p2] != '#')}
dist_from_dest = {pos: i for pos, i in maze.bfs4(dest, lambda p1, p2: maze[p2] != '#')}
print('Star 1:', count_cheats(2))
print('Star 2:', count_cheats(20))


# original = next(i for pos, i in maze.bfs4(start, lambda p1, p2: maze[p2] != '#') if pos == dest)
# print('Original: ', original)

# def find_cheats():
#     cnt = 0
#     for possible_cheat, v in maze.cellsv():
#         if v != '#':
#             continue
#         u, d, l, r = maze.grid.up(possible_cheat), maze.grid.down(possible_cheat), maze.grid.left(possible_cheat), maze.grid.right(possible_cheat)
#         if u in maze and d in maze and maze[u] != '#' and maze[d] != '#' or l in maze and r in maze and maze[l] != '#' and maze[r] != '#':
#             cnt += 1
#             if cnt % 100 == 0:
#                 print(cnt)
#             maze[possible_cheat] = '.'
#             cheat_path = next(i for pos, i in maze.bfs4(start, lambda p1, p2: maze[p2] != '#') if pos == dest)
#             maze[possible_cheat] = '#'
#             yield cheat_path
# # from collections import Counter
# # cnt = Counter(original - cheat for cheat in find_cheats())
# # for x in sorted(cnt.keys()):
# #     print(x, cnt[x])

# print('Star 1:', sum(original - cheat >= 100 for cheat in find_cheats()))

# original_path = []
# possible_cheats = set()
# for pos, i in maze.bfs4(start, lambda p1, p2: maze[p2] != '#'):
#     original_path.append(pos)
#     if pos == dest:
#         break
#     possible_cheats.update(n for n, nv in maze.near4v(pos) if nv == '#')


# def near(state, max_cheat):
#     pos, cheat_start, cheat_end = state
#     for n, nv in maze.near4v(pos):
#         if nv != '#':
#             if cheat_start is None or cheat_end is not None:
#                 yield n, cheat_start, cheat_end
#                 continue
#             if cheat_start.mdist(n) <= max_cheat-1:
#                 yield n, cheat_start, n
#             continue
#         if cheat_start is None:
#             yield n, n, None
#             continue
#         if cheat_end is None and cheat_start.mdist(n) <= max_cheat-1:
#             yield n, cheat_start, cheat_end

# cheats = set()
# from collections import defaultdict
# cheats_cnt = defaultdict(int)
# for (pos, cheat_start, cheat_end), length in algo.bfs((start, None, None), lambda s: near(s, 20)):
#     if length > original - 100:
#         break
#     if pos != dest:
#         continue
#     if length >= original:
#         continue
#     cheat = (cheat_start, cheat_end)
#     if cheat in cheats:
#         continue
#     cheats.add(cheat)
#     saves = original - length
#     cheats_cnt[saves] += 1
# print('Star 1:', sum(v for k, v in cheats_cnt.items() if k >= 100))