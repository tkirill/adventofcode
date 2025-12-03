import itertools, functools, more_itertools, math

from aoc.io import read, readlines, allints
from aoc import board, vec2, grid, algorithm, interval, math as amath, rectangle, walker


def idx(l: list, x, start=0):
    try:
        return l.index(x, start)
    except:
        return -1


def biggest(bank: list[int]):
    for fd in range(9, 0, -1):
        fdi = idx(bank, fd)
        if fdi == -1:
            continue
        for sd in range(9, 0, -1):
            sdi = idx(bank, sd, fdi+1)
            if sdi != -1:
                return fd*10+sd


def biggest12(bank: list[int]) -> int:
    for fd in range(9, 0, -1):
        fdi = idx(bank, fd)
        if fdi == -1:
            continue
        for sd in range(9, 0, -1):
            sdi = idx(bank, sd, fdi+1)
            if sdi == -1:
                continue
            for sd3 in range(9, 0, -1):
                sd3i = idx(bank, sd3, sdi+1)
                if sd3i == -1:
                    continue
                for sd4 in range(9, 0, -1):
                    sd4i = idx(bank, sd4, sd3i+1)
                    if sd4i == -1:
                        continue
                    for sd5 in range(9, 0, -1):
                        sd5i = idx(bank, sd5, sd4i+1)
                        if sd5i == -1:
                            continue
                        for sd6 in range(9, 0, -1):
                            sd6i = idx(bank, sd6, sd5i+1)
                            if sd6i == -1:
                                continue
                            for sd7 in range(9, 0, -1):
                                sd7i = idx(bank, sd7, sd6i+1)
                                if sd7i == -1:
                                    continue
                                for sd8 in range(9, 0, -1):
                                    sd8i = idx(bank, sd8, sd7i+1)
                                    if sd8i == -1:
                                        continue
                                    for sd9 in range(9, 0, -1):
                                        sd9i = idx(bank, sd9, sd8i+1)
                                        if sd9i == -1:
                                            continue
                                        for sd10 in range(9, 0, -1):
                                            sd10i = idx(bank, sd10, sd9i+1)
                                            if sd10i == -1:
                                                continue
                                            for sd11 in range(9, 0, -1):
                                                sd11i = idx(bank, sd11, sd10i+1)
                                                if sd11i == -1:
                                                    continue
                                                for sd12 in range(9, 0, -1):
                                                    sd12i = idx(bank, sd12, sd11i+1)
                                                    if sd12i != -1:
                                                        return sd12 + sd11*10 + sd10*100 + sd9*1000+ sd8*10000 + sd7*100_000 + sd6*1_000_000 + sd5*10_000_000 + sd4*100_000_000 + sd3*1_000_000_000+sd*10_000_000_000+fd*100_000_000_000


def star1():
    banks = readlines(2025, 3)
    banks = [[int(x) for x in b] for b in banks]
    return sum(biggest(b) for b in banks)


def star2():
    banks = readlines(2025, 3)
    banks = [[int(x) for x in b] for b in banks]
    return sum(biggest12(b) for b in banks)
