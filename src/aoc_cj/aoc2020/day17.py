import functools
import itertools
from collections.abc import Generator, Iterable, Sequence
from collections.abc import Set as AbstractSet

import more_itertools as mi


def replace_at_pos[T](t: Sequence[T], index: int, value: T) -> tuple[T, ...]:
    """Return a tuple with the element at `index` replaced by `value`."""
    return (*t[:index], value, *t[index + 1 :])


type Point = tuple[int, ...]


def neighbors(p: Point) -> Generator[Point]:
    for deltas in itertools.product(*itertools.repeat((-1, 0, 1), len(p))):
        if any(x != 0 for x in deltas):
            yield tuple(x + d for x, d in zip(p, deltas, strict=True))


def points_to_consider(active: AbstractSet[Point]) -> Iterable[Point]:
    min_corner, max_corner = zip(*(map(mi.minmax, zip(*active, strict=True))), strict=True)
    return itertools.product(
        *(range(min_for_d - 1, max_for_d + 2) for min_for_d, max_for_d in zip(min_corner, max_corner, strict=True)),
    )


def solve(txt: str, *, cycles: int = 6, dimensions: int = 3) -> int:
    active = {
        (x, y, *itertools.repeat(0, dimensions - 2))
        for y, line in enumerate(txt.splitlines())
        for x, c in enumerate(line)
        if c == "#"
    }

    for _cycle in range(cycles):
        active = {p for p in points_to_consider(active) if should_activate(p, active)}

    return len(active)


def should_activate(p: Point, active: set[Point]) -> bool:
    is_active = p in active
    active_neighbors = {n for n in neighbors(p) if n in active}
    if is_active:
        if len(active_neighbors) in (2, 3):
            return True
    elif len(active_neighbors) == 3:
        return True
    return False


part_1 = solve
part_2 = functools.partial(solve, dimensions=4)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
