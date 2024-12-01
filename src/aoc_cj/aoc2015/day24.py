import itertools
from math import prod


def groups(weights: set[int], weight_per_group: int):
    for size in range(1, len(weights)):
        yield from groups_of_size(weights, weight_per_group, size)


def groups_of_size(weights, weight_per_group, size):
    for group in itertools.combinations(weights, r=size):
        if sum(group) == weight_per_group:
            yield group


def helper(txt, number_of_groups=3):
    weights = [int(n) for n in txt.splitlines()]
    assert len(weights) == len(set(weights))
    weights = set(weights)
    weight_per_group = sum(weights) // number_of_groups
    min_group_size = len(next(groups(weights, weight_per_group)))
    return min(map(prod, groups_of_size(weights, weight_per_group, min_group_size)))


def part_1(txt):
    return helper(txt)


def part_2(txt):
    return helper(txt, 4)


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
