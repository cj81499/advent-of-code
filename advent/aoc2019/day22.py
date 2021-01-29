from __future__ import annotations

import itertools  # noqa
import re  # noqa
from collections import Counter, defaultdict, deque  # noqa


def deck_of_size(n):
    return [x for x in range(n)]


def deal_into_new_stack(deck):
    return list(reversed(deck))


def cut(deck, n):
    return deck[n:] + deck[:n]


def deal_with_increment(deck, n):
    new_deck = [None] * len(deck)
    for i, x in enumerate(deck):
        new_deck[(i * n) % len(new_deck)] = x
    return new_deck


def perform_shuffle(txt: str, deck_size=10007, repeat=1):
    deck = deck_of_size(deck_size)
    for _ in range(repeat):
        for instruction in txt.splitlines():
            if instruction == "deal into new stack":
                deck = deal_into_new_stack(deck)
            elif instruction.startswith("cut "):
                deck = cut(deck, int(instruction.split()[-1]))
            elif instruction.startswith("deal with increment "):
                deck = deal_with_increment(deck, int(instruction.split()[-1]))
            else:
                print("unrecognized shuffle instruction:", instruction)
                exit(1)
    return deck


def parta(txt: str):
    return perform_shuffle(txt).index(2019)


def partb(txt: str):
    pass
    # return perform_shuffle(txt, deck_size=119315717514047, repeat=101741582076661)[2020]


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
