import more_itertools as mi

from aoc_cj import util

SAND_SOURCE = 500 + 0j

ROCK = "#"
SAND = "o"


def parse(txt: str) -> tuple[dict[complex, str], float]:
    grid: dict[complex, str] = {}
    for text_line in txt.splitlines():
        for a, b in mi.pairwise(tuple(util.ints(rock_line)) for rock_line in text_line.split(" -> ")):
            a_x, a_y = a
            b_x, b_y = b

            start_x, end_x = min(a_x, b_x), max(a_x, b_x)
            start_y, end_y = min(a_y, b_y), max(a_y, b_y)
            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    grid[complex(x, y)] = ROCK

    max_rock_y = max(p.imag for p in grid)
    return grid, max_rock_y


def part_1(txt: str) -> int:
    grid, max_rock_y = parse(txt)

    count = 0
    sand_falling_forever = False
    while not sand_falling_forever:
        # simulate single unit of falling sand
        sand_pos = SAND_SOURCE
        sand_at_rest = False
        while not (sand_at_rest or sand_falling_forever):
            if sand_pos.imag > max_rock_y:
                sand_falling_forever = True
            elif (below_sand := sand_pos + 1j) not in grid:
                sand_pos = below_sand
            elif (diag_left := sand_pos + complex(-1, 1)) not in grid:
                sand_pos = diag_left
            elif (diag_right := sand_pos + complex(1, 1)) not in grid:
                sand_pos = diag_right
            else:
                sand_at_rest = True
        if sand_at_rest:
            grid[sand_pos] = SAND
            count += 1

    return count


def part_2(txt: str) -> int:
    grid, max_rock_y = parse(txt)

    floor_y = max_rock_y + 2

    count = 0
    while SAND_SOURCE not in grid:
        # simulate single unit of falling sand
        sand_pos = SAND_SOURCE
        sand_at_rest = False
        while not sand_at_rest:
            if sand_pos.imag + 1 == floor_y:
                sand_at_rest = True
            elif (below_sand := sand_pos + 1j) not in grid:
                sand_pos = below_sand
            elif (diag_left := sand_pos + complex(-1, 1)) not in grid:
                sand_pos = diag_left
            elif (diag_right := sand_pos + complex(1, 1)) not in grid:
                sand_pos = diag_right
            else:
                sand_at_rest = True
        if sand_at_rest:
            grid[sand_pos] = SAND
            count += 1

    return count


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
