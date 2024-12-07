def helper(txt):
    x, y, z = 0, 0, 0
    all_time_max = 0
    for move in txt.split(","):
        if move == "n":
            y += 1
            z -= 1
        elif move == "ne":
            x += 1
            z -= 1
        elif move == "se":
            x += 1
            y -= 1
        elif move == "s":
            y -= 1
            z += 1
        elif move == "sw":
            x -= 1
            z += 1
        elif move == "nw":
            x -= 1
            y += 1
        all_time_max = max(all_time_max, x, y, z)
    return max(x, y, z), all_time_max


def part_1(txt: str):
    return helper(txt)[0]


def part_2(txt: str):
    return helper(txt)[1]


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
