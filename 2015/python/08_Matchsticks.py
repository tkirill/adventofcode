import json


lines = [l.strip() for l in open('08_input.txt')]

src_sum = sum(len(l) for l in lines)
s1_sum = sum(len(eval(l)) for l in lines)
s2_sum = sum(len(json.dumps(l)) for l in lines)

print('Star 1:', src_sum - s1_sum)
print('Star 2:', s2_sum - src_sum)