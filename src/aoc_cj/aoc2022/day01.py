import heapq
from collections.abc import Iterable


def elf_calories(txt: str) -> Iterable[int]:
    return (sum(map(int, c.split())) for c in txt.split("\n\n"))


def parta(txt: str) -> int:
    return max(elf_calories(txt))


def partb(txt: str) -> int:
    return sum(heapq.nlargest(3, elf_calories(txt)))


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
