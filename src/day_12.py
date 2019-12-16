from __future__ import annotations

from datetime import date
from itertools import permutations
from typing import Iterable, Iterator, List, Optional

from src.util.helpers import get_puzzle


class Vector():
    def __init__(self, vector: Iterable[int]) -> None:
        self._vec = tuple(vector)

    def __repr__(self) -> str:
        return ", ".join(str(x) for x in self._vec)

    def __len__(self) -> int:
        return len(self._vec)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Vector) and self._vec == other._vec

    def __add__(self, other: Vector) -> Vector:
        assert len(self) == len(other)
        return Vector(self[i] + other[i] for i in range(len(self)))

    def __getitem__(self, index: int) -> int:
        return self._vec[index]

    def __iter__(self) -> Iterator[int]:
        return iter(self._vec)


class Moon():
    def __init__(
        self, x: int, y: int, z: int, vel: Optional[Vector] = None
    ) -> None:
        self.pos = Vector((x, y, z))
        self.vel = vel if vel else Vector((0, 0, 0))

    def __repr__(self) -> str:
        return f"Moon(pos: {self.pos}, vel: {self.vel})"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Moon) and \
            self.pos == other.pos and \
            self.vel == other.vel

    def apply_gravity(self, other: Moon) -> None:
        deltas = (self._grav_helper(other, d) for d in range(3))
        self.vel += Vector(deltas)

    def _grav_helper(self, other: Moon, dimension: int) -> int:
        # TODO: Clean
        if self.pos[dimension] == other.pos[dimension]:
            return 0
        return 1 if self.pos[dimension] < other.pos[dimension] else - 1

    def apply_velocity(self) -> None:
        self.pos += self.vel

    @staticmethod
    def parse_pos(position: str) -> Moon:
        body: str = position[1:-1]
        coordinate_strs = body.split(", ")
        x, y, z = [int(s[2:]) for s in coordinate_strs]
        return Moon(x, y, z)


def step(moons: List[Moon]) -> None:
    # Apply gravity
    for m1, m2 in permutations(moons, 2):
        m1.apply_gravity(m2)

    # Apply velocity
    for m in moons:
        m.apply_velocity()


def total_energy(moons: List[Moon]) -> int:
    def energy(moon: Moon) -> int:
        def pot_energy(moon: Moon) -> int:
            return sum(abs(v) for v in moon.pos)

        def kin_energy(moon: Moon) -> int:
            return sum(abs(v) for v in moon.vel)

        return kin_energy(moon) * pot_energy(moon)

    return sum(energy(m) for m in moons)


def parse_moons(lines: List[str]) -> List[Moon]:
    return [Moon.parse_pos(l) for l in lines]


def part1(lines: List[str]) -> int:
    moons = parse_moons(lines)

    for i in range(1000):
        step(moons)

    return total_energy(moons)


# def part2(lines: List[str]):
#     pass


def main() -> None:
    _, lines = get_puzzle(date(2019, 12, 12), "The N-Body Problem")

    print(f"part1: {part1(lines)}")
    # print(f"part2: {part2(lines)}")


if __name__ == "__main__":
    main()
