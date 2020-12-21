import math
import re
from collections import defaultdict
from itertools import product, chain

CHAINLENGTH = 12


def tile_to_borders(tile):
    row1, last_row = tile[0], tile[-1]
    col1 = ''.join([tile[x][0] for x in range(len(tile))])
    last_col = ''.join([tile[x][-1] for x in range(len(tile))])
    return [row1, last_row, col1, last_col]


def read_input():
    tiles = {}
    buf = []
    cur = None
    for line in open('input.txt'):
        line = line.strip()
        if 'Tile' in line:
            if buf:
                tiles[cur] = tile_to_borders(buf)
            cur = line.split()[1][:-1]
            buf = []
        elif line:
            buf.append(line)
    tiles[cur] = tile_to_borders(buf)
    return tiles


def adj_right(a, b):
    return a[-1] == b[-2]


def adj_bottom(a, b):
    return a[1] == b[0]


def vert_flip(tile):
    return [tile[1], tile[0], ''.join(reversed(tile[2])), ''.join(reversed(tile[3]))]


def hor_flip(tile):
    return [''.join(reversed(tile[0])), ''.join(reversed(tile[1])), tile[3], tile[2]]


def rotate(tile):
    return [''.join(reversed(tile[2])), ''.join(reversed(tile[3])), tile[1], tile[0]]


def flips(tile):
    for hor, vert in product([False, True], repeat=2):
        f = tile
        if hor:
            f = hor_flip(f)
        if vert:
            f = vert_flip(f)
        yield vert, hor, f


def rotations(tile):
    r = tile
    for i in range(4):
        yield i, r
        r = rotate(r)


def combs(tile):
    for vert, hor, f in flips(tile):
        for i, r in rotations(f):
            yield vert, hor, i, r


def graph(tiles):
    vertices = set()
    for key in tiles:
        for vert, hor, i, r in combs(tiles[key]):
            vertices.add((key, tuple(r)))
    g_right = dict()
    for v in vertices:
        g_right[v] = [a for a in vertices if a[0] != v[0] and adj_right(v[1], a[1])]
    g_bottom = dict()
    for v in vertices:
        g_bottom[v] = [a for a in vertices if a[0] != v[0] and adj_bottom(v[1], a[1])]
    return g_right, g_bottom


def adj12(start, g):
    rows = set()
    q = [(start,)]
    while q:
        cur = q.pop()
        for a in g[cur[-1]]:
            if any(a[0] == c[0] for c in cur):
                continue
            if len(cur) == CHAINLENGTH-1:
                rows.add(cur + (a,))
            else:
                q.append(cur + (a,))
    return rows


def row_graph(rows):
    g = dict()
    for row in rows:
        g[row] = [a for a in rows if all(adj_bottom(row[i][1], a[i][1]) for i in range(len(row)))]
    return g


def adjrows12(start, g):
    rows = set()
    q = [(start,)]
    while q:
        cur = q.pop()
        visited = set()
        for row in cur:
            for tile in row:
                visited.add(tile[0])
        for a in g[cur[-1]]:
            if any(t[0] in visited for t in a):
                continue
            if len(cur) == CHAINLENGTH-1:
                rows.add(cur + (a,))
            else:
                q.append(cur + (a,))
    return rows


def checkphoto(photo):
    tiles = set()
    for row in photo:
        tiles.update(t[0] for t in row)
    return len(tiles) == len(photo) ** 2


def arrange(tiles):
    size = int(math.sqrt(len(tiles)))
    print('N Tiles:', len(tiles), 'size', size)
    g_right, g_bottom = graph(tiles)
    print('g_right', len(g_right), 'g_bottom', len(g_bottom))
    rows = set()
    for start in g_right:
        rows |= adj12(start, g_right)
    print('rows', len(rows))
    g_rows = row_graph(rows)
    print('rows graph', len(g_rows))
    photos = set()
    for start in g_rows:
        photos |= adjrows12(start, g_rows)
    print('photos', len(photos))
    return next(iter(photos))


def star1():
    tiles = read_input()
    photo = arrange(tiles)
    muls = (photo[0][0], photo[0][-1], photo[-1][0], photo[-1][-1])
    print(math.prod(int(m[0]) for m in muls))


def vert_flip_img(tile):
    return list(reversed(tile))


def hor_flip_img(tile):
    return [''.join(reversed(row)) for row in tile]


def rotate_img(tile, n):
    cur = list(tile)
    for i in range(n):
        nxt = list(cur)
        for row in range(len(tile)):
            nxt[row] = ''.join(reversed(list(cur[col][row] for col in range(len(tile)))))
        cur = nxt
    return cur



def transimg(vert, hor, i, tile):
    cur = list(tile)
    if vert:
        cur = vert_flip_img(cur)
    if hor:
        cur = hor_flip_img(cur)
    cur = rotate_img(cur, i)
    return cur


def findcomb(tile, c):
    borders = tile_to_borders(tile)
    for vert, hor, i, r in combs(borders):
        if c == tuple(r):
            return transimg(vert, hor, i, tile)
    print(tile)
    raise Exception('AAAAAAAAAAA')


def cut(img):
    return [row[1:-1] for row in img[1:-1]]


def buildimage(photo, tiles):
    imgtiles = [[findcomb(tiles[t[0]], t[1]) for t in row] for row in photo]
    imgtiles = [[cut(t) for t in row] for row in imgtiles]
    img = []
    for rowt in imgtiles:
        for row in range(len(rowt[0])):
            img.append(''.join(chain.from_iterable(t[row] for t in rowt)))
    return img


def printimg(img):
    print()
    print('IMAGE')
    for row in img:
        print(row)


def read_input2():
    tiles = {}
    buf = []
    cur = None
    for line in open('input.txt'):
        line = line.strip()
        if 'Tile' in line:
            if buf:
                tiles[cur] = buf
            cur = line.split()[1][:-1]
            buf = []
        elif line:
            buf.append(line)
    tiles[cur] = buf
    return tiles


def find_monster(img):
    import regex
    monster = ['..................#.',
               '#....##....##....###',
               '.#..#..#..#..#..#...']
    for row in range(len(img)-3):
        for m in regex.finditer(monster[0], img[row], overlapped=True):
            if regex.match(monster[1], img[row+1][m.start():]) and regex.match(monster[2], img[row+2][m.start():]):
                yield row, m.start(), row+3, m.end()


def countn(img, r1, c1, r2, c2):
    c = 0
    for row in range(r1, r2):
        for col in range(c1, c2):
            if img[row][col] == '#':
                c += 1
    return c

def star2():
    borders = read_input()
    photo = arrange(borders)

    tiles = read_input2()
    # tile = tiles[photo[0][0][0]]
    # printimg(tile)
    # printimg(transimg(False, False, 1, tile))
    img = buildimage(photo, tiles)
    # printimg(img)
    for vert, hor in product([False, True], repeat=2):
        for r in range(4):
            cur = transimg(vert, hor, r, img)
            # printimg(cur)
            monsters = list(find_monster(cur))
            if monsters:
                globalc = countn(cur, 0, 0, len(cur), len(cur))
                for m in monsters:
                    globalc -= 15
                print(globalc)
                return

print('Star 1:')
star1()
print('Star 2:')
star2()