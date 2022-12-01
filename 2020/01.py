def star1():
    n = set(int(s.strip()) for s in open('input.txt'))
    for x in n:
        if 2020-x in n:
            print(x * (2020-x))
            return


print('Star 1:')
star1()


def star2():
    n = set(int(s.strip()) for s in open('input.txt'))
    for x in n:
        for y in n:
            if 2020 -x - y in n:
                print(x*y*(2020-x-y))
                return


print('Star2:')
star2()