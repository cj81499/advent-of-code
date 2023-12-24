def part_1(txt: str):
    return follow_instructions(txt)


def part_2(txt: str):
    return follow_instructions(txt, stop_at_repeat=True)


def follow_instructions(instructions: str, stop_at_repeat=False):
    direction = -1j
    pos = 0j
    seen = set()
    for move in instructions.split(", "):
        direction = (
            complex(-direction.imag, direction.real) if move[0] == "R" else complex(direction.imag, -direction.real)
        )
        for _ in range(int(move[1:])):
            pos += direction
            if stop_at_repeat and pos in seen:
                return man_dist(pos)
            seen.add(pos)
    return man_dist(pos)


def man_dist(pos):
    return abs(int(pos.real)) + abs(int(pos.imag))


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
