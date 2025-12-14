from aoc_cj.aoc2018 import day16


def part_1(txt: str) -> int:
    ip, *lines = txt.splitlines()
    ip = int(ip[4:])
    instructions = tuple(map(day16.Instruction.parse_str, lines))

    registers: day16.Registers = (0, 0, 0, 0, 0, 0)

    while True:
        # cmd, a, b, c = (x if len(str(x)) == 4 else int(x) for x in lines[registers[ip]].split())
        instruction = instructions[registers[ip]]
        registers = day16.run_cmd(instruction.opcode, registers, instruction)
        if registers[ip] == 28:
            break
    return max(registers)


def part_2(txt: str) -> int:
    ip, *lines = txt.splitlines()
    ip = int(ip[4:])

    cmds = [[x if len(str(x)) == 4 else int(x) for x in line.split()] for line in lines]
    instructions = tuple(map(day16.Instruction.parse_str, txt.splitlines()))
    print(instructions)

    seen = set()
    last = None
    registers = [0, 0, 0, 0, 0, 0]
    while registers[ip] >= 0 and registers[ip] < len(lines):
        cmd, a, b, c = cmds[registers[ip]]
        day16.run_cmd(cmd, registers, a, b, c)
        if registers[ip] == 28:
            m = max(registers)
            if m in seen:
                assert last is not None
                return last
            seen.add(m)
            last = m
        registers[ip] += 1
    raise AssertionError("unreachable")


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")  # SLOWWWWWW. (a few minutes, with pypy)
