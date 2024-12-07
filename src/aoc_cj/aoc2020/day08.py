def parse_instructions(txt):
    instructions = txt.splitlines()
    instructions = [x.split() for x in instructions]
    return [(cmd, int(n)) for cmd, n in instructions]


def simulate(instructions, stop_on_loop=False):
    ip = 0
    accumulator = 0
    seen_ips = set()
    while ip < len(instructions):
        # if we've executed this instruction before
        if ip in seen_ips:
            # part a: we found the answer; part b: we're in a loop
            return accumulator if stop_on_loop else None
        seen_ips.add(ip)
        cmd, n = instructions[ip]
        if cmd == "acc":
            accumulator += n
            ip += 1
        elif cmd == "jmp":
            ip += n
        elif cmd == "nop":
            ip += 1
    return accumulator


def part_1(txt):
    instructions = parse_instructions(txt)
    return simulate(instructions, True)


def part_2(txt):
    instructions = parse_instructions(txt)
    for i, (cmd, n) in enumerate(instructions):
        if cmd in ("jmp", "nop"):
            new_cmd = "jmp" if cmd == "nop" else "nop"
            instructions_copy = instructions.copy()
            instructions_copy[i] = (new_cmd, n)
            if (res := simulate(instructions_copy)) is not None:
                return res
    return -1


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
