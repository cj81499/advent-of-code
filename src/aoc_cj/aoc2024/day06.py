import more_itertools as mi


def part_1(txt: str) -> int:
    mapping = {x + y * 1j: c for y, row in enumerate(txt.splitlines()) for x, c in enumerate(row)}
    guard_pos = mi.one(p for p, c in mapping.items() if c == "^")
    guard_heading = -1j
    seen = set[complex]()
    while guard_pos in mapping:
        seen.add(guard_pos)
        new_guard_pos = guard_pos + guard_heading

        val_in_mapping = mapping.get(new_guard_pos)
        if val_in_mapping is None:  # if we're outside the mapping
            return len(seen)
        if val_in_mapping == "#":
            # turn right 90 deg
            guard_heading = complex(-guard_heading.imag, guard_heading.real)
            new_guard_pos = guard_pos
        guard_pos = new_guard_pos
    return len(seen)


def part_2(txt: str) -> int:
    lines = txt.splitlines()
    height = len(lines)
    width = len(lines[0])
    original_mapping = {x + y * 1j: c for y, row in enumerate(lines) for x, c in enumerate(row)}
    original_guard_pos = mi.one(p for p, c in original_mapping.items() if c == "^")
    original_guard_heading = -1j

    # works, but slow. optimization idea: instead of considering all (x, y), consider only (x, y) on the guard's initial path.

    causes_loop = set[complex]()
    for x in range(width):
        for y in range(height):
            mapping = dict(original_mapping)
            guard_pos = original_guard_pos
            guard_heading = original_guard_heading
            obstruction_pos = x + y * 1j
            if mapping[obstruction_pos] not in ("#", "^"):
                mapping[obstruction_pos] = "#"
                # seen is a set of (guard_pos, guard_heading) tuples
                # if we get a duplicate, we've found a loop
                seen = set[tuple[complex, complex]]()
                while guard_pos in mapping:
                    state = (guard_pos, guard_heading)
                    if state in seen:
                        # adding an obstruction at (x, y) will cause a loop
                        causes_loop.add(obstruction_pos)
                        break
                    seen.add(state)
                    new_guard_pos = guard_pos + guard_heading
                    val_in_mapping = mapping.get(new_guard_pos)
                    if val_in_mapping == "#":
                        # turn right 90 deg
                        guard_heading = complex(-guard_heading.imag, guard_heading.real)
                        new_guard_pos = guard_pos
                    guard_pos = new_guard_pos

    return len(causes_loop)


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
