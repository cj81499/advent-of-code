from __future__ import annotations

from advent.aoc2019.intcode_computer import IntcodeProgram


def parta(txt: str):
    p = IntcodeProgram.parse(txt)
    p.write_input(1)
    outputs = []
    p.set_output(outputs.append)
    p.run()
    assert all(n == 0 for n in outputs[:-1])
    return outputs[-1]


def partb(txt: str):
    p = IntcodeProgram.parse(txt)
    p.write_input(5)
    outputs = []
    p.set_output(outputs.append)
    p.run()
    assert len(outputs) == 1
    return outputs[0]


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
