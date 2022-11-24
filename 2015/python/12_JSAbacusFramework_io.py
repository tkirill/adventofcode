import re
import json

s = open('12_input.txt').read().strip()
print('Star 1:', sum(int(m.group(0)) for m in re.finditer('-?\d+', s)))


def visitsum(cur):
    if isinstance(cur, int):
        return cur
    if isinstance(cur, list):
        return sum(visitsum(v) for v in cur)
    if isinstance(cur, dict):
        if any(isinstance(v, str) and v == 'red' for v in cur.values()):
            return 0
        return sum(visitsum(v) for v in cur.values())
    return 0
    

jj = json.loads(s)
print('Star 2:', visitsum(jj))