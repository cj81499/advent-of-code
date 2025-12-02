import itertools
from collections.abc import Callable, Iterable

import more_itertools as mi


class fn[T, R]:
    def __init__(self, f: Callable[[T], R]) -> None:
        self.f = f

    def __ror__(self, other: T) -> R:
        return self.f(other)


class map_[T, R]:
    def __init__(self, f: Callable[[T], R]) -> None:
        self.f = f

    def __ror__(self, other: Iterable[T]) -> Iterable[R]:
        return map(self.f, other)


class _flatten:
    def __ror__[T](self, other: Iterable[Iterable[T]]) -> Iterable[T]:
        return mi.flatten(other)


flatten = _flatten()


class select[T]:
    def __init__(self, f: Callable[[T], bool]) -> None:
        self.f = f

    def __ror__(self, other: Iterable[T]) -> Iterable[T]:
        return filter(self.f, other)


def double(n: int) -> int:
    return n * 2


def two_ele[T](v: T) -> tuple[T, T]:
    return (v, v)


if __name__ == "__main__":
    x1 = 1 | fn(double)
    print(x1)

    l = itertools.count()
    x2 = l | map_(double)
    print(x2, mi.take(10, x2))

    l = itertools.count()
    x3 = l | map_[int, tuple[int, int]](two_ele) | flatten
    print(x3, mi.take(10, x3))

    l = itertools.count()
    x4 = l | map_(str)
    print(x4, mi.take(10, x4))

    l = itertools.count()
    x5 = l | select[int](lambda n: n % 2 == 0)
    print(x5, mi.take(10, x5))
