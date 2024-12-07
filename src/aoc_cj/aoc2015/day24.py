import itertools
from collections.abc import Generator
from math import prod


def groups(weights: set[int], weight_per_group: int) -> Generator[tuple[int, ...], None, None]:
    for size in range(1, len(weights)):
        yield from groups_of_size(weights, weight_per_group, size)


def groups_of_size(weights: set[int], weight_per_group: int, size: int) -> Generator[tuple[int, ...], None, None]:
    for group in itertools.combinations(weights, r=size):
        if sum(group) == weight_per_group:
            yield group


def helper(txt: str, number_of_groups: int = 3) -> int:
    weights = [int(n) for n in txt.splitlines()]
    assert len(weights) == len(set(weights))
    weights = set(weights)
    weight_per_group = sum(weights) // number_of_groups
    min_group_size = len(next(groups(weights, weight_per_group)))
    return min(map(prod, groups_of_size(weights, weight_per_group, min_group_size)))


def part_1(txt: str) -> int:
    return helper(txt)


def part_2(txt: str) -> int:
    return helper(txt, 4)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
