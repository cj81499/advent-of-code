from collections import defaultdict
from collections.abc import Mapping, Sequence
from typing import TypeVar

import more_itertools as mi


def is_correctly_ordered(rules: Mapping[int, set[int]], nums: Sequence[int]) -> bool:
    for i, n in enumerate(nums):
        after = nums[i + 1 :]
        must_come_before = rules[n]
        for n2 in after:
            if n2 in must_come_before:
                return False
    return True


def fix_ordering(rules: Mapping[int, set[int]], nums: Sequence[int]) -> tuple[int, ...]:
    order = []
    to_order = set(nums)
    while to_order:
        # the next number is not "blocked" by any number in its rules that hasn't already been added to the order
        chosen = mi.one(n for n in to_order if all(n2 in order for n2 in rules[n].intersection(nums)))
        order.append(chosen)
        to_order.remove(chosen)
    return tuple(order)


_T = TypeVar("_T")


def middle_element(seq: Sequence[_T]) -> _T:
    return seq[len(seq) // 2]


def part_1(txt: str) -> int:
    page_ordering_rules_s, pages_to_produce = txt.split("\n\n")
    rules = defaultdict[int, set[int]](set)
    for line in page_ordering_rules_s.splitlines():
        l, r = map(int, line.split("|"))
        rules[r].add(l)

    s = 0

    for line in pages_to_produce.splitlines():
        nums = tuple(map(int, line.split(",")))

        if is_correctly_ordered(rules, nums):
            s += middle_element(nums)

    return s


def part_2(txt: str) -> int:
    page_ordering_rules_s, pages_to_produce = txt.split("\n\n")
    rules = defaultdict[int, set[int]](set)
    for line in page_ordering_rules_s.splitlines():
        l, r = map(int, line.split("|"))
        rules[r].add(l)

    s = 0

    for line in pages_to_produce.splitlines():
        nums = tuple(map(int, line.split(",")))

        if not is_correctly_ordered(rules, nums):
            correctly_ordered_nums = fix_ordering(rules, nums)
            s += middle_element(correctly_ordered_nums)

    return s


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
