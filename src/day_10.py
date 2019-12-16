import cmath
from datetime import date
from typing import List, Set

from src.util.helpers import get_puzzle

ASTEROID = "#"


def get_asteroids(lines: List[str]) -> Set[complex]:
    asteroids = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == ASTEROID:
                pos = complex(x, y)
                asteroids.add(pos)
    return asteroids


def part1(lines: List[str]) -> int:
    asteroids = get_asteroids(lines)
    return max(
        len(
            set(
                cmath.phase(a1 - a2)
                for a2 in asteroids if a2 != a1
            )
        ) for a1 in asteroids
    )


# def part2(lines: List[str]) -> None:
#     pass


def main() -> None:
    _, lines = get_puzzle(date(2019, 12, 10), "Monitoring Station")

    print(f"part1: {part1(lines)}")
    # print(f"part2: {part2(lines)}")


if __name__ == "__main__":
    main()
