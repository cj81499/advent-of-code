import itertools  # noqa
import re  # noqa
from collections import Counter, defaultdict, deque  # noqa


def parta(txt):
    spreadsheet = [[int(n) for n in line.split()] for line in txt.splitlines()]
    return sum(max(row) - min(row) for row in spreadsheet)


def partb(txt):
    spreadsheet = [[int(n) for n in line.split()] for line in txt.splitlines()]
    return sum(
        m // n
        for row in spreadsheet
        for m, n in itertools.permutations(row, r=2)
        if m % n == 0
    )


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
