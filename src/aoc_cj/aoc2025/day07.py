import enum
import functools
from typing import assert_never

import more_itertools as mi


class GridEntry(enum.StrEnum):
    START = "S"
    SPLITTER = "^"
    EMPTY = "."


def part_1(txt: str) -> int:
    rows = tuple(tuple(map(GridEntry, line)) for line in txt.splitlines())
    start = mi.one(x for x, ge in enumerate(rows[0]) if ge == GridEntry.START)
    beams = {start}
    split_count = 0
    for row in rows:
        moving_to_empty, moving_to_splitter = mi.partition(lambda b: row[b] == GridEntry.SPLITTER, beams)
        moving_to_splitter = mi.countable(moving_to_splitter)
        beams = {*moving_to_empty, *mi.flatten((b - 1, b + 1) for b in moving_to_splitter)}
        split_count += moving_to_splitter.items_seen
    return split_count


def part_2(txt: str) -> int:
    g = {complex(x, y): GridEntry(c) for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line)}
    start = mi.one(p for p, ge in g.items() if ge == GridEntry.START)
    max_y = int(max(p.imag for p in g))

    @functools.cache
    def _helper(p: complex) -> int:
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
