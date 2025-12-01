from typing import Literal, TypeIs, override

type Direction = Literal["L", "R"]


def is_direction(d: str) -> TypeIs[Direction]:
    return d in ("L", "R")


class DialSolver:
    def __init__(self) -> None:
        self._dial_pos = 50
        self._zero_count = 0

    def _rotate(self, direction: Direction, distance: int) -> None:
        move = -distance if direction == "L" else distance
        self._dial_pos = (self._dial_pos + move) % 100
        if self._dial_pos == 0:
            self._zero_count += 1

    def solve(self, rotations: list[str]) -> int:
        for rotation in rotations:
            direction = rotation[0]
            assert is_direction(direction), f"rotation must start with 'L' or 'R'. Got '{direction}'"
            distance = int(rotation[1:])
            self._rotate(direction, distance)
        return self._zero_count


class DialSolver2(DialSolver):
    @override
    def _rotate(self, direction: Direction, distance: int) -> None:
        for _ in range(distance):
            super()._rotate(direction, 1)


def part_1(txt: str) -> int:
    return DialSolver().solve(txt.splitlines())


def part_2(txt: str) -> int:
    return DialSolver2().solve(txt.splitlines())


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
