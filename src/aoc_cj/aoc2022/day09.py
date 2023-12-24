from collections.abc import Generator

ORIGIN = 0 + 0j

UP = 0 + 1j  # positive imag -> up
DOWN = 0 - 1j  # negative imag -> down
LEFT = -1 + 0j  # negative real -> left
RIGHT = 1 + 0j  # positive real -> right

DIRECTIONS = {"U": UP, "D": DOWN, "L": LEFT, "R": RIGHT}


def parse_motions(txt: str) -> Generator[tuple[complex, int], None, None]:
    for line in txt.splitlines():
        direction, distance = line.split()
        yield DIRECTIONS[direction], int(distance)


def pull(lead_knot: complex, trail_knot: complex) -> complex:
    new_back_knot = trail_knot

    # if front_knot is far enough away, back_knot moves up to 1 position in each direction towards front_knot
    real_difference = lead_knot.real - trail_knot.real
    imag_difference = lead_knot.imag - trail_knot.imag
    if abs(real_difference) >= 2 or abs(imag_difference) >= 2:
        if real_difference != 0:
            new_back_knot += real_difference / abs(real_difference)
        if imag_difference != 0:
            new_back_knot += 1j * imag_difference / abs(imag_difference)

    return new_back_knot


def part_1(txt: str, rope_length: int = 2) -> int:
    # knot @ start is head, knot @ end is tail
    knot_positions = [ORIGIN for _ in range(rope_length)]

    # keep track of where the tail has been
    tail_visited = {ORIGIN}

    for direction, distance in parse_motions(txt):
        for _ in range(distance):
            head_of_rope, *rest_of_rope = knot_positions

            # move head in selected direction
            new_knot_positions = [head_of_rope + direction]

            # pull the rest of the rope behind it
            for knot_position in rest_of_rope:
                new_knot_positions.append(pull(new_knot_positions[-1], knot_position))

            knot_positions = new_knot_positions

            # the tail may have moved
            tail_visited.add(knot_positions[-1])

    return len(tail_visited)


def part_2(txt: str) -> int:
    return part_1(txt, 10)


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
