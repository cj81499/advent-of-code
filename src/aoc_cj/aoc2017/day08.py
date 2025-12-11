import operator
from collections import defaultdict

COMPARISONS = {
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne,
}


def perform_cmd(registers, cmd) -> None:
    reg, mode, amount, _, lhs, op, rhs = cmd.split()
    if COMPARISONS[op](registers[lhs], int(rhs)):
        amount = int(amount)
        registers[reg] += amount if mode == "inc" else -amount


def part_1(txt: str):
    registers = defaultdict(int)
    for cmd in txt.splitlines():
        perform_cmd(registers, cmd)
    return max(registers.values())


def part_2(txt: str):
    registers = defaultdict(int)
    all_time_max = 0
    for cmd in txt.splitlines():
        perform_cmd(registers, cmd)
        all_time_max = max(all_time_max, *registers.values())
    return all_time_max


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
