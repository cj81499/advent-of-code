import heapq


def part_1(txt: str) -> int:
    total_paper = 0
    for box in txt.splitlines():
        length, width, height = (int(x) for x in box.split("x"))
        a_sides = [length * width, width * height, height * length]
        sa = sum(2 * x for x in a_sides)
        total_paper += sa + min(a_sides)
    return total_paper


def part_2(txt: str) -> int:
    total_ribbon = 0
    for box in txt.splitlines():
        dims = [int(x) for x in box.split("x")]
        length, width, height = dims
        total_ribbon += sum(2 * x for x in heapq.nsmallest(2, dims)) + length * width * height
    return total_ribbon


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
