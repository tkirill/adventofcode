from aoc import *
from itertools import count
from more_itertools import nth
from hashlib import md5
import re
from collections import deque, Counter


def hashes(salt: str, repeat: int=0) -> Iterable[str]:
    for id in count():
        cur = md5((salt + str(id)).encode('ascii')).hexdigest()
        for _ in range(repeat):
            cur = md5(cur.encode('ascii')).hexdigest()
        yield id, cur


def find_same(s: str) -> tuple[str, set[str]]:
    m3 = re.search(r'(.)\1\1', s)
    same3 = m3.group(1) if m3 else None
    same5 = set(m.group(1) for m in re.finditer(r'(.)\1\1\1\1', s))
    return same3, same5


def find_keys(hashes: Iterable[tuple[int, str]]) -> Iterable[tuple[int, str]]:
    it = iter(hashes)
    window = deque()
    total_same5 = Counter()
    while True:
        id, hash = next(it)
        same3, same5 = find_same(hash)
        window.append((id, same3, same5))
        total_same5.update(same5)
        if len(window) < 1001:
            continue

        id, same3, same5 = window.popleft()
        total_same5.subtract(same5)
        if same3 and total_same5[same3] > 0:
            yield id


salt = read()[0]
print('Star 1:', nth(find_keys(hashes(salt)), 63))
print('Star 1:', nth(find_keys(hashes(salt, 2016)), 63))