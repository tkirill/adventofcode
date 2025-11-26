import argparse
import os
import sys
import dataclasses
from typing import Callable
from pathlib import Path
import re
from functools import cached_property
import requests

import aoc


@dataclasses.dataclass(frozen=True)
class DayInfo:
    
    year: int
    day: int
    name: str
    location: Path
    star1: Callable
    star2: Callable

    @cached_property
    def input(self):
        return self.location.parent.joinpath(f'{self.day:02d}_input.txt')


@dataclasses.dataclass(frozen=True)
class YearInfo:

    year: int
    location: Path
    days: list[DayInfo]


@dataclasses.dataclass(frozen=True)
class AocSuite:

    years: list[YearInfo]


def discover() -> AocSuite:
    aoc_dir = Path(os.path.dirname(__file__))
    year_dirs = [s for s in aoc_dir.iterdir() if s.is_dir() and s.name.startswith('year')]
    years = []
    for year_dir in year_dirs:
        year = int(year_dir.name[4:])
        day_files = [s for s in year_dir.iterdir() if s.is_file() and s.name.startswith('day_')]
        days = []
        for day_file in day_files:
            day, day_name = re.match(r'day_(\d+)_(.*)', day_file.stem).groups()
            day, day_name = int(day), day_name.replace('_', ' ')
            day_module = sys.modules[f'aoc.year{year}.{day_file.stem}']
            days.append(DayInfo(year, day, day_name, day_file, day_module.star1, day_module.star2))
        days.sort(key=lambda x: x.day)
        years.append(YearInfo(year, year_dir, days))
    years.sort(key=lambda x: x.year)
    return AocSuite(years)


def ensure_inputs(suite: AocSuite, cookie: str):
    cookies = {'session': cookie}
    for year in suite.years:
        for day in year.days:
            if day.input.exists():
                continue
            content = (requests
                       .get(f'https://adventofcode.com/{year.year}/day/{day.day}/input', cookies=cookies)
                       .content
                       .decode('ascii'))
            with day.input.open('w', encoding='ascii') as f:
                f.write(content)


parser = argparse.ArgumentParser(
                    prog='aoc',
                    description='Advent of Code launcher')
parser.add_argument('--cookie')
parser.add_argument('-y', '--year', type=int)
parser.add_argument('-d', '--day', type=int)

args = parser.parse_args()

cookie_path = os.path.abspath(args.cookie or 'session.cookie')
with open(cookie_path, 'r') as f:
    cookie = f.read()

suite = discover()
ensure_inputs(suite, cookie)
for year in suite.years:
    if args.year and args.year != year.year:
        continue
    for day in year.days:
        if args.day and args.day != day.day:
            continue
        print(f'{year.year}.{day.day} {day.name}:')
        print(f'    star 1: {day.star1()}')
        print(f'    star 2: {day.star2()}')
