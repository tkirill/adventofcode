import __main__
from pathlib import Path
import re
from typing import Any


###################
### Simple read ###
###################


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


##################
### Smart read ###
##################


def parsevalue(s: str, parse=int) -> str | Any:
    try:
        return parse(s)
    except ValueError:
        return s


def parseline(l: str, sep=r'\s', parse=int) -> str | list[str | Any]:
    l = l.strip()
    if sep:
        parts = [parsevalue(s, parse=parse) for s in re.split(sep, l)]
        return parts[0] if len(parts) == 1 else parts
    return parse(l)


def read(sep=r'\s', parse=int) -> list[str | list[str | Any]]:
    return [parseline(l, sep=sep, parse=parse) for l in readlines()]


def readblocks(sep=r'\s', parse=int):
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
