from aoc.io import readlines


DIGITS = '123456789'
DIGIT_WORDS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ALL_DIGITS = list(DIGITS) + DIGIT_WORDS
DIGIT_TO_INT = {d: DIGITS.index(d)+1 for d in DIGITS} | {d: DIGIT_WORDS.index(d)+1 for d in DIGIT_WORDS}


def find_first_and_last_digits(line: str, digits: list[str]) -> int:
    first = min([d for d in digits if d in line], key=line.find)
    last = max([d for d in digits if d in line], key=line.rfind)
    return int(f'{DIGIT_TO_INT[first]}{DIGIT_TO_INT[last]}')


def star1():
    return sum(find_first_and_last_digits(line, DIGITS) for line in readlines(year=2023, day=1))


def star2():
    return sum(find_first_and_last_digits(line, ALL_DIGITS) for line in readlines(year=2023, day=1))


if __name__ == '__main__':
    print('Star 1:', star1())
    print('Star 2:', star2())
