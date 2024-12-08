import itertools
import re

import more_itertools as mi

DIGITS_REGEX = re.compile(r"(\d+)")


def nums(txt: str) -> tuple[int, ...]:
    return tuple(int(x) for x in DIGITS_REGEX.findall(txt))


def position(disc: tuple[int, ...], t: int) -> int:
    _, num_positions, _, start_pos = disc
    return (start_pos + t) % num_positions


def simulate(txt: str, *, additional_disc: bool = False) -> int:
    discs = [nums(line) for line in txt.splitlines()]
    if additional_disc:
        discs.append((len(discs) + 1, 11, 0, 0))

    return mi.first(t for t in itertools.count() if all(position(d, t + d[0]) == 0 for d in discs))


def part_1(txt: str) -> int:
    return simulate(txt)


def part_2(txt: str) -> int:
    return simulate(txt, additional_disc=True)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
