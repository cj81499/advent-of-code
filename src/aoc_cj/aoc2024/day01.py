import collections


def parse(txt: str) -> tuple[tuple[int, ...], tuple[int, ...]]:
    ints_by_line = (tuple(int(x) for x in line.split()) for line in txt.splitlines())
    transpose = zip[tuple[int, ...]](*ints_by_line)
    tup = tuple(transpose)
    if len(tup) != 2:
        raise ValueError
    return tup


def part_1(txt: str) -> int:
    left_col, right_col = parse(txt)
    return sum(abs(l - r) for l, r in zip(sorted(sorted(left_col)), sorted(sorted(right_col))))


def part_2(txt: str) -> int:
    left_col, right_col = parse(txt)
    right_counts = collections.Counter(right_col)

    return sum(l * right_counts[l] for l in left_col)


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
