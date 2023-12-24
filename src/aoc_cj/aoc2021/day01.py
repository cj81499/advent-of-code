from collections.abc import Iterable

from more_itertools import pairwise, triplewise


def nums(txt: str) -> Iterable[int]:
    return map(int, txt.splitlines())


def part_1(txt: str) -> int:
    return sum(b > a for a, b in pairwise(nums(txt)))


def part_2(txt: str) -> int:
    sums = (sum(w) for w in triplewise(nums(txt)))
    return sum(b > a for a, b in pairwise(sums))


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
