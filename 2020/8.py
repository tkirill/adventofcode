def read_app():
    for line in open('input.txt'):
        line = line.strip()
        cmd, arg = line.split(' ')
        yield (cmd, int(arg))


def find_loop(app):
    acc = 0
    ip = 0
    visited = set()
    while ip not in visited:
        visited.add(ip)
        cmd, arg = app[ip]
        if cmd == 'acc':
            acc += arg
            ip += 1
        elif cmd == 'jmp':
            ip += arg
        else:
            ip += 1
    return acc


def star1():
    app = list(read_app())
    print(find_loop(app))


def find_loop2(app):
    acc = 0
    ip = 0
    visited = set()
    while ip not in visited:
        if ip >= len(app):
            return False, acc
        visited.add(ip)
        cmd, arg = app[ip]
        if cmd == 'acc':
            acc += arg
            ip += 1
        elif cmd == 'jmp':
            ip += arg
        else:
            ip += 1
    return True, acc


def star2():
    app = list(read_app())
    for i in range(len(app)):
        nextapp = list(app)
        cmd, arg = nextapp[i]
        if cmd == 'jmp':
            nextapp[i] = ('nop', arg)
        elif cmd == 'nop':
            nextapp[i] = ('jmp', arg)
        cycled, acc = find_loop2(nextapp)
        if not cycled:
            print(acc)
            break


print('Star 1:')
star1()
print('Star 2:')
star2()