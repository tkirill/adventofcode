def is_valid(line):
    rule, alpha, pwd = line.strip().split(' ')
    gte, lte = rule.split('-')
    gte, lte = int(gte), int(lte)
    alpha = alpha[0]
    return gte <= sum(1 for c in pwd if c == alpha) <= lte


def star1():
    print(sum(1 for line in open('input.txt') if is_valid(line)))


print('Star 1:')
star1()


def is_valid2(line):
    rule, alpha, pwd = line.strip().split(' ')
    pos1, pos2 = rule.split('-')
    pos1, pos2 = int(pos1)-1, int(pos2)-1
    alpha = alpha[0]
    count = int(pwd[pos1] == alpha) + int(pwd[pos2] == alpha)
    return count == 1


def star2():
    print(sum(1 for line in open('input.txt') if is_valid2(line)))


print('Star 2:')
star2()