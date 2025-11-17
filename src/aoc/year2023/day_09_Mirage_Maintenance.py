from aoc.io import read

from itertools import pairwise


def predict_forward(history: list[int]) -> int:
    if all(x == 0 for x in history):
        return 0
    diff = [b-a for a, b in pairwise(history)]
    return history[-1] + predict_forward(diff)


def predict_backward(history: list[int]) -> int:
    if all(x == 0 for x in history):
        return 0
    diff = [b-a for a, b in pairwise(history)]
    return history[0] - predict_backward(diff)


def star1():
    history = read(2023, 9)
    return sum(predict_forward(i) for i in history)


def star2():
    history = read(2023, 9)
    return sum(predict_backward(i) for i in history)


if __name__ == '__main__':
    print('Star 1:', star1())
    print('Star 2:', star2())
