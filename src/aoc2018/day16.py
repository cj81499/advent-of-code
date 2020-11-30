CMDS = set(["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr",
            "eqir", "eqri", "eqrr"])

OPERATIONS = {
    "addr": lambda r, a, b: r[a] + r[b],
    "addi": lambda r, a, b: r[a] + b,
    "mulr": lambda r, a, b: r[a] * r[b],
    "muli": lambda r, a, b: r[a] * b,
    "banr": lambda r, a, b: r[a] & r[b],
    "bani": lambda r, a, b: r[a] & b,
    "borr": lambda r, a, b: r[a] | r[b],
    "bori": lambda r, a, b: r[a] | b,
    "setr": lambda r, a, b: r[a],
    "seti": lambda r, a, b: a,
    "gtir": lambda r, a, b: 1 if a > r[b] else 0,
    "gtri": lambda r, a, b: 1 if r[a] > b else 0,
    "gtrr": lambda r, a, b: 1 if r[a] > r[b] else 0,
    "eqir": lambda r, a, b: 1 if a == r[b] else 0,
    "eqri": lambda r, a, b: 1 if r[a] == b else 0,
    "eqrr": lambda r, a, b: 1 if r[a] == r[b] else 0
}


def run_cmd(name, registers, a, b, c):
    registers[c] = OPERATIONS[name](registers, a, b)


def part1(samples):
    samples = samples.split("\n\n")
    sample_count = 0
    for s in samples:
        lines = s.split("\n")
        before = list(map(int, lines[0][9:-1].split(", ")))
        _, a, b, c = list(map(int, lines[1].split(" ")))
        after = list(map(int, lines[2][9:-1].split(", ")))

        acts_like_count = 0
        for cmd in CMDS:
            r = before.copy()
            run_cmd(cmd, r, a, b, c)
            if r == after:
                acts_like_count += 1
        if acts_like_count >= 3:
            sample_count += 1

    return sample_count


def opcodes_solved(opcodes):
    for code in opcodes:
        if isinstance(opcodes[code], set):
            return False
    return True


def part2(samples, program):
    opcodes = {i: CMDS.copy() for i in range(16)}
    samples = samples.split("\n\n")
    for s in samples:
        lines = s.split("\n")
        before = list(map(int, lines[0][9:-1].split(", ")))
        cmd_num, a, b, c = list(map(int, lines[1].split(" ")))
        after = list(map(int, lines[2][9:-1].split(", ")))
        for cmd in CMDS:
            if cmd in opcodes[cmd_num]:
                r = before.copy()
                run_cmd(cmd, r, a, b, c)
                if r != after:
                    opcodes[cmd_num].remove(cmd)
    solved = set()
    while not opcodes_solved(opcodes):
        for code in opcodes:
            if isinstance(opcodes[code], set) and len(opcodes[code]) == 1:
                opcodes[code] = opcodes[code].pop()
            if isinstance(opcodes[code], str):
                solved.add(opcodes[code])
            else:
                opcodes[code] = opcodes[code] - solved

    registers = [0, 0, 0, 0]
    program = program.splitlines()
    for cmd in program:
        cmd_num, a, b, c = [int(x) for x in cmd.split()]
        # cmd_num, a, b, c = [int(x) for x in cmd.strip().split(" ")]
        # _, a, b, c = list(map(int, cmd.split(" ")))

        run_cmd(opcodes[cmd_num], registers, a, b, c)
    return registers[0]


def main():
    input_txt, _ = helpers.load_input(16, "Chronal Classification")

    sections = input_txt.split("\n\n\n\n")

    print(f"part1: {part1(sections[0])}")
    print(f"part2: {part2(sections[0], sections[1])}")


if __name__ == "__main__":
    import helpers
    main()
