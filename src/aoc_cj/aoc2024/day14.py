import dataclasses
import enum
import itertools
import math
from collections import Counter
from typing import Self

from aoc_cj import util


class Quadrant(enum.Enum):
    TOP_LEFT = enum.auto()
    TOP_RIGHT = enum.auto()
    BOTTOM_LEFT = enum.auto()
    BOTTOM_RIGHT = enum.auto()


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class Robot:
    p: complex
    v: complex

    @classmethod
    def parse(cls, txt: str) -> Self:
        px, py, vx, vy = util.ints(txt)
        return cls(p=complex(px, py), v=complex(vx, vy))

    def after(self, t: int, *, width: int, height: int) -> complex:
        return complex(
            (self.p.real + t * self.v.real) % width,
            (self.p.imag + t * self.v.imag) % height,
        )


def quadrant(p: complex, *, width: int, height: int) -> Quadrant | None:
    on_top = p.imag < (height - 1) / 2
    on_bottom = p.imag > (height - 1) / 2
    on_left = p.real < (width - 1) / 2
    on_right = p.real > (width - 1) / 2
    if on_top and on_left:
        return Quadrant.TOP_LEFT
    if on_top and on_right:
        return Quadrant.TOP_RIGHT
    if on_bottom and on_left:
        return Quadrant.BOTTOM_LEFT
    if on_bottom and on_right:
        return Quadrant.BOTTOM_RIGHT
    return None


def part_1(txt: str, *, width: int = 101, height: int = 103) -> int:
    robots = map(Robot.parse, txt.splitlines())
    positions_after_100 = (r.after(100, width=width, height=height) for r in robots)
    quadrants = (quadrant(p, width=width, height=height) for p in positions_after_100)
    return math.prod(Counter(q for q in quadrants if q is not None).values())


def part_2(txt: str, *, width: int = 101, height: int = 103) -> int:  # pragma: no cover - no test case provided
    robots = list(map(Robot.parse, txt.splitlines()))
    for t in itertools.count():
        # find "groupings" (like the regions from day 12) of occupied positions.
        # if the largest is "big enough" to be ascii art of a christmas tree, return t.
        # TODO: consider moving this "grouping"/region-finding logic to `aoc_cj.utils`.
        robot_positions = {r.after(t, width=width, height=height) for r in robots}
        max_group_size = 0
        while robot_positions:
            region = set[complex]()
            to_add = [robot_positions.pop()]
            while to_add:
                adding = to_add.pop()
                region.add(adding)
                for adj_p in util.adj_4(adding):
                    if adj_p in robot_positions:
                        to_add.append(adj_p)
                        robot_positions.remove(adj_p)
            max_group_size = max(max_group_size, len(region))
        if max_group_size > 50:
            return t

    assert False, "unreachable"


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
