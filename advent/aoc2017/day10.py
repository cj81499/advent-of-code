from __future__ import annotations

import itertools  # noqa
import re  # noqa
from collections import Counter, defaultdict, deque  # noqa
from functools import reduce
from operator import xor

SUFFIX = (17, 31, 73, 47, 23)
DEFAULT_LIST_SIZE = 256


def do_round(nums, lengths, pos=0, skip_size=0):
    list_size = len(nums)
    for length in lengths:
        for i in range(length // 2):
            a = (pos + i) % list_size
            b = (pos + length - 1 - i) % list_size
            nums[a], nums[b] = nums[b], nums[a]
        pos = (pos + length + skip_size) % list_size
        skip_size += 1
    return pos, skip_size


def chunks(to_chunk, chunk_size):
    for i in range(0, len(to_chunk), chunk_size):
        yield to_chunk[i:i + chunk_size]


def dense_hash(sparse_hash):
    return "".join(hex(reduce(xor, c))[2:].zfill(2) for c in chunks(sparse_hash, 16))


def knot_hash(txt: str):
    ascii_codes = list(map(ord, txt))
    lengths = [*ascii_codes, *SUFFIX]
    nums = [*range(DEFAULT_LIST_SIZE)]
    pos = 0
    skip_size = 0
    for _ in range(64):
        pos, skip_size = do_round(nums, lengths, pos=pos, skip_size=skip_size)
    sparse_hash = tuple(nums)
    return dense_hash(sparse_hash)


def parta(txt: str, list_size: int = DEFAULT_LIST_SIZE):
    lengths = list(map(int, txt.split(",")))
    nums = [*range(list_size)]
    do_round(nums, lengths)
    return nums[0] * nums[1]


def partb(txt: str):
    return knot_hash(txt)


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
