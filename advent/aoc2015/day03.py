from datetime import date

import helpers
from point import Point

MOVES = {
    "^": Point(0, 1),
    "v": Point(0, -1),
    "<": Point(-1, 0),
    ">": Point(1, 0)
}


def part1(directions: str):
    pos = Point(0, 0)
    visited = set()
    visited.add(pos)
    for c in directions:
        pos += MOVES[c]
        visited.add(pos)
    return len(visited)


def part2(directions: str):
    pos = [Point(0, 0), Point(0, 0)]
    i = 0
    visited = set()
    visited.add(pos[0])
    for c in directions:
        pos[i] += MOVES[c]
        visited.add(pos[i])
        i = (i+1) % 2
    return len(visited)


def main():
    input_txt, _ = helpers.get_puzzle(date(2015, 12, 3), "Perfectly Spherical Houses in a Vacuum")  # noqa

    print(f"part1: {part1(input_txt)}")
    print(f"part2: {part2(input_txt)}")


if __name__ == "__main__":
    main()
