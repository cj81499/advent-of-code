from collections.abc import Iterable
from itertools import pairwise


def is_safe(nums: Iterable[int]) -> bool:
    differences = [b - a for a, b in pairwise(nums)]
    return all(d in (1, 2, 3) for d in differences) or all(d in (-1, -2, -3) for d in differences)


def part_1(txt: str) -> int:
    return sum(is_safe(map(int, line.split())) for line in txt.splitlines())


def part_2(txt: str) -> int:
    return sum(
        is_safe(nums := list(map(int, line.split())))
        or any(is_safe(nums[:i] + nums[i + 1 :]) for i in range(len(nums)))
        for line in txt.splitlines()
    )


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
