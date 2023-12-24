def part_1(txt):
    return simulate_slope(txt, 3, 1)


def simulate_slope(txt, right, down):
    lines = txt.strip().splitlines()
    count = 0

    y = 0
    x = 0

    while y < len(lines):
        if lines[y][x % len(lines[y])] == "#":
            count += 1
        y += down
        x += right

    return count


def part_2(txt):
    return (
        simulate_slope(txt, 1, 1)
        * simulate_slope(txt, 3, 1)
        * simulate_slope(txt, 5, 1)
        * simulate_slope(txt, 7, 1)
        * simulate_slope(txt, 1, 2)
    )


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
