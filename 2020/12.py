deltas = {
    'N': (0, -1),
    'E': (1, 0),
    'W': (-1, 0),
    'S': (0, 1)
}
dirs = ['N', 'E', 'S', 'W']

def star1():
    shipdir = 'E'
    shippos = [0, 0]
    for line in open('input.txt'):
        if line[0] == 'L':
            cur = dirs.index(shipdir)
            dgr = int(line.strip()[1:])
            cur -= dgr // 90
            shipdir = dirs[cur]
        elif line[0] == 'R':
            cur = dirs.index(shipdir)
            dgr = int(line.strip()[1:])
            cur += dgr // 90
            cur %= 4
            shipdir = dirs[cur]
        elif line[0] == 'F':
            x, y = deltas[shipdir]
            dist = int(line.strip()[1:])
            shippos[0] += x*dist
            shippos[1] += y*dist
        else:
            x, y = deltas[line[0]]
            dist = int(line.strip()[1:])
            shippos[0] += x * dist
            shippos[1] += y * dist
    print(abs(shippos[0]) + abs(shippos[1]))


def star2():
    point = [10, -1]
    shippos = [0, 0]
    for line in open('input.txt'):
        if line[0] == 'L':
            dgr = int(line.strip()[1:])
            while dgr > 0:
                point = [point[1], -point[0]]
                dgr -= 90
        elif line[0] == 'R':
            dgr = int(line.strip()[1:])
            while dgr > 0:
                point = [-point[1], point[0]]
                dgr -= 90
        elif line[0] == 'F':
            dist = int(line.strip()[1:])
            shippos[0] += point[0] * dist
            shippos[1] += point[1] * dist
        else:
            x, y = deltas[line[0]]
            dist = int(line.strip()[1:])
            point[0] += x * dist
            point[1] += y * dist
    print(abs(shippos[0]) + abs(shippos[1]))

print('Star 1:')
star1()
print('Star 2:')
star2()
