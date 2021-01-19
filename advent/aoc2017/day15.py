from __future__ import annotations

import itertools  # noqa
import re  # noqa
from collections import Counter, defaultdict, deque  # noqa

DIVISOR = 2147483647
FACTOR_A = 16807
FACTOR_B = 48271

MASK = 0xFFFF

FOURTY_MILLION = 40_000_000
FIVE_MILLION = 5_000_000


def parta(txt: str, num_loops=FOURTY_MILLION):
    a, b = [int(line.split()[-1]) for line in txt.splitlines()]
    matches = 0
    for _ in range(num_loops):
        a = (a * FACTOR_A) % DIVISOR
        b = (b * FACTOR_B) % DIVISOR
        # bitwise and to get last 16 bits
        if (a & MASK) == (b & MASK):
            matches += 1
    return matches


def partb(txt: str, num_loops=FIVE_MILLION):
    a, b = [int(line.split()[-1]) for line in txt.splitlines()]
    matches = 0
    for _ in range(num_loops):
        a = (a * FACTOR_A) % DIVISOR
        while a % 4 != 0:
            a = (a * FACTOR_A) % DIVISOR
        b = (b * FACTOR_B) % DIVISOR
        while b % 8 != 0:
            b = (b * FACTOR_B) % DIVISOR
        # bitwise and to mask
        if (a & MASK) == (b & MASK):
            matches += 1
    return matches


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
