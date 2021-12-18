"""cj's utilities https://adventofcode.com/"""


import itertools
from functools import reduce
from operator import mul
from typing import Any, Callable, Iterable, Protocol, TypeVar


class SupportsLessThan(Protocol):
    def __lt__(self, __other: Any) -> bool:
        ...


T = TypeVar("T")
S = TypeVar("S")
SupportsLessThanK = TypeVar("SupportsLessThanK", bound=SupportsLessThan)


def clamp(n: int, min_n: int, max_n: int) -> int:
    assert min_n <= max_n
    return max(min_n, min(n, max_n))


def group_by(iterable: Iterable[T], key: Callable[[T], SupportsLessThanK]) -> dict[SupportsLessThanK, list[T]]:
    groups = itertools.groupby(sorted(iterable, key=key), key=key)
    return {k: list(values) for k, values in groups}


def prod(iterable: Iterable[int], start: int = 1) -> int:
    return reduce(mul, iterable, start)
