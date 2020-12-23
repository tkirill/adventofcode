from itertools import islice


class CircularBuffer:
    def __init__(self, items, cur):
        self.cur = cur
        self.next = dict()
        for i in range(len(items)-1):
            self.next[items[i]] = items[i+1]
        self.next[items[-1]] = items[0]

    def popnext(self, n):
        result = []
        for i in range(n):
            nextitem = self.next[self.cur]
            self.next[self.cur] = self.next.pop(nextitem)
            result.append(nextitem)
        return result

    def insertafter(self, cup, items):
        cur = cup
        for x in items:
            self.next[x] = self.next[cur]
            self.next[cur] = x
            cur = x

    def move(self):
        self.cur = self.next[self.cur]

    def getafter(self, cup):
        cur = cup
        while self.next[cur] != cup:
            cur = self.next[cur]
            yield cur


def star1():
    maxcup = 9
    cups = CircularBuffer([int(x) for x in '157623984'], 1)
    for move_n in range(100):
        next3 = cups.popnext(3)
        dst = cups.cur - 1 or maxcup
        while dst in next3:
            dst = dst - 1 or maxcup
        cups.insertafter(dst, next3)
        cups.move()
    print(''.join(str(x) for x in cups.getafter(1)))


star1()


def star2():
    tmp = [int(x) for x in '157623984'] + list(range(10, 1000*1000+1))
    print(len(tmp))
    assert len(tmp) == 1000*1000
    maxcup = tmp[-1]
    cups = CircularBuffer(tmp, 1)
    for move_n in range(10*1000*1000):
        if move_n % (500*1000) == 0:
            print(move_n)
        next3 = cups.popnext(3)
        dst = cups.cur - 1 or maxcup
        while dst in next3:
            dst = dst - 1 or maxcup
        cups.insertafter(dst, next3)
        cups.move()
    answer = list(islice(cups.getafter(1), 2))
    print(answer)
    print(answer[0]*answer[1])


star2()