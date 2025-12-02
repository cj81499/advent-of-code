import more_itertools


def part_1(txt: str) -> int:
    ranges = txt.replace("\n", "").split(",")
    tot = 0
    for r in ranges:
        start, sep, end = r.partition("-")
        assert sep == "-"
        start, end = int(start), int(end)
        for n in range(start, end + 1):
            s = str(n)
            l = len(s)
            if l % 2 == 0 and s[: l // 2] == s[l // 2 :]:
                tot += n
    return tot


def part_2(txt: str) -> int:
    ranges = txt.replace("\n", "").split(",")
    tot = 0
    for r in ranges:
        start, sep, end = r.partition("-")
        assert sep == "-"
        start, end = int(start), int(end)
        for n in range(start, end + 1):
            s = str(n)
            l = len(s)
            if any(
                l % chunk_size == 0 and more_itertools.all_equal(more_itertools.chunked(s, chunk_size, strict=True))
                for chunk_size in range(1, (len(s) // 2) + 1)
            ):
                tot += n
    return tot


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
