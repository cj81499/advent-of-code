import itertools
from collections.abc import Iterable

from more_itertools import ichunked


def parta(txt: str):
    return sum(is_valid_triangle(nums(line)) for line in txt.splitlines())


def partb(txt: str):
    lines = txt.splitlines()
    assert len(lines) % 3 == 0
    return sum(
        sum(is_valid_triangle(n) for n in zip(la, lb, lc)) for la, lb, lc in (map(nums, c) for c in ichunked(lines, 3))
    )


def nums(s: str):
    return (int(n) for n in s.split())


def is_valid_triangle(candidate: Iterable[int]):
    return all(a + b > c for a, b, c in itertools.permutations(candidate))


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
