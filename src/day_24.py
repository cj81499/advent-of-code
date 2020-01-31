from datetime import date
from typing import List, Set, Tuple

from src.util.helpers import get_puzzle

BUG = "#"

GRID_SIZE = 5

Bugs = Set[complex]
State = Tuple[Tuple[int, int], ...]


def adj(pos: complex) -> List[complex]:
    adjustments = (1 + 0j, -1 + 0j, 0 + 1j, 0 - 1j)
    return [pos + adjust for adjust in adjustments]


def step(bugs: Bugs) -> Bugs:
    new_bugs = set()
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            pos = complex(x, y)
            adj_count = sum(1 for p in adj(pos) if p in bugs)
            if (adj_count == 1 if pos in bugs else adj_count in (1, 2)):
                new_bugs.add(pos)
    return new_bugs


def parse_bugs(lines: List[str]) -> Bugs:
    bugs = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == BUG:
                bugs.add(complex(x, y))
    return bugs


def bugs_to_state(bugs: Bugs) -> State:
    return tuple(sorted((int(c.real), int(c.imag)) for c in bugs))


def find_first_repeat(bugs: Bugs) -> Bugs:
    seen: Set[State] = set()
    state = bugs_to_state(bugs)
    while state not in seen:
        seen.add(state)
        bugs = step(bugs)
        state = bugs_to_state(bugs)
    return bugs


def biodiversity(bugs: Bugs) -> int:
    total_points = 0
    point_at_pos = 1
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            pos = complex(x, y)
            if pos in bugs:
                total_points += point_at_pos
            point_at_pos *= 2
    return total_points


def part1(lines: List[str]) -> int:
    bugs = parse_bugs(lines)
    first_repeat = find_first_repeat(bugs)
    return biodiversity(first_repeat)


# def part2(lines: List[str]) -> int:
#     return 0


def main() -> None:
    _, lines = get_puzzle(date(2019, 12, 24), "Planet of Discord")  # noqa

    print(f"part1: {part1(lines)}")
    # print(f"part2: {part2(lines)}")


if __name__ == "__main__":
    main()
