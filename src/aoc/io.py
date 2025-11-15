from pathlib import Path
from typing import Optional, Callable
import re


def get_input_filename(year: int, day: int) -> Path:
    input_filename = Path(__file__).parent.joinpath(f'year{year}', f'{day:02d}_input.txt')
    if not input_filename.exists():
        raise FileNotFoundError(str(input_filename))
    return input_filename


def readraw(year: int, day: int, strip=True):
    input_filename = get_input_filename(year, day)
    with input_filename.open() as f:
        result = f.read()
        return result.strip() if strip else result


def readlines(year: int, day: int, strip: bool=True, strip_chars: Optional[str]=None) -> list[str]:
    input_filename = get_input_filename(year, day)
    with input_filename.open() as f:
        return [l.strip(strip_chars) if strip else l for l in f]


def readsplit(year: int, day: int, sep=r'\s') -> list[list[str]]:
    return [re.split(sep, l) for l in readlines(year, day)]


def allints(s: str) -> list[int]:
    return [int(x.group()) for x in re.finditer(r'-?\d+', s)]


def parsevalue[TValue](s: str, parse: Callable[[str], TValue]=int) -> str | TValue:
    try:
        return parse(s)
    except ValueError:
        return s


def parseline[TValue](
        l: str,
        sep: str=r'\s',
        parse: Callable[[str], TValue]=int,
        skip_empty=True,
        strip: bool=True,
        strip_chars: Optional[str]=None) -> str | TValue | list[str | TValue]:
    if strip:
        l = l.strip(strip_chars)
    if sep:
        parts = [parsevalue(s, parse=parse) for s in re.split(sep, l) if s or not skip_empty]
        return parts[0] if len(parts) == 1 else parts
    return parsevalue(l, parse=parse)


def parselines[TValue](lines: list[str], sep: str=r'\s', parse: Callable[[str], TValue]=int, skip_empty=True) -> list[str | TValue | list[str | TValue]]:
    return [parseline(l, sep, parse, skip_empty) for l in lines]


def read[TValue](year: int,
                 day: int,
                 sep: str=r'\s',
                 parse: Callable[[str], TValue]=int,
                 skip_empty=True) -> list[str | TValue | list[str | TValue]]:
    return parselines(readlines(year, day), sep, parse, skip_empty)


def readblocks[TValue](year: int,
                       day: int,
                       sep: str=r'\s',
                       parse: Callable[[str], TValue]=int,
                       strip: bool=True,
                       strip_chars: Optional[str]=None):
    result = []
    tmp = []
    for l in readlines(year, day, strip=strip, strip_chars=strip_chars):
        if not l:
            result.append(tmp)
            tmp = []
        else:
            tmp.append(parseline(l, sep=sep, parse=parse, strip=strip, strip_chars=strip_chars))
    result.append(tmp)
    return result
