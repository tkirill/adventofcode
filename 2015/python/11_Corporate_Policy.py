import string


ENG = string.ascii_lowercase


def parse26(s: str) -> int:
    r = 0
    for i, c in enumerate(reversed(s)):
        r += 26**i * ENG.index(c)
    return r


def str26(x: int) -> str:
    digits = [ENG[x % 26]]
    x //= 26
    while x > 0:
        x, cur = divmod(x, 26)
        digits.append(ENG[cur])
    return ''.join(reversed(digits))


def is_valid(x: int) -> bool:
    s = str26(x)
    if not any(ENG[i-3:i] in s for i in range(3, len(ENG)+1)):
        return False
    if any(x in s for x in 'iol'):
        return False
    if sum(1 for x in ENG if x*2 in s) < 2:
        return False
    return True


cur = parse26(open('11_input.txt').readline().strip())
while not is_valid(cur):
    cur += 1
print('Star 1:', str26(cur))

cur += 1
while not is_valid(cur):
    cur += 1
print('Star 2:', str26(cur))