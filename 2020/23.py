from array import array
from itertools import islice


class CircularBuffer:
    def __init__(self, items):
        self.cur = items[0]
        self.next = array('i', (0 for _ in range(len(items))))
        for i in range(len(items)-1):
            self.next[items[i]] = items[i+1]
        self.next[items[-1]] = items[0]

    def popnext(self):
        a = self.next[self.cur]
        b = self.next[a]
        c = self.next[b]
        self.next[self.cur] = self.next[c]
        return [a, b, c]

    def insertafter(self, cup, items):
        self.next[items[2]] = self.next[cup]
        self.next[cup] = items[0]
        self.next[items[0]] = items[1]
        self.next[items[1]] = items[2]

    def move(self):
        self.cur = self.next[self.cur]

    def getafter(self, cup):
        cur = cup
        while self.next[cur] != cup:
            cur = self.next[cur]
            yield cur


def star1():
    maxcup = 8
    cups = CircularBuffer([int(x)-1 for x in '157623984'])
    for move_n in range(100):
        next3 = cups.popnext()
        dst = cups.cur - 1 if cups.cur > 0 else maxcup
        while dst in next3:
            dst = dst - 1 if dst > 0 else maxcup
        cups.insertafter(dst, next3)
        cups.move()
    print(''.join(str(x+1) for x in cups.getafter(0)))


def star2():
    tmp = [int(x)-1 for x in '157623984'] + list(range(9, 1000*1000))
    maxcup = tmp[-1]
    cups = CircularBuffer(tmp)
    for move_n in range(10*1000*1000):
        next3 = cups.popnext()
        dst = cups.cur - 1 if cups.cur > 0 else maxcup
        while dst in next3:
            dst = dst - 1 if dst > 0 else maxcup
        cups.insertafter(dst, next3)
        cups.move()
    answer = [x+1 for x in islice(cups.getafter(0), 2)]
    print(answer[0]*answer[1])


print('Star 1:')
star1()
print('Star 2:')
star2()