from utils import *
from tqdm import trange


def step(x, y, vx, vy):
    x += vx
    y += vy
    vx += -sign(vx)
    vy -= 1
    return x, y, vx, vy


def sim(vx, vy):
    x, y = 0, 0
    maxy = 0
    while True:
        if 209 <= x <= 238 and -86 <= y <= -59:
            return maxy
        if vx == 0 and not 209 <= x <= 238:
            return None
        if y < -86:
            return None
        x, y, vx, vy = step(x, y, vx, vy)
        maxy = max(y, maxy)


maxy = 0
cc = 0
for vx in trange(0, 300, desc='Values of VX'):
    for vy in range(-100, 300):
        my = sim(vx, vy)
        if my is not None:
            cc += 1
            if my > maxy:
                maxy = my
print('Star 1:', maxy)
print('Star 2:', cc)