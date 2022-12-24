import dataclasses
from typing import Any, Callable, Generic, TypeVar

from aoc_cj import util

Registers = tuple[int, ...]
Operation = Callable[[Registers, int, int], int]

_T = TypeVar("_T")


OPERATIONS: dict[str, Operation] = {
    "addr": lambda r, a, b: r[a] + r[b],
    "addi": lambda r, a, b: r[a] + b,
    "mulr": lambda r, a, b: r[a] * r[b],
    "muli": lambda r, a, b: r[a] * b,
    "banr": lambda r, a, b: r[a] & r[b],
    "bani": lambda r, a, b: r[a] & b,
    "borr": lambda r, a, b: r[a] | r[b],
    "bori": lambda r, a, b: r[a] | b,
    "setr": lambda r, a, b: r[a],
    "seti": lambda r, a, b: a,
    "gtir": lambda r, a, b: 1 if a > r[b] else 0,
    "gtri": lambda r, a, b: 1 if r[a] > b else 0,
    "gtrr": lambda r, a, b: 1 if r[a] > r[b] else 0,
    "eqir": lambda r, a, b: 1 if a == r[b] else 0,
    "eqri": lambda r, a, b: 1 if r[a] == b else 0,
    "eqrr": lambda r, a, b: 1 if r[a] == r[b] else 0,
}


@dataclasses.dataclass
class Sample:
    before: Registers
    instruction: "Instruction[int]"
    after: Registers

    @staticmethod
    def parse(sample: str) -> "Sample":
        before, instruction, after = sample.splitlines()
        before_ints = tuple(util.ints(before))
        after_ints = tuple(util.ints(after))
        return Sample(before_ints, Instruction.parse(instruction), after_ints)

    def behaves_like(self) -> set[str]:
        return {cmd for cmd in OPERATIONS if run_cmd(cmd, self.before, self.instruction) == self.after}


@dataclasses.dataclass
class Instruction(Generic[_T]):
    opcode: _T
    a: int
    b: int
    c: int

    @staticmethod
    def parse(instruction: str) -> "Instruction[int]":
        # opcode, *abc_strs = instruction.split()
        # abc = map(int, abc_strs)
        return Instruction(*util.ints(instruction))

    @staticmethod
    def parse_str(instruction: str) -> "Instruction[str]":
        opcode, *abc_strs = instruction.split()
        abc = map(int, abc_strs)
        return Instruction(opcode, *abc)


def update_registers(r: Registers, i: int, new_val: int) -> Registers:
    return r[:i] + (new_val,) + r[i + 1 :]


def run_cmd(opcode_name: str, registers: Registers, instruction: Instruction[Any]) -> Registers:
    a, b, c = instruction.a, instruction.b, instruction.c
    return update_registers(registers, c, OPERATIONS[opcode_name](registers, a, b))


def parta(txt: str) -> int:
    samples_s, _instructions_s = txt.split("\n\n\n\n")
    samples = [Sample.parse(s) for s in samples_s.split("\n\n")]
    return sum(1 for s in samples if len(s.behaves_like()) >= 3)


def partb(txt: str) -> int:
    samples_s, instructions_s = txt.split("\n\n\n\n")
    samples = [Sample.parse(s) for s in samples_s.split("\n\n")]
    instructions = [Instruction.parse(l) for l in instructions_s.splitlines()]

    # solve opcodes
    solved_opcodes = solve_opcodes(samples)

    # execute instructions
    registers: Registers = (0, 0, 0, 0)
    for instruction in instructions:
        registers = run_cmd(solved_opcodes[instruction.opcode], registers, instruction)
    return registers[0]


def solve_opcodes(samples: list[Sample]) -> dict[int, str]:
    unsolved_opcodes = {i: set(OPERATIONS) for i in range(len(OPERATIONS))}

    for sample in samples:
        unsolved_opcodes[sample.instruction.opcode] &= sample.behaves_like()

    solved_opcodes: dict[int, str] = {}
    while unsolved_opcodes:
        newly_solved = {i: opcodes.pop() for i, opcodes in unsolved_opcodes.items() if len(opcodes) == 1}
        solved_opcodes |= newly_solved
        unsolved_opcodes = {
            k: {v for v in vals if v not in solved_opcodes.values()}
            for k, vals in unsolved_opcodes.items()
            if k not in solved_opcodes
        }

    return solved_opcodes


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
