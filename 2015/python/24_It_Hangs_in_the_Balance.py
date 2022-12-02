from aoc import *
from itertools import groupby
import math


def has_subset_sum(values, expected):
    subset = {(i, 0) for i in range(len(values)+1)}
    for i in range(1, len(values)+1):
        for j in range(1, expected+1):
            if j < values[i-1] and (i-1, j) in subset:
                subset.add((i, j))
            if j <= values[i-1] and (i-1, j) in subset or (i-1, j-values[i-1]) in subset:
                subset.add((i, j))
    return (len(values), expected) in subset


def find_subsets(values, expected):
    dp = [[False] * (expected+1) for j in range(len(values))]
    for i in range(len(values)):
        dp[i][0] = True
    if values[0] <= expected:
        dp[0][values[0]] = True

    for i in range(1, len(values)):
        for j in range(1, expected+1):
            if values[i] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-values[i]]
    if not dp[len(values)-1][expected]:
        print('LALALA')
    
    subsets = []
    def find_recursive(i, j, p):
        if j == 0:
            subsets.append(list(p))
            return
        elif i == 0 and dp[i][j]:
            p.append(values[i])
            subsets.append(list(p))
            p.pop()
            return
        
        if dp[i-1][j]:
            find_recursive(i-1, j, p)
        if j >= values[i] and dp[i-1][j-values[i]]:
            p.append(values[i])
            find_recursive(i-1, j-values[i], p)
            p.pop()
    find_recursive(len(values)-1, expected, [])
    return subsets


def subset_score(s):
    return (len(s), math.prod(s))


def has_non_overlaping_subsets(front, subsets, expected):
    count = 0
    for s in subsets:
        if not (s & front):
            count += 1
            if count == expected:
                return True
    return False


def find_optimal_front(presents, n):
    expected = sum(presents) // n
    subsets = [set(x) for x in find_subsets(presents, expected)]
    subsets.sort(key=subset_score)
    for front in subsets:
        if has_non_overlaping_subsets(front, subsets, n-1):
            return front



presents = read()
print('Star 1:', math.prod(find_optimal_front(presents, 3)))
print('Star 1:', math.prod(find_optimal_front(presents, 4)))