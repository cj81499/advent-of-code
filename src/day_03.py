from datetime import date
from typing import Callable, Dict, List

from src.util.helpers import get_puzzle

START = 0 + 0j
MOVEMENTS = {"U":  0 + 1j, "D":  0 - 1j, "R":  1 + 0j, "L": -1 + 0j}


def get_points(wire: str) -> Dict[complex, int]:
    points: Dict[complex, int] = {}
    commands = wire.split(",")
    pos = START
    steps = 1
    for c in commands:
        direction, distance = c[0], int(c[1:])
        move = MOVEMENTS[direction]
        for _ in range(distance):
            pos += move
            if pos not in points:
                points[pos] = steps
            steps += 1
    return points


def wire_evaluator(
    lines: List[str],
    evaluator_func: Callable[
        [complex, Dict[complex, int], Dict[complex, int]], int
    ]
) -> int:
    first, second = (get_points(wire) for wire in lines)
    intersections = first.keys() & second.keys()
    measurements = [evaluator_func(p, first, second) for p in intersections]
    return min(measurements)


def part1(lines: List[str]) -> int:
    def manhattan_distance(
        p: complex,
        f: Dict[complex, int],
        s: Dict[complex, int]
    ) -> int:
        return int(abs(p.real) + abs(p.imag))

    return wire_evaluator(lines, manhattan_distance)


def part2(lines: List[str]) -> int:
    def step_count(
        p: complex,
        f: Dict[complex, int],
        s: Dict[complex, int]
    ) -> int:
        return f[p] + s[p]

    return wire_evaluator(lines, step_count)


def main() -> None:
    _, lines = get_puzzle(date(2019, 12, 3), "Crossed Wires")

    print(f"part1: {part1(lines)}")
    print(f"part2: {part2(lines)}")


if __name__ == "__main__":
    main()
