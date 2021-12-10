from utils import *


lines = readlines('10_input.txt')
scores1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
scores2 = {'(': 1, '[': 2, '{': 3, '<': 4}
check = {')': '(', ']': '[', '}': '{', '>': '<'}


def find_mistake(line):
    q = []
    for x in line:
        if x in check.values():
            q.append(x)
        elif q and q[-1] == check[x]:
            q.pop()
        else:
            return scores1[x], None
    score2 = 0
    for x in reversed(q):
        score2 *= 5
        score2 += scores2[x]
    return None, score2


score1, score2 = 0, []
for line in lines:
    s1, s2 = find_mistake(line)
    if s1 is not None:
        score1 += s1
    else:
        score2.append(s2)
score2.sort()
print('Star 1:', score1)
print('Star 2:', score2[len(score2) // 2])