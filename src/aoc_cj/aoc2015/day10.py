import itertools
from collections.abc import Iterable

import more_itertools as mi


def look_and_say(txt: str, *, rounds: int) -> str:
    it: Iterable[int] = (int(c) for c in txt)
    for _ in range(rounds):
        it = itertools.chain.from_iterable((count, char) for char, count in mi.run_length.encode(it))
    return "".join(str(n) for n in it)


def part_1(txt: str) -> int:
    return len(look_and_say(txt, rounds=40))


def part_2(txt: str) -> int:
    return len(look_and_say(txt, rounds=50))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
