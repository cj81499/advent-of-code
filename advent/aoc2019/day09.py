from __future__ import annotations

import itertools  # noqa
import re  # noqa
from collections import Counter, defaultdict, deque  # noqa

from advent.aoc2019.intcode_computer import IntcodeProgram


def parta(txt: str):
    p = IntcodeProgram.parse(txt)
    p.write_input(1)
    output = deque()
    p.set_output(output.append)
    p.run()
    assert len(output) == 1
    return output[0]


def partb(txt: str):
    p = IntcodeProgram.parse(txt)
    p.write_input(2)
    output = deque()
    p.set_output(output.append)
    p.run()
    assert len(output) == 1
    return output[0]


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
