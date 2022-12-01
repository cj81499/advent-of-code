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


def parta(txt):
    return helper(txt)


def partb(txt):
    return helper(txt, 4)


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
