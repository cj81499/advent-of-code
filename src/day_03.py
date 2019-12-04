from datetime import date
from typing import List, Dict, Callable

import helpers

START = 0 + 0j

MOVEMENTS = {"U":  0 + 1j, "D":  0 - 1j, "R":  1 + 0j, "L": -1 + 0j}


def get_points(wire: List[str]) -> Dict[complex, int]:
    points = {}
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


def wire_evaluator(lines: List[str], evaluator_func: Callable) -> int:
    first, second = (get_points(wire) for wire in lines)
    intersections = first.keys() & second.keys()
    measurements = [evaluator_func(p, first, second) for p in intersections]
    return min(measurements)


def part1(lines: List[str]) -> int:
    def manhattan_distance(p, f, s) -> int:
        return int(abs(p.real) + abs(p.imag))

    return wire_evaluator(lines, manhattan_distance)


def part2(lines: List[str]) -> int:
    def step_count(p, f, s) -> int:
        return f[p] + s[p]

    return wire_evaluator(lines, step_count)


def main():
    _, lines = helpers.get_puzzle(date(2019, 12, 3), "Crossed Wires")

    print(f"part1: {part1(lines)}")
    print(f"part2: {part2(lines)}")


if __name__ == "__main__":
    main()
