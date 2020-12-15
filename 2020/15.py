def play(turn_count):
    ns = [0,3,1,6,7,5]
    mem = {ns[i]: i for i in range(len(ns)-1)}
    prev = ns[-1]
    count = len(ns)
    for i in range(turn_count-len(ns)):
        spoken = mem.get(prev, None)
        mem[prev] = count-1
        prev = 0 if spoken is None else count-1-spoken
        count += 1
    return prev


print('Star 1:')
print(play(2020))
print('Star 2:')
print(play(30000000))