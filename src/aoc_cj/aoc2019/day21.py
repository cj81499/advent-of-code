from aoc_cj.aoc2019.intcode_computer import IntcodeProgram


def run_springscript(intcode, instructions):
    p = IntcodeProgram.parse(intcode)

    for i in instructions:
        for c in i:
            p.write_input(ord(c))
        p.write_input(ord("\n"))

    p.run()
    return p.outputs[-1]


def part_1(txt: str):
    # J = D ^ !(A ^ B ^ C)

    # D means the bot will land the jump
    # !(A ^ B ^ C) means one or more of A,B,C is empty
    instructions = [
        "OR A J",
        "AND B J",
        "AND C J",  # J = A ^ B ^ C
        "NOT J J",  # J = !(A ^ B ^ C)
        "AND D J",  # J = D ^ !(A ^ B ^ C)
        "WALK",  # go!
    ]
    return run_springscript(txt, instructions)


def part_2(txt: str):
    # J = D ^ !(A ^ B ^ C) ^ (H v E)

    # D means the bot will land the jump
    # !(A ^ B ^ C) means one or more of A,B,C is empty
    # H v E means we have somewhere to go after landing

    instructions = [
        "OR A J",
        "AND B J",
        "AND C J",  # J = A ^ B ^ C
        "NOT J J",  # J = !(A ^ B ^ C)
        "AND D J",  # J = D ^ !(A ^ B ^ C)
        "OR E T",
        "OR H T",  # T = H OR E
        "AND T J",  # J = D ^ !(A ^ B ^ C) ^ (H v E)
        "RUN",  # go!
    ]
    return run_springscript(txt, instructions)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
