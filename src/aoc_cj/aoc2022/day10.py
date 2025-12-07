import dataclasses

r"""
I refactored my original solution expecting this "computer" to be reused
(since that's been the case in previous years).

Unfortunately for me, it was not reused.

¯\_(ツ)_/¯
"""

from collections.abc import Callable, Iterable
from typing import ClassVar


@dataclasses.dataclass
class Opcode:
    duration: int
    apply: Callable[[int, list[int]], int]

    OPCODES: ClassVar[dict[str, "Opcode"]] = {}

    @staticmethod
    def parse(opcode: str) -> "Opcode":
        return Opcode.OPCODES[opcode]


Opcode.OPCODES = {
    "noop": Opcode(1, lambda x, args: x),
    "addx": Opcode(2, lambda x, args: x + args[0]),
}


@dataclasses.dataclass
class Instruction:
    opcode: Opcode
    args: list[int]

    @staticmethod
    def parse(instruction: str) -> "Instruction":
        opcode, *args = instruction.split()
        return Instruction(Opcode.parse(opcode), [int(n) for n in args])

    def execute(self, x: int) -> int:
        return self.opcode.apply(x, self.args)


class Computer:
    def __init__(self, instructions: Iterable[Instruction]) -> None:
        self._instructions = list(instructions)
        self._instruction_pointer = 0
        self.x = 1
        self._running: tuple[Instruction, int] | None = None
        self.cycle_number = 0

    def cycle(self) -> int:
        # start of cycle
        if self._running is None and self._instruction_pointer < len(self._instructions):
            to_run = self._instructions[self._instruction_pointer]
            self._instruction_pointer += 1
            self._running = (to_run, self.cycle_number)

        # during cycle
        self.cycle_number += 1
        x = self.x

        # after the cycle
        if self._running is not None:
            instruction, started_at = self._running

            if self.cycle_number - started_at == instruction.opcode.duration:
                self.x = instruction.execute(x)
                self._running = None

        return x


def part_1(txt: str) -> int:
    computer = Computer(Instruction.parse(line) for line in txt.splitlines())

    signal_strength_sum = 0
    while computer.cycle_number <= 240:
        result = computer.cycle()
        if (computer.cycle_number - 20) % 40 == 0:
            signal_strength_sum += computer.cycle_number * result

    return signal_strength_sum


def part_2(txt: str) -> str:
    computer = Computer(Instruction.parse(line) for line in txt.splitlines())

    chars = []
    # crt has 6 rows and 40 cols
    for _row_idx in range(6):
        for col_idx in range(40):
            is_lit = abs(col_idx - computer.cycle()) < 2
            chars.append("#" if is_lit else ".")
        chars.append("\n")

    return "".join(chars).strip()


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
