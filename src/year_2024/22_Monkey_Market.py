from aoc.io import *
import itertools as itls
import more_itertools as mtls


def calc_secrets(secrets: list[int], n: int):
    result = [[0] * 2001 for _ in range(len(secrets))]
    for i, v in enumerate(secrets):
        result[i][0] = v
    for i in range(1, n+1):
        for j in range(len(result)):
            tmp = result[j][i-1]
            tmp = (tmp ^ (tmp * 64)) % 16777216
            tmp = (tmp ^ (tmp // 32)) % 16777216
            tmp = (tmp ^ (tmp * 2048)) % 16777216
            result[j][i] = tmp
    return result


def calc_sequences(secrets: list[list[int]]):
    diffs = []
    for row in secrets:
        diffs.append([(b%10)-(a%10) for a, b in itls.pairwise(row)])
    result = []
    for i, row in enumerate(diffs):
        result.append({})
        for j, s in enumerate(mtls.sliding_window(row, 4)):
            result[-1].setdefault(s, secrets[i][j + 4]%10)
    return result


def find_best_seq(seqs: list[dict[tuple[int, int, int, int], int]]):
    cache = {}
    best = 0
    for s in itls.chain.from_iterable(x.keys() for x in seqs):
        if s not in cache:
            tmp = sum(x.get(s, 0) for x in seqs)
            cache[s] = tmp
            if tmp > best:
                best = tmp
    return best


secrets = read()
s2000 = calc_secrets(secrets, 2000)
print('Star 1:', sum(r[-1] for r in s2000))
seqs = calc_sequences(s2000)
print('Star 2:', find_best_seq(seqs))
