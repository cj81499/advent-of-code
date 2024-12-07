import itertools
from dataclasses import dataclass
from typing import Self

import z3  # type: ignore[import-untyped]

from aoc_cj import util


@dataclass
class Hailstone:
    px: int
    py: int
    pz: int
    vx: int
    vy: int
    vz: int

    @classmethod
    def parse(cls, s: str) -> Self:
        return cls(*util.ints(s))

    def intersect_xy(self, other: Self) -> complex | None:
        px1 = self.px
        py1 = self.py
        vx1 = self.vx
        vy1 = self.vy

        px2 = other.px
        py2 = other.py
        vx2 = other.vx
        vy2 = other.vy

        try:
            # We have x and y as functions of time (t)
            # x = vx * t + px                                                       # noqa: ERA001
            # y = vy * t + py                                                       # noqa: ERA001
            #
            # Solve each equation for t
            # t = (x - px) / vx                                                     # noqa: ERA001
            # t = (y - py) / vy                                                     # noqa: ERA001
            #
            # We have two equations for t. Set them equal to each other and solve for y
            # (x - px) / vx = (y - py) / vy
            # y = vy * ((x / vx) - (px / vx)) + py                                  # noqa: ERA001
            #
            # Convert to y = mx + b form
            # y = (vy / vx) * x + py - ((vy * px) / vx)                             # noqa: ERA001
            # m = (vy / vx)                                                         # noqa: ERA001
            # b = py - ((vy * px) / vx)                                             # noqa: ERA001
            #
            # We have two equations for y (one for each hailstone)
            # y = m1 * x + b1                                                       # noqa: ERA001
            # y = m2 * x + b2                                                       # noqa: ERA001
            # m1 * x + b1 = m2 * x + b2
            # x = (b2 - b1) / (m1 - m2)                                             # noqa: ERA001

            # solve for x by substituting m1, m2, b1, and b2
            x = ((py2 - ((vy2 * px2) / vx2)) - (py1 - ((vy1 * px1) / vx1))) / ((vy1 / vx1) - (vy2 / vx2))

            # solve for y using equation from earlier
            y = vy1 * ((x / vx1) - (px1 / vx1)) + py1
        except ZeroDivisionError:  # divide by zero implies no intersection
            return None

        # if the intersection is in the past
        if (
            (self.vx > 0 and x < self.px)  # moving right, but x is left of starting position
            or (self.vx < 0 and x > self.px)  # moving left, but x is right of starting position
            or (other.vx > 0 and x < other.px)  # moving right, but x is left of starting position
            or (other.vx < 0 and x > other.px)  # moving left, but x is right of starting position
        ):
            return None

        return complex(x, y)


def part_1(txt: str, *, range_endpoints: tuple[int, int] = (200000000000000, 400000000000000)) -> int:
    hailstones = [Hailstone.parse(l) for l in txt.splitlines()]

    return sum(
        1
        for h1, h2 in itertools.combinations(hailstones, 2)
        if (
            ((intersect := h1.intersect_xy(h2)) is not None)
            and range_endpoints[0] <= intersect.real <= range_endpoints[1]
            and range_endpoints[0] <= intersect.imag <= range_endpoints[1]
        )
    )


def part_2(txt: str) -> int:
    hailstones = [Hailstone.parse(l) for l in txt.splitlines()]

    # rock position and velocity
    px, py, pz, vx, vy, vz = z3.Reals(("px", "py", "pz", "vx", "vy", "vz"))

    s = z3.Solver()
    for h in hailstones:
        t = z3.Real(f"t - {h}")
        # add constraint that rock will collide w/ hailstone @ t
        s.add(
            px + vx * t == h.px + h.vx * t,
            py + vy * t == h.py + h.vy * t,
            pz + vz * t == h.pz + h.vz * t,
        )

    assert s.check() == z3.sat
    model = s.model()
    result = z3.simplify(model[px] + model[py] + model[pz])
    assert isinstance(result, z3.RatNumRef)
    result_int = result.as_long()
    assert isinstance(result_int, int)
    return result_int


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
