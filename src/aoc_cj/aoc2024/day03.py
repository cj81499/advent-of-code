import math
import re

MUL_PATTERN = re.compile(r"mul\((\d+),(\d+)\)")
INSTRUCTION_PATTERN = re.compile(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)")


def part_1(txt: str) -> int:
    s = 0
    for match in MUL_PATTERN.findall(txt):
        s += math.prod(map(int, match))
    return s


def part_2(txt: str) -> int:
    s = 0
    enabled = True
    for match in INSTRUCTION_PATTERN.finditer(txt):
        m = match.group(0)
        if m == "do()":
            enabled = True
        elif m == "don't()":
            enabled = False
        else:
            if enabled:
                s += math.prod(map(int, match.groups()))
    return s


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
