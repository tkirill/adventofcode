import re


def read_input():
    rules = {}
    messages = []
    for line in open('input.txt'):
        line = line.strip()
        if ':' in line:
            key, rule = line.split(': ')
            rules[key] = rule
        elif line:
            messages.append(line)
    return rules, messages


def build_regexp(rules):
    result = rules['0']
    while True:
        next = re.sub('\d+', lambda x: f'({rules[x.group(0)]})', result)
        print(next)
        if next == result:
            return '^' + result.replace('"', '').replace(' ', '') + '$'
        result = next


def is_valid(msg, rules):
    regexp = build_regexp(rules)
    return re.match(regexp, msg) is not None


def star1():
    rules, messages = read_input()
    r = build_regexp(rules)
    print(sum(1 for x in messages if re.match(r, x) is not None))


def star2():
    rules, messages = read_input()
    rules['8'] = '42+'
    rules['11'] = '(?P<yolo>42(?&yolo)?31)'
    r = build_regexp(rules)
    import regex
    print(sum(1 for x in messages if regex.match(r, x) is not None))


print('Star 1:')
star1()
print('Star 2:')
star2()