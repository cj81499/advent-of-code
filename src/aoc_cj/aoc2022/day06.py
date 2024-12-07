import more_itertools as mi


def part_1(txt: str, n: int = 4) -> int:
    return mi.first(i for i, chars in enumerate(mi.windowed(txt, n), start=n) if mi.all_unique(chars))


def part_2(txt: str) -> int:
    return part_1(txt, 14)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
