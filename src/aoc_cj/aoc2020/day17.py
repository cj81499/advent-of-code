import functools
import itertools

import more_itertools as mi

type Point = tuple[int, ...]


@functools.cache
def neighbors(p: Point) -> tuple[Point, ...]:
    return tuple(
        tuple(x + d for x, d in zip(p, deltas, strict=True))
        for deltas in itertools.product(*itertools.repeat((-1, 0, 1), len(p)))
        if any(x != 0 for x in deltas)
    )


def should_activate(p: Point, active: set[Point]) -> bool:
    active_neighbors = sum(1 for n in neighbors(p) if n in active)
    return active_neighbors == 3 or (active_neighbors == 2 and p in active)


def solve(txt: str, *, cycles: int = 6, dimensions: int = 3) -> int:
    active = {
        (x, y, *itertools.repeat(0, dimensions - 2))
        for y, line in enumerate(txt.splitlines())
        for x, c in enumerate(line)
        if c == "#"
    }

    for _cycle in range(cycles):
        points_to_consider = active.union(mi.flatten(map(neighbors, active)))
        active = {p for p in points_to_consider if should_activate(p, active)}

    return len(active)


part_1 = solve
part_2 = functools.partial(solve, dimensions=4)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
