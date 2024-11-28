import __main__
from pathlib import Path
import re
from typing import Any, Callable


def get_input_filename() -> Path:
    main = Path(__main__.__file__)
    n = re.match(r'\d\d', main.stem)
    input_filename = main.with_name(f'{n.group()}_input.txt')
    if not input_filename.exists():
        raise FileNotFoundError(str(input_filename))
    return input_filename


def readraw():
    input_filename = get_input_filename()
    with input_filename.open() as f:
        return f.read().strip()


def readlines() -> list[str]:
    input_filename = get_input_filename()
    with input_filename.open() as f:
        return [l.strip() for l in f]


def readsplit(sep='\s') -> list[list[str]]:
    return [re.split(sep, l) for l in readlines()]


def allints(s: str) -> list[int]:
    return [int(x.group()) for x in re.finditer(r'-?\d+', s)]


def parsevalue[TValue](s: str, parse: Callable[[str], TValue]=int) -> str | TValue:
    try:
        return parse(s)
    except ValueError:
        return s


def parseline[TValue](l: str, sep: str=r'\s', parse: Callable[[str], TValue]=int) -> str | TValue | list[str | TValue]:
    l = l.strip()
    if sep:
        parts = [parsevalue(s, parse=parse) for s in re.split(sep, l)]
        return parts[0] if len(parts) == 1 else parts
    return parsevalue(l, parse=parse)


def parselines[TValue](lines: list[str], sep: str=r'\s', parse: Callable[[str], TValue]=int) -> list[str | TValue | list[str | TValue]]:
    return [parseline(l, sep, parse) for l in lines]


def read[TValue](sep: str=r'\s', parse: Callable[[str], TValue]=int) -> list[str | TValue | list[str | TValue]]:
    return parselines(readlines(), sep, parse)


def readblocks[TValue](sep: str=r'\s', parse: Callable[[str], TValue]=int):
    result = []
    tmp = []
    for l in readlines():
        if not l:
            result.append(tmp)
            tmp = []
        else:
            tmp.append(parseline(l, sep=sep, parse=parse))
    result.append(tmp)
    return result