from aoc_cj.aoc2019.intcode_computer import IntcodeProgram


def run_springscript(intcode, instructions):
    p = IntcodeProgram.parse(intcode)

    for i in instructions:
        for c in i:
            p.write_input(ord(c))
        p.write_input(ord("\n"))

    p.run()
    # print("".join(chr(c) for c in [*p.outputs][:-1]))
    return p.outputs[-1]


def parta(txt: str):
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


def partb(txt: str):
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


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
