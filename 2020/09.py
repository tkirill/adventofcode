def star1():
    n = [int(s.strip()) for s in open('input.txt')]
    for i in range(25, len(n)):
        is_valid = False
        for x in range(i-25, i):
            for y in range(x+1, i):
                if n[x] + n[y] == n[i]:
                    is_valid = True
                    break
        if not is_valid:
            print(n[i])
            break


def star2():
    n = [int(s.strip()) for s in open('input.txt')]
    invalid = 41682220
    for r in range(len(n)):
        for l in range(0, r):
            s = sum(n[i] for i in range(l, r+1))
            if s == invalid:
                print('from', l, 'to', r)
                print(min(n[l:r+1]) + max(n[l:r+1]))
                break


print('Star 1')
star1()
print('Star 2')
star2()