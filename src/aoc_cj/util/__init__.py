"""cj's utilities https://adventofcode.com/"""

import math
import re
from collections.abc import Callable, Generator
from typing import TypeVar

from ._point import Point3D
from ._priority_queue import PriorityQueue

__all__ = (
    "Point3D",
    "PriorityQueue",
    "clamp",
    "create_regex_parser",
    "digits",
    "floats",
    "ints",
    "is_prime",
)

_T = TypeVar("_T")


def clamp(n: int, min_n: int, max_n: int) -> int:
    assert min_n <= max_n
    return max(min_n, min(n, max_n))


def is_prime(n: int) -> bool:
    """
    Check if n is prime

    A positive integer that is greater than 1 and is not divisible without
    a remainder by any positive integer other than itself and 1 is prime.
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # all primes > 3 are of the form 6n +/- 1
    for f in range(5, math.ceil(math.sqrt(n)) + 1, 6):
        if n % f == 0 or n % (f + 2) == 0:
            return False
    return True


def create_regex_parser(p: str | re.Pattern[str], f: Callable[[str], _T]) -> Callable[..., Generator[_T, None, None]]:
    def regex_parse_fn(s: str) -> Generator[_T, None, None]:
        yield from map(f, re.findall(p, s))

    return regex_parse_fn


ints = create_regex_parser(r"-?\d+", int)
digits = create_regex_parser(r"\d", int)
floats = create_regex_parser(r"-?\d+\.\d+", float)
