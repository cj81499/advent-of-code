from collections.abc import Iterable

from more_itertools import pairwise, triplewise


def nums(txt: str) -> Iterable[int]:
    return map(int, txt.splitlines())


def parta(txt: str) -> int:
    return sum(b > a for a, b in pairwise(nums(txt)))


def partb(txt: str) -> int:
    sums = (sum(w) for w in triplewise(nums(txt)))
    return sum(b > a for a, b in pairwise(sums))


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
