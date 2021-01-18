from __future__ import annotations

import itertools  # noqa
import re  # noqa
from collections import Counter, defaultdict, deque  # noqa

from advent.aoc2019.intcode_computer import IntcodeProgram


def parta(txt: str):
    m = 0
    for phase_setting_seq in itertools.permutations(range(5)):
        amplifiers = [IntcodeProgram.parse(txt) for _ in range(5)]
        prev = 0
        for a, n in zip(amplifiers, phase_setting_seq):
            a.write_input(n)
            a.write_input(prev)
            output = []
            a.set_output(output.append)
            a.run()
            prev = output[0]
        m = max(m, prev)
    return m


def partb(txt: str):
    m = 0
    for phase_setting_seq in itertools.permutations(range(5, 10)):
        amplifiers = [IntcodeProgram.parse(txt) for _ in range(5)]
        for a, n in zip(amplifiers, phase_setting_seq):
            a.write_input(n)
        prev = 0
        while not amplifiers[-1].terminated:
            for a in amplifiers:
                a.write_input(prev)
                output = deque()
                a.set_output(output.append)
                a.run()
                prev = output.popleft()
        m = max(m, prev)
    return m


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
