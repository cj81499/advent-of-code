from __future__ import annotations

from aoc_cj.aoc2019.intcode_computer import IntcodeProgram


def parta(txt: str):
    p = IntcodeProgram.parse(txt)
    p.write_input(1)
    p.run()
    assert len(p.outputs) == 1
    return p.outputs[0]


def partb(txt: str):
    p = IntcodeProgram.parse(txt)
    p.write_input(2)
    p.run()
    assert len(p.outputs) == 1
    return p.outputs[0]


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
