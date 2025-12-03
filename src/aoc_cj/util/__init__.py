"""cj's utilities https://adventofcode.com/"""

import math
import re
from collections.abc import Callable, Generator

from ._point import Point3D
from ._priority_queue import PriorityQueue

__all__ = (
    "Point3D",
    "PriorityQueue",
    "adj_4",
    "adj_8",
    "clamp",
    "create_regex_parser",
    "digits",
    "floats",
    "ints",
    "is_prime",
)


def adj_4(p: complex) -> Generator[complex]:
    for delta in (-1, 1, -1j, 1j):
        yield p + delta


def adj_8(p: complex) -> Generator[complex]:
    for delta in (-1 - 1j, -1j, 1 - 1j, -1, 1, -1 + 1j, 1j, 1 + 1j):
        yield p + delta


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


def create_regex_parser[T](p: str | re.Pattern[str], f: Callable[[str], T]) -> Callable[[str], Generator[T]]:
    def regex_parse_fn(s: str) -> Generator[T]:
        yield from map(f, re.findall(p, s))

    return regex_parse_fn


ints = create_regex_parser(r"-?\d+", int)
digits = create_regex_parser(r"\d", int)
floats = create_regex_parser(r"-?\d+\.\d+", float)
