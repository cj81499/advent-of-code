import collections
import itertools
from collections.abc import Collection, Generator, Iterable
from typing import Final, Literal

ACTIVE: Final = "#"
INACTIVE: Final = "."

type Point = tuple[int, ...]


def neighbors(pos: Point) -> Generator[Point]:
    for delta in itertools.product(*itertools.repeat((-1, 0, 1), len(pos))):
        if not all(x == 0 for x in delta):
            yield tuple(x + dx for x, dx in zip(pos, delta))


def simulate(txt: str, dimensions: int) -> int:
    # initialize space
    space = collections.defaultdict[Point, Literal[".", "#"]](lambda: INACTIVE)
    space.update(
        {
            (x, y, *itertools.repeat(0, dimensions - 2)): c
            for y, row in enumerate(txt.splitlines())
            for x, c in enumerate(row)
        }
    )

    # run 6 iterations of the simulation
    for _ in range(6):
        # get min and max coordinates
        mins, maxes = minmax_tuple(set(space))
        # count active neighbors for each position
        active_neighbors = collections.defaultdict[Point, int](int)
        for p in expand_points(mins, maxes):
            if space[p] == ACTIVE:
                for n in neighbors(p):
                    active_neighbors[n] += 1

        # calculate the contents of the new space
        new_space = collections.defaultdict[Point, Literal[".", "#"]](lambda: INACTIVE)
        new_space.update(
            {
                p: ACTIVE
                for p in expand_points(mins, maxes)
                if active_neighbors[p] == 3 or (active_neighbors[p] == 2 and space[p] == ACTIVE)
            }
        )
        space = new_space

    return sum(v == ACTIVE for v in space.values())


def minmax_tuple(points: Collection[Point]) -> tuple[Point, Point]:
    return tuple(min(x) for x in zip(*points)), tuple(max(x) for x in zip(*points))


def expand_points(mins: Point, maxes: Point) -> Iterable[tuple[int, ...]]:
    assert len(mins) == len(maxes)
    return itertools.product(*(range(start - 1, stop + 2) for start, stop in zip(mins, maxes)))


def part_1(txt: str) -> int:
    return simulate(txt, 3)


def part_2(txt: str) -> int:
    return simulate(txt, 4)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
