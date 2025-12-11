import itertools
from collections.abc import Generator, Iterable

import more_itertools as mi


def part_1(txt: str) -> int:
    return sum(is_valid_triangle(nums(line)) for line in txt.splitlines())


def part_2(txt: str) -> int:
    lines = txt.splitlines()
    assert len(lines) % 3 == 0
    return sum(
        sum(is_valid_triangle(n) for n in zip(la, lb, lc, strict=True))
        for la, lb, lc in (map(nums, c) for c in mi.ichunked(lines, 3))
    )


def nums(s: str) -> Generator[int]:
    return (int(n) for n in s.split())


def is_valid_triangle(candidate: Iterable[int]) -> bool:
    return all(a + b > c for a, b, c in itertools.permutations(candidate))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
