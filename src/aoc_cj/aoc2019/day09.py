from aoc_cj.aoc2019.intcode_computer import IntcodeProgram


def part_1(txt: str):
    p = IntcodeProgram.parse(txt)
    p.write_input(1)
    p.run()
    assert len(p.outputs) == 1
    return p.outputs[0]


def part_2(txt: str):
    p = IntcodeProgram.parse(txt)
    p.write_input(2)
    p.run()
    assert len(p.outputs) == 1
    return p.outputs[0]


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
