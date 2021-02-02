from __future__ import annotations

import itertools  # noqa
import re  # noqa
from collections import Counter, defaultdict, deque  # noqa

NUMPAD_A = """
123
456
789
"""


NUMPAD_B = """
  1
 234
56789
 ABC
  D
"""


DIRECTION_TO_MOVE = {"U": -1j, "R": 1, "D": 1j, "L": -1}


def parta(txt: str):
    return helper(txt, NUMPAD_A)


def partb(txt: str):
    return helper(txt, NUMPAD_B)


def helper(code: str, numpad: str):
    pos_to_char = get_pos_to_char(numpad)
    result = []
    pos = next(p for p, c in pos_to_char.items() if c == "5")
    for line in code.splitlines():
        for direction in line:
            new_pos = pos + DIRECTION_TO_MOVE[direction]
            if new_pos in pos_to_char:
                pos = new_pos
        result.append(pos_to_char.get(pos))
    return "".join(result)


def get_pos_to_char(numpad: str):
    return {
        complex(x, y): c
        for y, line in enumerate(numpad.strip("\n").splitlines())
        for x, c in enumerate(line)
        if c != " "
    }


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
