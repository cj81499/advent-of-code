import itertools

from aoc_cj.aoc2019.intcode_computer import IntcodeProgram


def parta(txt: str):
    p = IntcodeProgram.parse(txt)
    p[1] = 12
    p[2] = 2
    p.run()
    return p[0]


def partb(txt: str):
    for noun, verb in itertools.product(range(0, 100), repeat=2):
        p = IntcodeProgram.parse(txt)
        p[1] = noun
        p[2] = verb
        p.run()
        if p[0] == 19690720:
            return 100 * noun + verb


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
