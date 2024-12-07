from collections import defaultdict
from collections.abc import Mapping, Sequence
from typing import TypeVar

import more_itertools as mi


def parse(txt: str) -> tuple[str, Mapping[int, set[int]]]:
    page_ordering_rules_s, pages_to_produce = txt.split("\n\n")
    rules = defaultdict[int, set[int]](set)
    for line in page_ordering_rules_s.splitlines():
        l, r = map(int, line.split("|"))
        rules[r].add(l)
    return pages_to_produce, rules


def is_correctly_ordered(rules: Mapping[int, set[int]], page_order: Sequence[int]) -> bool:
    for i, n in enumerate(page_order):
        after = page_order[i + 1 :]
        must_come_prior_to_n = rules[n]
        # if any number that must come prior to n appears after n, the pages are not in the correct order
        if any(n2 in must_come_prior_to_n for n2 in after):
            return False
    return True


_T = TypeVar("_T")


def middle_element(seq: Sequence[_T]) -> _T:
    return seq[len(seq) // 2]


def fix_ordering(rules: Mapping[int, set[int]], page_order: Sequence[int]) -> tuple[int, ...]:
    order: list[int] = []
    to_order = set(page_order)
    while to_order:
        # the next number in the order is not "blocked" by any number in its rules that hasn't already been added to the order
        chosen = mi.one(
            n
            for n in to_order
            if len(
                rules[n]
                # remove rules that deal with numbers that aren't in the sequence we're working with
                .intersection(page_order)
                # remove rules that are satisfied because they're already positioned prior to n
                .difference(order)
            )
            == 0
        )
        order.append(chosen)
        to_order.remove(chosen)
    return tuple(order)


def part_1(txt: str) -> int:
    pages_to_produce, rules = parse(txt)
    return sum(
        middle_element(page_order)
        for line in pages_to_produce.splitlines()
        if is_correctly_ordered(rules, page_order := tuple(map(int, line.split(","))))
    )


def part_2(txt: str) -> int:
    pages_to_produce, rules = parse(txt)
    return sum(
        middle_element(fix_ordering(rules, page_order))
        for line in pages_to_produce.splitlines()
        if not is_correctly_ordered(rules, page_order := tuple(map(int, line.split(","))))
    )


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
