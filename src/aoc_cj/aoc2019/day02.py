import itertools

from aoc_cj.aoc2019.intcode_computer import IntcodeProgram


def part_1(txt: str):
    p = IntcodeProgram.parse(txt)
    p[1] = 12
    p[2] = 2
    p.run()
    return p[0]


def part_2(txt: str):
    for noun, verb in itertools.product(range(0, 100), repeat=2):
        p = IntcodeProgram.parse(txt)
        p[1] = noun
        p[2] = verb
        p.run()
        if p[0] == 19690720:
            return 100 * noun + verb


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
