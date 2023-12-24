import itertools
from collections.abc import Iterable

from more_itertools import ichunked


def part_1(txt: str):
    return sum(is_valid_triangle(nums(line)) for line in txt.splitlines())


def part_2(txt: str):
    lines = txt.splitlines()
    assert len(lines) % 3 == 0
    return sum(
        sum(is_valid_triangle(n) for n in zip(la, lb, lc)) for la, lb, lc in (map(nums, c) for c in ichunked(lines, 3))
    )


def nums(s: str):
    return (int(n) for n in s.split())


def is_valid_triangle(candidate: Iterable[int]):
    return all(a + b > c for a, b, c in itertools.permutations(candidate))


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
