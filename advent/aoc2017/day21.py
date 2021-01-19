from __future__ import annotations

import itertools  # noqa
import re  # noqa
from collections import Counter, defaultdict, deque  # noqa

import numpy as np

INITIAL = """
.#.
..#
###
""".strip()


def all_orientations(grid):
    flipped = np.fliplr(grid)
    return (
        grid, np.rot90(grid), np.rot90(grid, 2), np.rot90(grid, 3),
        flipped, np.rot90(flipped), np.rot90(flipped, 2), np.rot90(flipped, 3),
    )


def grid_to_s(g):
    return "/".join("".join(row) for row in g)


def enhance(subgrid, rules):
    return np.array([[*line] for line in rules.get(grid_to_s(subgrid)).split("/")])


def parse_rules(txt: str):
    rules = dict(line.split(" => ") for line in txt.splitlines())
    expanded = {}
    for rule, result in rules.items():
        rule_grid = np.array([[*line] for line in rule.split("/")])
        for o in all_orientations(rule_grid):
            expanded[grid_to_s(o)] = result
    return expanded


def parta(txt: str, iterations=5):
    rules = parse_rules(txt)
    grid = np.array([[*line] for line in INITIAL.splitlines()])
    for i in range(iterations):
        n = 2 if len(grid) % 2 == 0 else 3
        split_count = len(grid) // n
        grid = np.vstack(tuple(
            np.hstack(tuple(
                enhance(s, rules) for s in np.hsplit(row, split_count)
            ))
            for row in np.vsplit(grid, split_count)
        ))
    return np.count_nonzero(grid == "#")


def partb(txt: str):
    return parta(txt, iterations=18)


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
