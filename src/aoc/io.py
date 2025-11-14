import __main__
from pathlib import Path
from typing import Optional


def get_input_filename(year: int, day: int) -> Path:
    input_filename = Path(__file__).parent.joinpath(f'year{year}', f'{day:02d}_input.txt')
    if not input_filename.exists():
        raise FileNotFoundError(str(input_filename))
    return input_filename


def readraw(strip=True):
    input_filename = get_input_filename()
    with input_filename.open() as f:
        result = f.read()
        return result.strip() if strip else result


def readlines(year: int, day: int, strip: bool=True, strip_chars: Optional[str]=None) -> list[str]:
    input_filename = get_input_filename(year, day)
    with input_filename.open() as f:
        return [l.strip(strip_chars) if strip else l for l in f]
