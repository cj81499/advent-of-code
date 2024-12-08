import heapq


def part_1(txt: str) -> int:
    total_paper = 0
    for box in txt.splitlines():
        l, w, h = (int(x) for x in box.split("x"))
        a_sides = [l * w, w * h, h * l]
        sa = sum(2 * x for x in a_sides)
        total_paper += sa + min(a_sides)
    return total_paper


def part_2(txt: str) -> int:
    total_ribbon = 0
    for box in txt.splitlines():
        dims = [int(x) for x in box.split("x")]
        l, w, h = dims
        total_ribbon += sum(2 * x for x in heapq.nsmallest(2, dims)) + l * w * h
    return total_ribbon


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
