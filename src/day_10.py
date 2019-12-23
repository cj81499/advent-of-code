import math
from datetime import date
from typing import List, Set

from src.util.helpers import get_puzzle

ASTEROID = "#"


def deg(origin: complex, point: complex) -> float:
    difference = point - origin
    # flip the imaginary part b/c 0j is top row of input
    angle = math.atan2(difference.real, -difference.imag)
    deg = math.degrees(angle)
    if deg < 0:
        deg += 360
    return deg


def get_asteroids(lines: List[str]) -> Set[complex]:
    asteroids = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == ASTEROID:
                pos = complex(x, y)
                asteroids.add(pos)
    return asteroids


def count_observable(candidate: complex, asteroids: Set[complex]) -> int:
    angles = set(deg(candidate, a) for a in asteroids if a != candidate)
    return len(angles)


def part1(lines: List[str]) -> int:
    asteroids = get_asteroids(lines)
    base_location = best_asteroid(asteroids)
    return count_observable(base_location, asteroids)


def best_asteroid(asteroids: Set[complex]) -> complex:
    return max(asteroids, key=lambda a: count_observable(a, asteroids))


def dist(a: complex, b: complex) -> float:
    diff = a - b
    return (diff.real**2 + diff.imag**2)**0.5


def vaporize_order(lines: List[str]) -> List[complex]:
    asteroids = get_asteroids(lines)
    base_location = best_asteroid(asteroids)
    asteroids.remove(base_location)

    distances = {a: dist(base_location, a) for a in asteroids}
    angles = {a: deg(base_location, a) for a in asteroids}

    order = []
    angle = -1.0
    while asteroids:
        after_last_angle = set(a for a in asteroids if angles[a] > angle)
        if len(after_last_angle) == 0:
            angle = -1
            continue
        angle = min(angles[a] for a in after_last_angle)
        asteroids_at_angle = set(
            a for a in after_last_angle if angles[a] == angle)
        vaporize = min(asteroids_at_angle, key=lambda a: distances[a])
        order.append(vaporize)
        asteroids.remove(vaporize)
    return order


def part2(lines: List[str]) -> int:
    order = vaporize_order(lines)
    bet_result = order[200 - 1]
    return int(bet_result.real*100 + bet_result.imag)


def main() -> None:
    _, lines = get_puzzle(date(2019, 12, 10), "Monitoring Station")

    print(f"part1: {part1(lines)}")
    print(f"part2: {part2(lines)}")


if __name__ == "__main__":
    main()
