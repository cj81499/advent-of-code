from collections import defaultdict
from operator import eq, ge, gt, le, lt, ne

COMPARISONS = {">": gt, "<": lt, ">=": ge, "<=": le, "==": eq, "!=": ne}


def perform_cmd(registers, cmd):
    reg, mode, amount, _, lhs, op, rhs = cmd.split()
    if COMPARISONS[op](registers[lhs], int(rhs)):
        amount = int(amount)
        registers[reg] += amount if mode == "inc" else -amount


def parta(txt: str):
    registers = defaultdict(lambda: 0)
    for cmd in txt.splitlines():
        perform_cmd(registers, cmd)
    return max(registers.values())


def partb(txt: str):
    registers = defaultdict(lambda: 0)
    all_time_max = 0
    for cmd in txt.splitlines():
        perform_cmd(registers, cmd)
        all_time_max = max(all_time_max, *registers.values())
    return all_time_max


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
