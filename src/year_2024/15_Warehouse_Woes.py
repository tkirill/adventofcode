from aoc.io import *
from aoc.grid import *
from aoc import algo
import itertools as itls
import sys
import time


def display(maze: Field[str]):
    print('\033[H')  # go to left top corner
    for s in maze.items:
        line = []
        for x in s:
            if x == '@':
                line.append('\033[31;1m@\033[0m')  # red color
            elif x == 'O':
                line.append('\033[32;1mO\033[0m')  # green color
            elif x == '[':
                line.append('\033[32;1m[')  # green color
            elif x == ']':
                line.append(']\033[0m')  # clear format
            else:
                line.append(f'\033[90m{x}')  # bright black (i.e. dark grey)
        print(''.join(line))


def near(maze, pos, move):
    nxt = maze.grid.step(pos, move)
    if maze[nxt] in '[]O':
        yield nxt
    if maze[pos] == '[':
        yield maze.grid.right(pos)
    elif maze[pos] == ']':
        yield maze.grid.left(pos)


def do_moves(maze: Field[str], moves: list[str], visualize: bool=False):
    robot = next(pos for pos, v in maze.cellsv() if v == '@')
    if visualize:
        print('\x1b[2J\033[?25l')  # clear screen & hide cursor
        display(maze)
    for move in itls.chain.from_iterable(moves):
        need_move = [pos for pos, _ in algo.bfs(robot, lambda x: near(maze, x, move))]
        moved = [maze.grid.step(x, move) for x in need_move]
        if any(maze[x] == '#' for x in moved):
            continue
        nxt_maze = Field([list(x) for x in maze.items])
        for cur in need_move:
            nxt_maze[cur] = '.'
        for cur in need_move:
            nxt = maze.grid.step(cur, move)
            nxt_maze[nxt] = maze[cur]
            if maze[cur] == '@':
                robot = nxt
        maze = nxt_maze
        if visualize:
            time.sleep(.1)
            display(maze)
    if visualize:
        print('\033[0m')
    return maze


def widen_x2(maze: list[list[str]]):
    result = []
    for line in maze:
        result.append([])
        for x in line:
            match x:
                case '@': result[-1].extend('@.')
                case 'O': result[-1].extend('[]')
                case _: result[-1].extend(x*2)
    return result


maze, moves = readblocks(parse=list)
final_maze = do_moves(Field(maze), moves, 'v1' in sys.argv)
print('Star 1:', sum(pos.y*100 + pos.x for pos, v in final_maze.cellsv() if v == 'O'))
final_maze = do_moves(Field(widen_x2(maze)), moves, 'v2' in sys.argv)
print('Star 2:', sum(pos.y*100 + pos.x for pos, v in final_maze.cellsv() if v == '['))