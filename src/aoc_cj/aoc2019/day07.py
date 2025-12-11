import itertools

from aoc_cj.aoc2019.intcode_computer import IntcodeProgram


def part_1(txt: str):
    m = 0
    for phase_setting_seq in itertools.permutations(range(5)):
        amplifiers = [IntcodeProgram.parse(txt) for _ in range(5)]
        prev = 0
        for a, n in zip(amplifiers, phase_setting_seq, strict=True):
            a.write_input(n)
            a.write_input(prev)
            a.run()
            prev = a.outputs[0]
        m = max(m, prev)
    return m


def part_2(txt: str):
    m = 0
    for phase_setting_seq in itertools.permutations(range(5, 10)):
        amplifiers = [IntcodeProgram.parse(txt) for _ in range(5)]
        for a, n in zip(amplifiers, phase_setting_seq, strict=True):
            a.write_input(n)
        prev = 0
        while not amplifiers[-1].terminated:
            for a in amplifiers:
                a.write_input(prev)
                a.run()
                prev = a.outputs[-1]
        m = max(m, prev)
    return m


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
