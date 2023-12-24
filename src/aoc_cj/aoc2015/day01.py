from collections import Counter


def part_1(s: str):
    c = Counter(s)
    return c["("] - c[")"]


def part_2(s: str):
    floor = 0
    for i, x in enumerate(s):
        floor += 1 if x == "(" else -1
        if floor == -1:
            return i + 1


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
