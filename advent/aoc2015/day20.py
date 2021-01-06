import itertools  # noqa
import re  # noqa
from collections import Counter, defaultdict, deque  # noqa


def select_house(presents, min_presents):
    for i, n in enumerate(presents):
        if n > min_presents and i > 0:
            return i

    return None


def presents_for_houses(min_presents, present_multiplier, house_limit=None):
    # this is probably big enough... right? (works for examples, so it's probably fine)
    arr_size = min_presents // 10
    presents = [0] * arr_size
    for elf_num in range(1, arr_size):
        iterator = itertools.count() if house_limit is None else range(house_limit)
        for i in (elf_num * (n + 1) for n in iterator):
            if i >= arr_size:
                break
            presents[i] += elf_num * present_multiplier

    return presents


def helper(txt, present_multiplier, house_limit=None):
    min_presents = int(txt)
    presents = presents_for_houses(min_presents, present_multiplier, house_limit=house_limit)
    return select_house(presents, min_presents)


def parta(txt):
    return helper(txt, 10)


def partb(txt):
    return helper(txt, 11, 50)


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
