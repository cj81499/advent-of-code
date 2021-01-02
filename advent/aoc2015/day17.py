from datetime import date
from itertools import combinations as combos
from typing import List

LITERS = 150


def get_good_combos(liters: int, lines: List[str]):
    containers = list(map(int, lines))
    good = []
    for i in range(len(containers)):
        size_good = [x for x in combos(containers, i) if sum(x) == liters]
        good.extend(size_good)
    return good


def parta(liters: int, lines: List[str]):
    return len(get_good_combos(liters, lines))


def partb(liters: int, lines: List[str]):
    good_combos = get_good_combos(liters, lines)
    min_len = min(map(len, good_combos))
    return sum(1 for x in good_combos if len(x) == min_len)


def main():
    _, input_lines = helpers.get_puzzle(date(2015, 12, 17), "No Such Thing as Too Much")  # noqa

    print(f"parta: {parta(LITERS, input_lines)}")
    print(f"partb: {partb(LITERS, input_lines)}")


if __name__ == "__main__":
    main()
