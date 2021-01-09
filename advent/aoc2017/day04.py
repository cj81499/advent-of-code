import itertools  # noqa
import re  # noqa
from collections import Counter, defaultdict, deque  # noqa


def is_valid(passphrase: str):
    words = passphrase.split()
    return len(set(words)) == len(words)


def parta(txt):
    return sum(is_valid(passphrase) for passphrase in txt.splitlines())


def is_valid_b(passphrase: str):
    words = passphrase.split()
    words = ["".join(sorted(word)) for word in words]
    return len(set(words)) == len(words)


def partb(txt):
    return sum(is_valid_b(passphrase) for passphrase in txt.splitlines())


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
