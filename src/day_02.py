from datetime import date
from itertools import combinations
from typing import List

from src.intcode_interpreter import run_intcode_program
from src.util.helpers import get_puzzle


def part1(memory: List[int]) -> int:
    # work with a copy of memory to avoid side effects
    memory = memory.copy()
    memory[1] = 12
    memory[2] = 2
    return run_intcode_program(memory)[0]


def part2(memory: List[int]) -> int:
    GOAL = 19690720
    # work with a copy of memory to avoid side effects
    memory = memory.copy()
    for noun, verb in combinations(range(0, 100), 2):
        memory[1], memory[2] = noun, verb
        if run_intcode_program(memory)[0] == GOAL:
            return 100 * noun + verb
    return -1


def main() -> None:
    txt, _ = get_puzzle(date(2019, 12, 2), "1202 Program Alarm")

    nums = [int(x) for x in txt.split(",")]

    print(f"part1: {part1(nums)}")
    print(f"part2: {part2(nums)}")


if __name__ == "__main__":
    main()
