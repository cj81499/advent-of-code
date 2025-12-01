def part_1(txt: str) -> int:
    dial_pos = 50
    zero_count = 0
    for rotation in txt.splitlines():
        direction = rotation[0]
        distance = int(rotation[1:])
        if direction == "L":
            dial_pos = (dial_pos - distance) % 100
        elif direction == "R":
            dial_pos = (dial_pos + distance) % 100
        else:
            assert False, f"unreachable. rotation must start with 'L' or 'R'. Got '{direction}'"
        if dial_pos == 0:
            zero_count += 1
    return zero_count


def part_2(txt: str) -> int:
    dial_pos = 50
    zero_count = 0
    for rotation in txt.splitlines():
        direction = rotation[0]
        pos_distance = int(rotation[1:])
        assert direction in ("L", "R"), f"rotation must start with 'L' or 'R'. Got '{direction}'"
        if direction == "L":
            move = -1
        else:
            move = 1
        for _ in range(pos_distance):
            dial_pos = (dial_pos + move) % 100
            if dial_pos == 0:
                zero_count += 1
    return zero_count


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
