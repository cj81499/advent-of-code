import itertools
from typing import Iterable, TypeVar

T = TypeVar("T")


def sliding_window(iterable: Iterable[T], n: int) -> Iterable[tuple[T, ...]]:
    """https://napsterinblue.github.io/notes/python/internals/itertools_sliding_window/"""
    iterables = itertools.tee(iterable, n)

    for iterable, num_skipped in zip(iterables, itertools.count()):
        for _ in range(num_skipped):
            next(iterable, None)

    return zip(*iterables)


def nums(txt: str) -> list[int]:
    return list(map(int, txt.splitlines()))


def parta(txt: str) -> int:
    return sum(b > a for a, b in sliding_window(nums(txt), 2))


def partb(txt: str) -> int:
    windows = sliding_window(nums(txt), 3)
    sums = map(sum, windows)
    return sum(b > a for a, b in sliding_window(sums, 2))


def main(txt: str) -> None:
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
