def parse_instructions(txt):
    instructions = txt.splitlines()
    instructions = [x.split() for x in instructions]
    return [(cmd, int(n)) for cmd, n in instructions]


def simulate(instructions, stop_on_loop=False, loop_limit=None):
    loops = 0
    accumulator = 0
    ip = 0
    seen = set()
    while loop_limit is None or loops < loop_limit and ip < len(instructions):
        if stop_on_loop and ip in seen:
            return accumulator
        seen.add(ip)
        cmd, n = instructions[ip]
        if cmd == "acc":
            accumulator += n
            ip += 1
        elif cmd == "jmp":
            ip += n
        elif cmd == "nop":
            ip += 1
        loops += 1
    return accumulator if (loop_limit is None or loops < loop_limit) else None


def parta(txt):
    instructions = parse_instructions(txt)
    return simulate(instructions, True)


def partb(txt):
    instructions = parse_instructions(txt)
    for i, (cmd, n) in enumerate(instructions):
        if cmd in ("jmp", "nop"):
            new_cmd = "jmp" if cmd == "nop" else "nop"
            instructions_copy = [x for x in instructions]
            instructions_copy[i] = (new_cmd, n)
            res = simulate(instructions_copy, loop_limit=10000)
            if res is not None:
                return res
    return -1


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
