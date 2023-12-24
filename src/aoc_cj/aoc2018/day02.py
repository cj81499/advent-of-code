import itertools
from collections import Counter


def part_1(txt):
    c = Counter()
    for line in txt.splitlines():
        s = set(Counter(line).values())
        c.update(s)
    return c[2] * c[3]


def part_2(txt):
    for s1, s2 in itertools.product(txt.splitlines(), repeat=2):
        if sum(a != b for a, b in zip(s1, s2)) == 1:
            return "".join(a for a, b in zip(s1, s2) if a == b)


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
