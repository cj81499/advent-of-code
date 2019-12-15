from datetime import date
from typing import List, Iterable
from itertools import permutations

import helpers


class Vector():
    def __init__(self, vector: Iterable[int]):
        self._vec = tuple(vector)

    def __repr__(self):
        return ", ".join(str(x) for x in self._vec)

    def __len__(self):
        return len(self._vec)

    def __eq__(self, other):
        return self._vec == other._vec

    def __add__(self, other):
        assert len(self) == len(other)
        return Vector(self[i] + other[i] for i in range(len(self)))

    def __getitem__(self, key):
        return self._vec[key]


class Moon():
    def __init__(self, x: int, y: int, z: int, vel: Vector = None):
        self.pos = Vector((x, y, z))
        self.vel = vel if vel else Vector((0, 0, 0))

    def __repr__(self):
        return f"Moon(pos: {self.pos}, vel: {self.vel})"

    def __eq__(self, other):
        return self.pos == other.pos and self.vel == other.vel

    def apply_gravity(self, other):
        deltas = (self._grav_helper(other, d) for d in range(3))
        self.vel += Vector(deltas)

    def _grav_helper(self, other, dimension: int) -> int:
        # TODO: Clean
        if self.pos[dimension] == other.pos[dimension]:
            return 0
        return 1 if self.pos[dimension] < other.pos[dimension] else - 1

    def apply_velocity(self):
        self.pos += self.vel

    @staticmethod
    def parse_pos(position: str):
        body: str = position[1:-1]
        coordinate_strs = body.split(", ")
        coordinates = [int(s[2:]) for s in coordinate_strs]
        return Moon(*coordinates)


def step(moons):
    # Apply gravity
    for m1, m2 in permutations(moons, 2):
        m1.apply_gravity(m2)

    # Apply velocity
    for m in moons:
        m.apply_velocity()


def total_energy(moons):
    def energy(moon: Moon):
        def pot_energy(moon: Moon):
            return sum(abs(v) for v in moon.pos)

        def kin_energy(moon: Moon):
            return sum(abs(v) for v in moon.vel)

        return kin_energy(moon) * pot_energy(moon)

    return sum(energy(m) for m in moons)


def parse_moons(lines: List[str]) -> List[Moon]:
    return [Moon.parse_pos(l) for l in lines]


def part1(lines: List[str]):
    moons = parse_moons(lines)

    for i in range(1000):
        step(moons)

    return total_energy(moons)


# def part2(lines: List[str]):
#     pass


def main():
    _, lines = helpers.get_puzzle(date(2019, 12, 12), "The N-Body Problem")

    print(f"part1: {part1(lines)}")
    # print(f"part2: {part2(lines)}")


if __name__ == "__main__":
    main()
