from typing import Iterable


def product(numbers: Iterable[int]) -> int:
    result = 1
    for n in numbers:
        result *= n
    return result