import dataclasses
import itertools
from dataclasses import dataclass
from typing import Optional

from typing_extensions import Self

from aoc_cj import util


def line_intersect(
    Ax1: float, Ay1: float, Ax2: float, Ay2: float, Bx1: float, By1: float, Bx2: float, By2: float
) -> Optional[tuple[float, float]]:
    """
    returns a (x, y) tuple or None if there is no intersection
    https://rosettacode.org/wiki/Find_the_intersection_of_two_lines#Python
    """
    d = (By2 - By1) * (Ax2 - Ax1) - (Bx2 - Bx1) * (Ay2 - Ay1)
    if d:
        uA = ((Bx2 - Bx1) * (Ay1 - By1) - (By2 - By1) * (Ax1 - Bx1)) / d
        uB = ((Ax2 - Ax1) * (Ay1 - By1) - (Ay2 - Ay1) * (Ax1 - Bx1)) / d
    else:
        return None
    if not (0 <= uA <= 1 and 0 <= uB <= 1):
        return None
    x = Ax1 + uA * (Ax2 - Ax1)
    y = Ay1 + uA * (Ay2 - Ay1)

    return x, y


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

    def at_t(self, t: int) -> Self:
        return dataclasses.replace(self, px=self.px + self.vx * t, py=self.py + self.vy * t, pz=self.pz + self.vz * t)


def parta(txt: str, *, range_endpoints: tuple[int, int] = (200000000000000, 400000000000000)) -> int:
    FAR_FUTURE_T = 1_000_000_000_000_000_000_000_000_000_000
    hailstones = [Hailstone.parse(l) for l in txt.splitlines()]
    count = 0
    for h1, h2 in itertools.combinations(hailstones, 2):
        future_h1, future_h2 = h1.at_t(FAR_FUTURE_T), h2.at_t(FAR_FUTURE_T)
        intersect = line_intersect(h1.px, h1.py, future_h1.px, future_h1.py, h2.px, h2.py, future_h2.px, future_h2.py)
        if intersect is not None:
            ix, iy = intersect
            if range_endpoints[0] <= ix <= range_endpoints[1] and range_endpoints[0] <= iy <= range_endpoints[1]:
                count += 1
    return count


def partb(txt: str) -> int:
    raise NotImplementedError()


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
