lines = [x.strip() for x in open('02_input.txt')]
presents = [tuple(int(xx) for xx in x.split('x')) for x in lines]

total = 0
for p in presents:
    sides = [p[0]*p[1], p[1]*p[2], p[0]*p[2]]
    total += sum(sides) * 2 + min(sides)
print('Star 1:', total)

total = 0
for p in presents:
    sides = [p[0]+p[1], p[1]+p[2], p[0]+p[2]]
    total += min(sides)*2 + p[0]*p[1]*p[2]
print('Star 2:', total)