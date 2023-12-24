import operator
from functools import reduce

import more_itertools as mi


def get_common_item(*strings: str) -> str:
    return mi.one(reduce(operator.and_, (set(s) for s in strings)))


def priority(c: str) -> int:
    assert len(c) == 1
    return ord(c.lower()) - ord("a") + (1 if c.islower() else 27)


def part_1(txt: str) -> int:
    return sum(priority(get_common_item(l[: len(l) // 2], l[len(l) // 2 :])) for l in txt.splitlines())


def part_2(txt: str) -> int:
    return sum(priority(get_common_item(*chunk)) for chunk in mi.chunked(txt.splitlines(), 3))


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
