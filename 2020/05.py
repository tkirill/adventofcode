def get_id(line):
    return int(line.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0'), 2)


def star1():
    print(max(get_id(line.strip()) for line in open('input.txt')))


def star2():
    ids = [get_id(line.strip()) for line in open('input.txt')]
    ids.sort()
    for i in range(len(ids)):
        if ids[i+1] - ids[i] == 2:
            print(ids[i]+1)
            break


print('Star 1:')
star1()
print('Star 2:')
star2()