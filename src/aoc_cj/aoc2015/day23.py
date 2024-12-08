def simulate(txt: str, a: int = 0) -> dict[str, int]:
    registers = {"a": a, "b": 0}
    instructions = [line.split() for line in txt.splitlines()]

    ip = 0
    while ip < len(instructions):
        ins = instructions[ip]
        op = ins[0]
        if op == "hlf":
            registers[ins[1]] //= 2
        elif op == "tpl":
            registers[ins[1]] *= 3
        elif op == "inc":
            registers[ins[1]] += 1
        elif op == "jmp":
            # subtract 1 from jmp opcodes b/c we always increment ip by 1 at the end
            ip += int(ins[1]) - 1
        elif op == "jie":
            if registers[ins[1].strip(",")] % 2 == 0:
                ip += int(ins[2]) - 1
        elif op == "jio":
            if registers[ins[1].strip(",")] == 1:
                ip += int(ins[2]) - 1
        else:
            raise Exception("unknown opcode")
        ip += 1
    return registers


def part_1(txt: str) -> int:
    return simulate(txt)["b"]


def part_2(txt: str) -> int:
    return simulate(txt, a=1)["b"]


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
