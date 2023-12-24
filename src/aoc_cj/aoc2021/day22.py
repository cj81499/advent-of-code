import itertools
import re
from dataclasses import dataclass
from typing import Optional

PATTERN = re.compile(r"(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)")


def parse(line: str) -> tuple[str, int, int, int, int, int, int]:
    match = PATTERN.match(line)
    assert match is not None
    status, *nums = match.groups()
    min_x, max_x, min_y, max_y, min_z, max_z = map(int, nums)
    return status, min_x, max_x, min_y, max_y, min_z, max_z


def part_1(txt: str) -> int:
    on_points = set()
    for line in txt.splitlines():
        status, min_x, max_x, min_y, max_y, min_z, max_z = parse(line)
        if all(n in range(-50, 51) for n in (min_x, max_x, min_y, max_y, min_z, max_z)):
            for p in itertools.product(range(min_x, max_x + 1), range(min_y, max_y + 1), range(min_z, max_z + 1)):
                if status == "on":
                    on_points.add(p)
                elif status == "off":
                    on_points.discard(p)
    return len(on_points)


def part_2(txt: str) -> int:
    # idea shown in 2D, solution takes this approach, but generalized to 3D
    #
    # rather than adding each point, keep track of many rectangles (when we move to 3D, this'll be cubiods)
    # of regions that are on. at the end, we can simply sum the area of each rectangle (cubiod)
    #
    # For handling off, do something like this (for every on region)
    #
    # first on
    #
    #  +-------+
    #  |       |
    #  |  ON   |
    #  |       |
    #  +-------+
    #
    # overlaping off
    #
    #  +-------+
    #  |       |
    #  | ON +--+--+
    #  |    |  |  |
    #  +----+--+  |
    #       | OFF |
    #       +-----+
    #
    # simplifies to
    #
    #  +----+--+       +-------+            +----+--+
    #  |    |ON|       |  ON   |            | ON |ON|
    #  | ON +--+   or  +----+--+   or even  +----+--+
    #  |    |          | ON |               | ON |
    #  +----+          +----+               +----+
    #
    # (fewer splits ought to be better for performance)
    #
    # For handling on, we first turn that region off, then create a new cuboid for it.
    # Simply creating a new rectangle for it will result in double counting if any of the region was previously on.
    #
    # Key idea is that the region is now FAR too large to loop over all points.
    # Instead, we'll need to calculate volume.

    cc = CuboidCollection()
    for line in txt.splitlines():
        status, min_x, max_x, min_y, max_y, min_z, max_z = parse(line)
        c = Cuboid(min_x, max_x, min_y, max_y, min_z, max_z)
        if status == "on":
            cc.add(c)
        elif status == "off":
            cc.subtract(c)

    return cc.volume()


@dataclass(frozen=True)
class Cuboid:
    min_x: int
    max_x: int
    min_y: int
    max_y: int
    min_z: int
    max_z: int

    def _is_valid(self) -> bool:
        return (self.min_x <= self.max_x) and (self.min_y <= self.max_y) and (self.min_z <= self.max_z)

    def volume(self) -> int:
        return (self.max_x - self.min_x + 1) * (self.max_y - self.min_y + 1) * (self.max_z - self.min_z + 1)

    def intersection(self, other: "Cuboid") -> Optional["Cuboid"]:
        min_x = max(self.min_x, other.min_x)
        max_x = min(self.max_x, other.max_x)

        if min_x > max_x:
            return None

        min_y = max(self.min_y, other.min_y)
        max_y = min(self.max_y, other.max_y)

        if min_y > max_y:
            return None

        min_z = max(self.min_z, other.min_z)
        max_z = min(self.max_z, other.max_z)

        if min_z > max_z:
            return None

        return Cuboid(min_x, max_x, min_y, max_y, min_z, max_z)

    def subtract(self, other: "Cuboid") -> set["Cuboid"]:
        # if there is no intersection, return self
        if (isec := self.intersection(other)) is None:
            return {self}

        #       low # -> high #
        # x:     left -> right
        # y: forwards -> backwards
        # z:     down -> up

        # cuboid contained with self that is fully below isec
        a = Cuboid(self.min_x, self.max_x, self.min_y, self.max_y, self.min_z, isec.min_z - 1)
        # cuboid contained with self that is fully above isec
        b = Cuboid(self.min_x, self.max_x, self.min_y, self.max_y, isec.max_z + 1, self.max_z)
        # cuboid contained with self that is to left of isec at same height
        c = Cuboid(self.min_x, isec.min_x - 1, self.min_y, self.max_y, isec.min_z, isec.max_z)
        # # cuboid contained with self that is to right of isec at same height
        d = Cuboid(isec.max_x + 1, self.max_x, self.min_y, self.max_y, isec.min_z, isec.max_z)
        # cuboid contained with self that is directly in front of isec
        e = Cuboid(isec.min_x, isec.max_x, self.min_y, isec.min_y - 1, isec.min_z, isec.max_z)
        # cuboid contained with self that is directly in behind isec
        f = Cuboid(isec.min_x, isec.max_x, isec.max_y + 1, self.max_y, isec.min_z, isec.max_z)

        result = {a, b, c, d, e, f}

        # only return cuboids that have volume
        return {c for c in result if c._is_valid() and c.volume() > 0}


class CuboidCollection:
    def __init__(self) -> None:
        self._cuboids: set[Cuboid] = set()

    def volume(self) -> int:
        return sum(c.volume() for c in self._cuboids)

    def add(self, cuboid: Cuboid) -> None:
        self.subtract(cuboid)  # subtract the cuboid we're adding so we don't double count it
        self._cuboids.add(cuboid)

    def subtract(self, cuboid: Cuboid) -> None:
        self._cuboids = set(itertools.chain.from_iterable(c.subtract(cuboid) for c in self._cuboids))


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
