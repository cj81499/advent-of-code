import itertools
from collections import Counter


def parta(txt):
    c = Counter()
    for line in txt.splitlines():
        s = set(Counter(line).values())
        c.update(s)
    return c[2] * c[3]


def partb(txt):
    for s1, s2 in itertools.product(txt.splitlines(), repeat=2):
        if sum(a != b for a, b in zip(s1, s2)) == 1:
            return "".join(a for a, b in zip(s1, s2) if a == b)


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
