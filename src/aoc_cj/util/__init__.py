"""cj's utilities https://adventofcode.com/"""

import math
import re
from collections.abc import Generator

from ._point import Point3D
from ._priority_queue import PriorityQueue

__all__ = (
    "clamp",
    "floats",
    "ints",
    "is_prime",
    "Point3D",
    "PriorityQueue",
)


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


_INTS_PATTERN = re.compile(r"-?\d+")


def ints(s: str) -> Generator[int, None, None]:
    yield from map(int, _INTS_PATTERN.findall(s))


_FLOATS_PATTERN = re.compile(r"-?\d+\.\d+")


def floats(s: str) -> Generator[float, None, None]:
    yield from map(float, _FLOATS_PATTERN.findall(s))
