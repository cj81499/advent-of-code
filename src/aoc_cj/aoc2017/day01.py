def part_1(txt):
    return sum(int(c) for i, c in enumerate(txt) if c == txt[i - 1])


def part_2(txt):
    return sum(int(c) for i, c in enumerate(txt) if c == txt[i - len(txt) // 2])


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
