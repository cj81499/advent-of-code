"""
This solution is *obnoxiously* slow (~30m for part 2 iirc. I'm not running it again to confirm that.)
"""

import itertools
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from typing import Self, override

from aoc_cj import util

DOWN = util.Point3D(0, 0, -1)


@dataclass
class Brick:
    c1: util.Point3D
    c2: util.Point3D

    @override
    def __str__(self) -> str:
        return f"({self.c1}, {self.c2})"

    @classmethod
    def parse(cls, s: str) -> Self:
        l, sep, r = s.partition("~")
        assert sep == "~"
        c1 = util.Point3D.parse(l)
        c2 = util.Point3D.parse(r)
        assert c1.x <= c2.x and c1.y <= c2.y and c1.z <= c2.z
        return cls(c1, c2)

    def fall(self, other_bricks: Iterable[Self]) -> Self:
        if self.c1.z == 1:  # if on ground, cannot fall
            return self

        for other in other_bricks:
            if (
                self.c1.z == other.c2.z + 1  # if self's lowest point is 1 above other's highest point
                and (
                    other.c1.x <= self.c1.x <= other.c2.x
                    or other.c1.x <= self.c2.x <= other.c2.x
                    or self.c1.x <= other.c1.x <= self.c2.x
                    or self.c1.x <= other.c2.x <= self.c2.x
                )
                and (
                    other.c1.y <= self.c1.y <= other.c2.y
                    or other.c1.y <= self.c2.y <= other.c2.y
                    or self.c1.y <= other.c1.y <= self.c2.y
                    or self.c1.y <= other.c2.y <= self.c2.y
                )
            ):
                return self

        cls = self.__class__
        return cls(self.c1 + DOWN, self.c2 + DOWN)


def parse(txt: str) -> Sequence[Brick]:
    # sorting bricks by z improves ability to simulate gravity
    original_bricks = sorted((Brick.parse(line) for line in txt.splitlines()), key=lambda b: (b.c1.z, b.c2.z))
    return simulate_falling(original_bricks)


def simulate_falling(bricks: Sequence[Brick]) -> Sequence[Brick]:
    while True:
        new_bricks = simulate_fall_one_step(bricks)
        if new_bricks == bricks:
            return bricks
        bricks = new_bricks


def simulate_fall_one_step(bricks: Sequence[Brick]) -> Sequence[Brick]:
    return [b.fall(itertools.chain(bricks[:i], bricks[i + 1 :])) for i, b in enumerate(bricks)]


def part_1(txt: str) -> int:
    bricks = parse(txt)

    return sum(
        1
        for i, b in enumerate(bricks)
        if (other_bricks := list(itertools.chain(bricks[:i], bricks[i + 1 :]))) == simulate_fall_one_step(other_bricks)
    )


def part_2(txt: str) -> int:
    bricks = parse(txt)

    count = 0
    for i, b in enumerate(bricks):
        other_bricks = list(itertools.chain(bricks[:i], bricks[i + 1 :]))
        after_falling = simulate_falling(other_bricks)
        count += sum(1 for b1, b2 in zip(other_bricks, after_falling) if b1 != b2)
    return count


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
