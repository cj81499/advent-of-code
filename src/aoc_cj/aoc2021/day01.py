import itertools
from collections.abc import Iterable

import more_itertools as mi


def nums(txt: str) -> Iterable[int]:
    return map(int, txt.splitlines())


def part_1(txt: str) -> int:
    return sum(b > a for a, b in itertools.pairwise(nums(txt)))


def part_2(txt: str) -> int:
    sums = (sum(w) for w in mi.triplewise(nums(txt)))
    return sum(b > a for a, b in itertools.pairwise(sums))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
