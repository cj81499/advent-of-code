from itertools import combinations
from typing import List

from aocd import data

from intcode_interpreter import run_intcode_program


def parta(txt: str) -> int:
    memory = [int(x) for x in txt.split(",")]
    # work with a copy of memory to avoid side effects
    memory = memory.copy()
    memory[1] = 12
    memory[2] = 2
    return run_intcode_program(memory)[0]


def partb(txt: str) -> int:
    memory = [int(x) for x in txt.split(",")]
    GOAL = 19690720
    # work with a copy of memory to avoid side effects
    memory = memory.copy()
    for noun, verb in combinations(range(0, 100), 2):
        memory[1], memory[2] = noun, verb
        if run_intcode_program(memory)[0] == GOAL:
            return 100 * noun + verb
    return -1


def main() -> None:
    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")


if __name__ == "__main__":
    main()
