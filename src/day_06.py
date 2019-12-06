from datetime import date
from typing import List

import helpers


def get_masses(lines):
    return {mass: parent for parent, mass in (l.split(")") for l in lines)}


def depth(masses, mass):
    return len(ancestors(masses, mass))


def ancestors(masses, mass):
    parent = masses.get(mass)
    return set() if not parent else ancestors(masses, parent) | {parent}


def part1(lines: List[str]):
    masses = get_masses(lines)
    return sum(depth(masses, m) for m in masses)


def part2(lines: List[str]):
    masses = get_masses(lines)

    y_ancestors = ancestors(masses, "YOU")
    s_ancestors = ancestors(masses, "SAN")

    common_ancestors = y_ancestors & s_ancestors

    return len(y_ancestors) + len(s_ancestors) - 2 * len(common_ancestors)


def main():
    _, lines = helpers.get_puzzle(date(2019, 12, 6), "Universal Orbit Map")

    print(f"part1: {part1(lines)}")
    print(f"part2: {part2(lines)}")


if __name__ == "__main__":
    main()
