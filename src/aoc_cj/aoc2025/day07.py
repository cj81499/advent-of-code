import enum
import functools
from typing import assert_never

import more_itertools as mi


class GridEntry(enum.StrEnum):
    START = "S"
    SPLITTER = "^"
    EMPTY = "."


def part_1(txt: str) -> int:
    g = {complex(x, y): GridEntry(c) for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line) if c != "."}
    start = mi.one(p for p, ge in g.items() if ge == GridEntry.START)
    beams = {start}
    split_count = 0
    for _ in range(10_000):  # HACK: 10,000 if probably enough...
        new_beams = set[complex]()
        for b in beams:
            below = b + 1j
            if g.get(below) == GridEntry.SPLITTER:
                split_count += 1
                new_beams.add(below - 1)
                new_beams.add(below + 1)
            else:
                new_beams.add(below)
        beams = new_beams
    return split_count


def part_2(txt: str) -> int:
    g = {complex(x, y): GridEntry(c) for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line)}
    start = mi.one(p for p, ge in g.items() if ge == GridEntry.START)
    max_y = int(max(p.imag for p in g))

    @functools.cache
    def _helper(p: complex) -> int:
        print(p)
        if p.imag > max_y:
            return 1
        ge = g.get(p)
        if ge is GridEntry.SPLITTER:
            return _helper(p + 1j - 1) + _helper(p + 1j + 1)
        if ge is GridEntry.EMPTY or ge is GridEntry.START or ge is None:
            return _helper(p + 1j)
        assert_never(ge)

    return _helper(start)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
