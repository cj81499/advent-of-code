import itertools
from collections.abc import Mapping, Set

Rocks = Mapping[complex, str]

# FIXME: this could benefit from a refactor
#
# Imagine a RockPlatform class. It'd store:
# - the dimensions of the the rock platform
# - positions of O rocks and # rocks (separately?)
#
# It'd have methods:
# tilt(self, direction) -> RockPlatform
# total_load(self) -> int
#
# It'd also have a convenience staticmethod to parse a RockPlatform from a str.
#
# It would be hashable so we could quickly determine if we've seen it before.


def tilt(rocks: Rocks, direction: complex) -> Rocks:
    new_rocks = {p: r for p, r in rocks.items() if r == "#"}
    max_x = int(max(p.real for p in rocks))
    max_y = int(max(p.imag for p in rocks))
    y_range = range(max_y, -1, -1) if direction == 1j else range(max_y + 1)
    x_range = range(max_x, -1, -1) if direction == 1 else range(max_x + 1)
    for y in y_range:
        for x in x_range:
            p = complex(x, y)
            if rocks.get(p) == "O":
                new_pos = p
                while (
                    (potential_new_pos := new_pos + direction) not in new_rocks
                    and (0 <= potential_new_pos.real <= max_x)
                    and (0 <= potential_new_pos.imag <= max_y)
                ):
                    new_pos = potential_new_pos
                new_rocks[new_pos] = "O"

    return new_rocks


def total_load(rocks: Rocks) -> int:
    max_y = int(max(p.imag for p in rocks))
    max_x = int(max(p.real for p in rocks))
    max_load = max_y + 1
    tot = 0
    for y in range(max_y + 1):
        load_per_rock = max_load - y
        for x in range(max_x + 1):
            p = complex(x, y)
            if rocks.get(p) == "O":
                tot += load_per_rock
    return tot


def part_1(txt: str) -> int:
    rocks = {complex(x, y): c for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line) if c != "."}
    return total_load(tilt(rocks, -1j))


def total_load2(o_rocks: Set[complex], max_y: int) -> int:
    max_load = max_y + 1
    tot = 0
    for r in o_rocks:
        tot += max_load - int(r.imag)
    return tot


def part_2(txt: str) -> int:
    rocks: Rocks = {complex(x, y): c for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line) if c != "."}
    total_iterations = 1000000000
    tilt_cycle = itertools.islice(itertools.repeat((-1j, -1, 1j, 1)), total_iterations)
    o_rock_history: dict[frozenset[complex], int] = {}
    o_rock_history_by_cycle_number = [frozenset(p for p, r in rocks.items() if r == "O")]
    for cycle_number, cycle in enumerate(tilt_cycle, start=1):  # pragma: no branch # we expect to return while looping
        for direction in cycle:
            rocks = tilt(rocks, direction)
        o_rocks = frozenset(p for p, r in rocks.items() if r == "O")
        if o_rocks in o_rock_history:
            cycle_start = o_rock_history[o_rocks]
            cycle_length = cycle_number - cycle_start
            remaining_iterations = total_iterations - cycle_number
            cycle_index_after_all_iterations = remaining_iterations % cycle_length
            o_rocks_at_end = o_rock_history_by_cycle_number[cycle_start + cycle_index_after_all_iterations]
            return total_load2(o_rocks_at_end, int(max(p.imag for p in rocks)))
        o_rock_history[o_rocks] = cycle_number
        o_rock_history_by_cycle_number.append(o_rocks)
    return total_load(rocks)  # pragma: no cover # we expect to return while looping


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
