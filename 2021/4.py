from typing import List, Tuple
from utils import *


def read_input() -> Tuple[List[int], List[List[int]]]:
    first_line, *blocks = splitfalse(readlines('4_input.txt'))
    return parse1d(first_line[0]), [parse2d(b, None) for b in blocks]


def bingo(board):
    won = False
    def move(number):
        nonlocal won
        if won:
            return None
        for row in board:
            for col in range(len(row)):
                if row[col] == number:
                    row[col] = None
                    if not any(row) or not any(column(board, col)):
                        won = True
                        return sum(x for row in board for x in row if x) * number
        return None
    return move


numbers, boards = read_input()
players, scores = [bingo(b) for b in boards], []
for x in numbers:
    scores.extend(filter(None, (p(x) for p in players)))

print('Star 1:', scores[0])
print('Star 2:', scores[-1])