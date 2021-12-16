# https://adventofcode.com/2021/day/3
from utils import *
from collections import Counter


def star1():
    lines = readlines('3_input.txt')
    counters = [Counter(bits) for bits in zip(*lines)]
    gamma, epsilon = [int(''.join(c.most_common()[pos][0] for c in counters), base=2) for pos in [0, -1]]
    print(gamma * epsilon)


print('Star 1:')
star1()


def count_most_common(lines):
    count_zeroes = [0] * len(lines[0])
    for line in lines:
        for i, c in enumerate(line):
            if c == '0':
                count_zeroes[i] += 1
    result = [0] * len(count_zeroes)
    for i, c in enumerate(count_zeroes):
        is_one = c < (len(lines) / 2)
        if is_one:
            result[i] = 1
    return result


def find_oxy(lines):
    for i in range(len(lines[0])):
        cnts = Counter(line[i] for line in lines)
        b = '1' if cnts['1'] >= cnts['0'] else '0'
        tmp = [line for line in lines if line[i] == b]
        if len(tmp) == 1:
            return int(''.join(tmp[0]), base=2)
        lines = tmp


def find_co2(lines):
    for i in range(len(lines[0])):
        cnts = Counter(line[i] for line in lines)
        b = '1' if cnts['1'] < cnts['0'] else '0'
        tmp = [line for line in lines if line[i] == b]
        if len(tmp) == 1:
            return int(''.join(tmp[0]), base=2)
        lines = tmp


def star2():
    lines = readlines('3_input.txt')
    oxy, co2 = find_oxy(lines), find_co2(lines)
    print(oxy, co2)
    print(oxy * co2)


star2()