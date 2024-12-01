import itertools
from typing import Iterable

from more_itertools import run_length


def look_and_say(txt: str, *, rounds: int) -> str:
    it: Iterable[int] = (int(c) for c in txt)
    for _ in range(rounds):
        it = itertools.chain.from_iterable((count, char) for char, count in run_length.encode(it))
    return "".join(str(n) for n in it)


def part_1(txt: str) -> int:
    return len(look_and_say(txt, rounds=40))


def part_2(txt: str) -> int:
    return len(look_and_say(txt, rounds=50))


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
