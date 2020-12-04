import re


def parse_pspt(lines):
    pspt = {}
    for line in lines:
        for item in line.split(' '):
            key, value = item.split(':')
            pspt[key] = value
    return pspt


def read_pspts():
    result = []
    cur = []
    for line in open('input.txt'):
        line = line.strip()
        if not line:
            result.append(parse_pspt(cur))
            cur = []
            continue
        cur.append(line)
    result.append(parse_pspt(cur))
    return result


def is_valid(p):
    expected = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for e in expected:
        if e not in p:
            return False
    return True


def star1():
    pspts = read_pspts()
    print(sum(1 for p in pspts if is_valid(p)))


def is_valid_number(s, gte, lte):
    try:
        x = int(s)
        return gte <= x <= lte
    except ValueError:
        return False


def is_valid_hgt(s: str):
    return s.endswith('cm') and is_valid_number(s[:-2], 150, 193) \
           or s.endswith('in') and is_valid_number(s[:-2], 59, 76)


def is_valid_hcl(s):
    return re.match('^#[0-9a-f]{6}$', s)


def is_valid_ecl(s):
    return s in 'amb blu brn gry grn hzl oth'.split(' ')


def is_valid_pid(s):
    return re.match('^[0-9]{9}$', s)


def is_valid2(p):
    expected = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for e in expected:
        if e not in p:
            return False
    return is_valid_number(p['byr'], 1920, 2002) and \
           is_valid_number(p['iyr'], 2010, 2020) and \
           is_valid_number(p['eyr'], 2020, 2030) and \
           is_valid_hgt(p['hgt']) and \
           is_valid_hcl(p['hcl']) and \
           is_valid_ecl(p['ecl']) and \
           is_valid_pid(p['pid'])


def star2():
    pspts = read_pspts()
    print(sum(1 for p in pspts if is_valid2(p)))


print('Star 1:')
star1()
print('Star 2:')
star2()