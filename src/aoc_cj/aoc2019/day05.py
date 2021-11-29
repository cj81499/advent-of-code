from aoc_cj.aoc2019.intcode_computer import IntcodeProgram


def parta(txt: str):
    p = IntcodeProgram.parse(txt)
    p.write_input(1)
    p.run()
    assert all(n == 0 for n in [*p.outputs][:-1])
    return p.outputs[-1]


def partb(txt: str):
    p = IntcodeProgram.parse(txt)
    p.write_input(5)
    p.run()
    assert len(p.outputs) == 1
    return p.outputs[0]


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
