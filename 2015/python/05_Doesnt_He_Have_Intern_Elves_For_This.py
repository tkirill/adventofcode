import re


lines = [l.strip() for l in open('05_input.txt').readlines()]

def is_nice(s: str) -> bool:
    return not re.search('ab|cd|pq|xy', s) and len(re.findall('[aeiou]', s)) >= 3 and re.search(r'(.)\1', s)

def is_really_nice(s: str) -> bool:
    return re.search(r'(..).*\1', s) and re.search(r'(.).\1', s)

print('Star 1:', sum(1 for x in lines if is_nice(x)))
print('Star 2:', sum(1 for x in lines if is_really_nice(x)))

import re