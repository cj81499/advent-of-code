from datetime import date
from typing import List

import helpers


def run_intcode_program(nums: List[int]) -> List[int]:
    for i in range(0, len(nums), 4):
        opcode = nums[i]
        if opcode == 99:
            return nums

        if opcode not in (1, 2):
            raise AssertionError("Invalid opcode")

        pos_1 = nums[i + 1]
        pos_2 = nums[i + 2]
        pos_3 = nums[i + 3]

        if opcode == 1:
            nums[pos_3] = nums[pos_1] + nums[pos_2]
        elif opcode == 2:
            nums[pos_3] = nums[pos_1] * nums[pos_2]


def part1(txt: str, lines: List[str]):
    nums = [int(x) for x in txt.split(",")]
    nums[1] = 12
    nums[2] = 2
    return run_intcode_program(nums)[0]


def part2(txt: str, lines: List[str]):
    goal = 19690720
    for noun in range(0, 100):
        for verb in range(0, 100):
            nums = [int(x) for x in txt.split(",")]
            nums[1] = noun
            nums[2] = verb
            if run_intcode_program(nums)[0] == goal:
                return 100 * noun + verb


def main():
    txt, lines = helpers.get_puzzle(date(2019, 12, 2), "1202 Program Alarm")

    print(f"part1: {part1(txt, lines)}")
    print(f"part2: {part2(txt, lines)}")


if __name__ == "__main__":
    main()
