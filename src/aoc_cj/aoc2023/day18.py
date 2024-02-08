import enum
import itertools
import re
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from typing import ClassVar

import more_itertools as mi
from typing_extensions import Self


class Direction(enum.Enum):
    U = +0 - 1j
    D = +0 + 1j
    L = -1 + 0j
    R = +1 + 0j

    @staticmethod
    def is_right_turn(d1: "Direction", d2: "Direction") -> bool:
        return complex(-d1.value.imag, d1.value.real) == d2.value


@dataclass(frozen=True)
class Step:
    direction: "Direction"
    distance: int
    color: str

    PATTERN: ClassVar = re.compile(r"^(?P<direction>U|D|L|R) (?P<distance>\d+) \(#(?P<color>[0-9a-f]{6})\)$")
    INT_TO_DIRECTION_MAPPING: ClassVar = {"0": Direction.R, "1": Direction.D, "2": Direction.L, "3": Direction.U}
    DIRECTION_TO_INT_MAPPING: ClassVar = {v: k for k, v in INT_TO_DIRECTION_MAPPING.items()}

    @classmethod
    def parse(cls, s: str) -> Self:
        match = cls.PATTERN.match(s)
        assert match is not None
        return cls(
            direction=Direction[match.group("direction")],
            distance=int(match.group("distance")),
            color=match.group("color"),
        )

    def flip(self) -> Self:
        cls = self.__class__
        return cls(
            direction=cls.INT_TO_DIRECTION_MAPPING[self.color[-1]],
            distance=int("".join(self.color[:-1]), 16),
            color=hex(self.distance)[2:] + cls.DIRECTION_TO_INT_MAPPING[self.direction],
        )


@dataclass(frozen=True)
class DigPlan:
    steps: Sequence[Step]

    @classmethod
    def parse(cls, s: str, *, flipped: bool = False) -> Self:
        steps = (Step.parse(line) for line in s.splitlines())
        if flipped:
            steps = (s.flip() for s in steps)
        return cls(tuple(steps))

    def dig(self) -> int:
        start = 0 + 0j

        pos = start
        vertices = []
        for before, current, after in mi.sliding_window(
            itertools.chain((self.steps[-1],), self.steps, (self.steps[0],)), 3
        ):
            # modify our movements to move along the outside edge of the trench we're digging
            right_turn_count = sum(
                Direction.is_right_turn(s1.direction, s2.direction) for s1, s2 in mi.pairwise((before, current, after))
            )
            pos += current.direction.value * (current.distance + right_turn_count - 1)
            vertices.append(pos)
        assert pos == start

        res = area(vertices)
        assert res.is_integer()
        return int(res)


def area(vertices: Iterable[complex]) -> float:
    """
    Compute area of a polygon represented as an iterable of vertices

    modified version of code from https://rosettacode.org/wiki/Shoelace_formula_for_polygonal_area#Python:_Explicit
    """

    x, y = zip(*((int(p.real), int(p.imag)) for p in vertices), strict=True)
    return abs(sum(i * j for i, j in zip(x, y[1:] + y[:1])) - sum(i * j for i, j in zip(x[1:] + x[:1], y))) / 2


def part_1(txt: str) -> int:
    return DigPlan.parse(txt).dig()


def part_2(txt: str) -> int:
    return DigPlan.parse(txt, flipped=True).dig()


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
