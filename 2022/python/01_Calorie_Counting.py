def read_input():
    elfs = open('01_input.txt').read().strip().split('\n\n')
    return [sum(map(int, x.split())) for x in elfs]


elfs = read_input()
elfs.sort()

print('Star 1:', elfs[-1])
print('Star 2:', sum(elfs[-3:]))