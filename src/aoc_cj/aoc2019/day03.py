START = 0 + 0j
MOVEMENTS = {"U": 0 + 1j, "D": 0 - 1j, "R": 1 + 0j, "L": -1 + 0j}


def get_points(wire: str) -> dict[complex, int]:
    points: dict[complex, int] = {}
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


def wire_evaluator(lines, evaluator):
    first, second = (get_points(wire) for wire in lines)
    intersections = first.keys() & second.keys()
    measurements = [evaluator(p, first, second) for p in intersections]
    return min(measurements)


def part_1(txt: str) -> int:
    lines = txt.splitlines()

    def manhattan_distance(p: complex, f: dict[complex, int], s: dict[complex, int]) -> int:
        return int(abs(p.real) + abs(p.imag))

    return wire_evaluator(lines, manhattan_distance)


def part_2(txt: str) -> int:
    lines = txt.splitlines()

    def step_count(p: complex, f: dict[complex, int], s: dict[complex, int]) -> int:
        return f[p] + s[p]

    return wire_evaluator(lines, step_count)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
