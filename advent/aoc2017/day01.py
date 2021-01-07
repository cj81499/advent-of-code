import itertools  # noqa
import re  # noqa
from collections import Counter, defaultdict, deque  # noqa


def parta(txt):
    return sum(int(c) for i, c in enumerate(txt) if c == txt[i - 1])


def partb(txt):
    return sum(int(c) for i, c in enumerate(txt) if c == txt[i - len(txt) // 2])


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
