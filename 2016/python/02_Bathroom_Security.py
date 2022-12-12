from aoc import *


KEYPAD1 = list(filter(None, '''
123
456
789
'''.splitlines()))


KEYPAD2 = list(filter(None, '''
  1
 234
56789
 ABC
  D
'''.splitlines()))


instructions = read()


cur = Vec2(1, 1)
code = []
for i in instructions:
    for c in i:
        tmp = cur.step(c)
        if 0 <= tmp.x <= 2 and 0 <= tmp.y <= 2:
            cur = tmp
    code.append(KEYPAD1[cur.y][cur.x])
print('Star 1:', ''.join(code))


cur = Vec2(2, 2)
code = []
for i in instructions:
    for c in i:
        tmp = cur.step(c)
        if (tmp-2).mdist() <= 2:
            cur = tmp
    code.append(KEYPAD2[cur.y][cur.x])
print('Star 2:', ''.join(code))


### Alternative solution using just complex numbers ###


cur = 1 + 1j
code = []
for i in instructions:
    for c in i:
        delta = -1 if c == 'L' else 1 if c == 'R' else -1j if c == 'U' else 1j
        tmp = cur + delta
        if 0 <= tmp.real <= 2 and 0 <= tmp.imag <= 2:
            cur = tmp
    code.append(KEYPAD1[int(cur.imag)][int(cur.real)])
print('Star 1 (complex):', ''.join(code))


cur = 2 + 2j
code = []
for i in instructions:
    for c in i:
        delta = -1 if c == 'L' else 1 if c == 'R' else -1j if c == 'U' else 1j
        tmp = cur + delta
        if abs(tmp.real-2) + abs(tmp.imag-2) <= 2:
            cur = tmp
    code.append(KEYPAD2[int(cur.imag)][int(cur.real)])
print('Star 2 (complex):', ''.join(code))