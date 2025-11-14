from aoc.io import *


SNAFU_TO_DEC = {
    '=': -2,
    '-': -1,
    '0': 0,
    '1': 1,
    '2': 2
}
DEC_TO_SNAFU = '012=-'


def snafu_to_dec(s: str) -> int:
    result = 0
    cur = 1
    for c in reversed(s):
        result += SNAFU_TO_DEC[c] * cur
        cur *= 5
    return result


def dec_to_snafu(n: int) -> str:
    result = []
    while n > 0:
        nxt, d = divmod(n, 5)
        result.append(DEC_TO_SNAFU[d])
        if d >= 3:
            nxt += 1
        n = nxt
    return ''.join(reversed(result))

print('Star 1:', dec_to_snafu(sum(snafu_to_dec(s) for s in readlines())))


# s2d = [s.split() for s in '''1=-0-2     1747
#  12111      906
#   2=0=      198
#     21       11
#   2=01      201
#    111       31
#  20012     1257
#    112       32
#  1=-1=      353
#   1-12      107
#     12        7
#     1=        3
#    122       37'''.splitlines()]
# print('SNAFU -> DEC:')
# for s, e in s2d:
#     print(s, snafu_to_dec(s), e)

# print()
# print('DEC -> SNAFU:')
# for s, e in s2d:
#     print(e, dec_to_snafu(int(e)), s)
