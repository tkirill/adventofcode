from itertools import chain


def adj(row, col, f):
    for dr in [-1, 0, 1]:
        cr = row + dr
        if cr < 0 or cr >= len(f):
            continue
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            cc = col + dc
            if cc < 0 or cc >= len(f[cr]):
                continue
            yield f[cr][cc]


def star1():
    f = [list(line.strip()) for line in open('input.txt')]

    changed = True
    while changed:
        nf = [list(row) for row in f]
        changed = False
        for row in range(len(f)):
            for col in range(len(f[0])):
                occ = sum(1 for x in adj(row, col, f) if x == '#')
                if f[row][col] == 'L' and occ == 0:
                    nf[row][col] = '#'
                    changed = True
                elif f[row][col] == '#' and occ >= 4:
                    nf[row][col] = 'L'
                    changed = True
        f = nf

    print(sum(1 for c in chain.from_iterable(f) if c == '#'))


def star2():
    f = [list(line.strip()) for line in open('input.txt')]

    def infield(row, col):
        return 0 <= row < len(f) and 0 <= col < len(f[0])

    def find_occ(sr, sc, dr, dc):
        cr, cc = sr, sc
        while True:
            cr += dr
            cc += dc
            if not infield(cr, cc):
                return 0
            if f[cr][cc] == 'L':
                return 0
            if f[cr][cc] == '#':
                return 1

    def count_occ(row, col):
        result = 0
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue
                result += find_occ(row, col, dr, dc)
        return result

    changed = True
    while changed:
        changed = False
        nf = [list(row) for row in f]
        for row in range(len(f)):
            for col in range(len(f[0])):
                occ = count_occ(row, col)
                if f[row][col] == 'L' and occ == 0:
                    nf[row][col] = '#'
                    changed = True
                elif f[row][col] == '#' and occ >= 5:
                    nf[row][col] = 'L'
                    changed = True
        f = nf

    print(sum(sum(1 for c in row if c == '#') for row in f))


print('Star 1:')
star1()
print('Star 2:')
star2()