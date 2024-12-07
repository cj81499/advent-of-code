import math
from typing import Literal

from aoc_cj.aoc2018 import day16 as d


def factors(n: int) -> set[int]:
    results = set[int]()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            results.add(i)
            results.add(n // i)
    return results


def part_1(txt: str, *, part: Literal[1, 2] = 1) -> int:
    ip_s, *instructions_strs = txt.splitlines()
    ip = int(ip_s[4:])
    instructions = [d.Instruction.parse_str(line) for line in instructions_strs]

    registers: d.Registers = (0 if part == 1 else 1, 0, 0, 0, 0, 0)
    remaining = math.inf if part == 1 else 100
    # 100 times is enough to find the number the main loop will find the sum of the factors of
    while registers[ip] < len(instructions) and remaining > 0:
        instruction = instructions[registers[ip]]
        opcode = instruction.opcode
        registers = d.run_cmd(opcode, registers, instruction)
        registers = d.update_registers(registers, ip, registers[ip] + 1)
        remaining -= 1
    return registers[0] if part == 1 else sum(factors(max(registers)))


def part_2(txt: str) -> int:
    return part_1(txt, part=2)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
