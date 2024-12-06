import more_itertools as mi


class LoopDetectedError(Exception):
    pass


def explore(mapping: dict[complex, str], initial_guard_pos: complex) -> set[complex]:
    guard_pos = initial_guard_pos
    guard_heading = -1j
    # seen is a set of (guard_pos, guard_heading) tuples
    # if we get a duplicate, we've found a loop
    seen = set[tuple[complex, complex]]()
    while guard_pos in mapping:
        state = guard_pos, guard_heading
        if state in seen:
            raise LoopDetectedError
        seen.add(state)

        new_guard_pos = guard_pos + guard_heading
        val_in_mapping = mapping.get(new_guard_pos)
        if val_in_mapping is None:  # if we're outside the mapping
            break
        if val_in_mapping == "#":
            # turn right 90 deg
            guard_heading = complex(-guard_heading.imag, guard_heading.real)
            new_guard_pos = guard_pos
        guard_pos = new_guard_pos
    return {p for p, _heading in seen}


def part_1(txt: str) -> int:
    mapping = {x + y * 1j: c for y, row in enumerate(txt.splitlines()) for x, c in enumerate(row)}
    guard_pos = mi.one(p for p, c in mapping.items() if c == "^")
    return len(explore(mapping, guard_pos))


def part_2(txt: str) -> int:
    mapping = {x + y * 1j: c for y, row in enumerate(txt.splitlines()) for x, c in enumerate(row)}
    guard_pos = mi.one(p for p, c in mapping.items() if c == "^")

    # optimization: instead of considering all (x, y) in mapping, consider only
    # (x, y) on the guard's "normal" path.
    positions_on_guard_path = explore(mapping, guard_pos)

    causes_loop = set[complex]()
    for obstruction_pos in positions_on_guard_path:
        obstructed_mapping = {**mapping, obstruction_pos: "#"}
        try:
            explore(obstructed_mapping, guard_pos)
        except LoopDetectedError:
            causes_loop.add(obstruction_pos)
    return len(causes_loop)


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
