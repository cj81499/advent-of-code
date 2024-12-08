import itertools
import re
from collections.abc import Iterable

import more_itertools as mi

PATTERN = re.compile(r"target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)")
INF = float("inf")
VELOCITY_RANGE = range(-500, 500)  # this should probably be enough...

Target = tuple[int, int, int, int]


def part_1(txt: str) -> int:
    return max(simulate_all(parse_target(txt)))


def part_2(txt: str) -> int:
    return mi.ilen(simulate_all(parse_target(txt)))


def simulate_all(target: Target) -> Iterable[int]:
    raw_results = (simulate(v, target) for v in itertools.product(VELOCITY_RANGE, VELOCITY_RANGE))
    yield from (int(r) for r in raw_results if r != -INF)


def parse_target(txt: str) -> Target:
    match = PATTERN.match(txt)
    assert match is not None, "bad input"
    min_x, max_x, min_y, max_y = map(int, match.groups())
    return min_x, max_x, min_y, max_y


def simulate(initial_velocity: tuple[int, int], target: Target) -> float:
    min_x, max_x, min_y, max_y = target
    pos = (0, 0)
    velocity = initial_velocity
    highest_y = 0
    while True:
        x, y = pos
        dx, dy = velocity

        # if we will never reach the target
        if (
            (y < min_y and dy < 0)  # we're below the target range and we're falling
            or (x > max_x and dx >= 0)  # to the right of the target range and not moving left
            or (x < min_x and dx < 0)  # to the left of the target range and not moving right
        ):
            return -INF

        highest_y = max(highest_y, pos[1])  # update highest_y

        # if we're in the target
        if min_x <= x <= max_x and min_y <= y <= max_y:
            return highest_y

        # update position
        pos = (x + dx, y + dy)

        # update velocity
        if dx > 0:
            dx -= 1
        elif dx < 0:
            dx += 1
        velocity = (dx, dy - 1)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
