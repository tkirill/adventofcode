from aoc import *


def find_first(s, len_):
    for i in range(len(s)):
        if len(set(s[i:i+len_])) == len_:
            return i+len_


line = read()[0]
print('Star 1:', find_first(line, 4))
print('Star 2:', find_first(line, 14))


### Alternative solution using regular expressions ###

build_re = lambda n: ''.join(rf'(.)(?!.{{,{i}}}\{n-1-i})' for i in range(n-2,-1,-1)) + '.'
print('Star 1:', re.search(build_re(4), line).end())
print('Star 2:', re.search(build_re(14), line).end())