from aoc import *
import re


MARK = re.compile(r'\((\d+)x(\d+)\)')


def decompress1(archive: str) -> str:
    total = 0
    cur = 0
    while cur < len(archive):
        nxt = MARK.search(archive, pos=cur)
        if not nxt:
            total += len(archive) - cur
            cur = len(archive)
            break
        total += nxt.start() - cur
        len_, times = allints(nxt.group())
        total += len_ * times
        cur = nxt.end() + len_
    return total


def decompress2(archive: str) -> str:
    total = 0
    cur = 0
    while cur < len(archive):
        nxt = MARK.search(archive, pos=cur)
        if not nxt:
            total += len(archive) - cur
            cur = len(archive)
            break
        total += nxt.start() - cur
        len_, times = allints(nxt.group())
        total += decompress2(archive[nxt.end():nxt.end()+len_]) * times
        cur = nxt.end() + len_
    return total


archive = readraw()
print('Star 1:', decompress1(archive))
print('Star 2:', decompress2(archive))