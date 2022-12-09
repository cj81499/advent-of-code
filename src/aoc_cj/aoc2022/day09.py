DIRECTIONS = {
    "U": 0 + 1j,  # positive imag -> up
    "D": 0 - 1j,  # negative imag -> down
    "L": -1 + 0j,  # negative real -> left
    "R": 1 + 0j,  # positive real -> right
}

ORIGIN = 0 + 0j


def move(head: complex, tail: complex, direction: complex) -> tuple[complex, complex]:
    new_head = head + direction
    new_tail = tail

    # if change in real >= 2 or change in imag >= 2, tail will move to "old" head
    if abs(new_head.real - tail.real) >= 2 or abs(new_head.imag - tail.imag) >= 2:
        new_tail = head

    return new_head, new_tail


def pull(head: complex, tail: complex) -> complex:
    # if head is far enough away, tail moves to where head used to be
    if abs(head.real - tail.real) >= 2 or abs(head.imag - tail.imag) >= 2:
        new_tail = tail

        if abs(head.real - tail.real) != 0:
            new_tail += (head.real - tail.real) / abs(head.real - tail.real)
        if abs(head.imag - tail.imag) != 0:
            new_tail += 1j * ((head.imag - tail.imag) / abs(head.imag - tail.imag))
        return new_tail
    return tail


def parta(txt: str) -> int:

    head_pos = ORIGIN
    tail_pos = ORIGIN

    tail_positions = {ORIGIN}

    for motion in txt.splitlines():
        direction_s, distance_s = motion.split()
        direction = DIRECTIONS[direction_s]
        distance = int(distance_s)

        for _ in range(distance):
            head_pos, tail_pos = move(head_pos, tail_pos, direction)
            tail_positions.add(tail_pos)

    return len(tail_positions)


def partb(txt: str) -> int:
    # knot @ start is head, knot @ end is tail
    knot_positions = [ORIGIN for _ in range(10)]

    tail_positions = {ORIGIN}

    for motion in txt.splitlines():
        direction_s, distance_s = motion.split()
        direction = DIRECTIONS[direction_s]
        distance = int(distance_s)

        for _ in range(distance):
            # pull the rope

            # move head in selected direction
            new_knot_positions = []
            new_knot_positions.append(knot_positions[0] + direction)
            # move the rest of the rope behind it
            for i, k in enumerate(knot_positions[1:], start=1):
                new_knot_positions.append(pull(new_knot_positions[-1], k))

            knot_positions = new_knot_positions

            # the tail may have moved
            tail_positions.add(knot_positions[-1])

    return len(tail_positions)


def main(txt: str) -> None:
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
