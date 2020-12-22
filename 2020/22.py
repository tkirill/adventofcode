from collections import deque
from itertools import islice


def read_input():
    decks = []
    for line in open('input.txt'):
        line = line.strip()
        if 'Player' in line:
            decks.append(deque())
            cur = decks[-1]
        elif line:
            cur.append(int(line))
    return decks


def play(decks):
    while all(decks):
        a, b = decks[0][0], decks[1][0]
        if a > b:
            decks[0].rotate(-1)
            decks[0].append(decks[1].popleft())
        else:
            decks[1].rotate(-1)
            decks[1].append(decks[0].popleft())


def star1():
    decks = read_input()
    play(decks)
    winner = next(filter(None, decks))
    print(sum(i * winner.pop() for i in range(1, len(winner)+1)))


def play2(decks):
    mem = set()
    while all(decks):
        cur_state = (tuple(decks[0]), tuple(decks[1]))
        if cur_state in mem:
            return True
        mem.add(cur_state)
        a, b = decks[0].popleft(), decks[1].popleft()
        if a > len(decks[0]) or b > len(decks[1]):
            if a > b:
                decks[0].append(a)
                decks[0].append(b)
            else:
                decks[1].append(b)
                decks[1].append(a)
        else:
            subdecks = [deque(islice(decks[0], a)), deque(islice(decks[1], b))]
            first_won = play2(subdecks)
            if first_won:
                decks[0].append(a)
                decks[0].append(b)
            else:
                decks[1].append(b)
                decks[1].append(a)
    return bool(decks[0])


def star2():
    decks = read_input()
    winner = decks[0] if play2(decks) else decks[1]
    print(sum(i * winner.pop() for i in range(1, len(winner) + 1)))


print('Star 1:')
star1()
print('Star 2:')
star2()