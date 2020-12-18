import re


def reverse_polish_notation(line, prec):
    stack = list()
    output = ''
    for c in line:
        if c == ' ':
            continue
        if re.match('\d', c):
            output += c
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and prec[stack[-1]] >= prec[c]:
                output += stack.pop()
            stack.append(c)
    while stack:
        output += stack.pop()
    return output


def calc(line, prec):
    line = reverse_polish_notation(line, prec)
    stack = list()
    for c in line:
        if re.match('\d', c):
            stack.append(int(c))
        else:
            a, b = stack.pop(), stack.pop()
            stack.append(eval(f"{a} {c} {b}"))
    return stack.pop()


def star1():
    prec = {'*': 1, '+': 1}
    print(sum(calc(line.strip(), prec) for line in open('input.txt')))


def star2():
    prec = {'*': 1, '+': 2}
    print(sum(calc(line.strip(), prec) for line in open('input.txt')))


print('Star 1:')
star1()
print('Star 2:')
star2()