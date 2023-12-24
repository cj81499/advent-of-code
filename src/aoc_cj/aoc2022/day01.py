import heapq
from collections.abc import Iterable

from aoc_cj import util


def elf_calories(txt: str) -> Iterable[int]:
    return (sum(util.ints(c)) for c in txt.split("\n\n"))


def part_1(txt: str) -> int:
    return max(elf_calories(txt))


def part_2(txt: str) -> int:
    return sum(heapq.nlargest(3, elf_calories(txt)))


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
