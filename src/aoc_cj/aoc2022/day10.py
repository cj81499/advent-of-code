import dataclasses
import enum
from collections import deque
from typing import Optional

from typing_extensions import assert_never


class Opcode(enum.Enum):
    NOOP = enum.auto()
    ADDX = enum.auto()

    def duration(self) -> int:
        if self is Opcode.NOOP:
            return 1
        if self is Opcode.ADDX:
            return 2
        assert_never(self)

    def apply(self, x: int, args: list[int]) -> int:
        if self is Opcode.NOOP:
            return x
        if self is Opcode.ADDX:
            return x + args[0]
        assert_never(self)


@dataclasses.dataclass
class Instruction:
    opcode: Opcode
    args: list[int]

    @staticmethod
    def parse(instruction: str) -> "Instruction":
        opcode, *args = instruction.split()
        return Instruction(Opcode[opcode.upper()], [int(n) for n in args])

    def execute(self, x: int) -> int:
        return self.opcode.apply(x, self.args)


class Computer:
    def __init__(self, instructions: list[Instruction]) -> None:
        self._instructions = deque(instructions)
        self.x = 1
        self._running: Optional[tuple[Instruction, int]] = None

    def cycle(self) -> int:
        # start of cycle
        if self._running is None and self._instructions:
            to_run = self._instructions.popleft()
            self._running = (to_run, to_run.opcode.duration())

        # during cycle
        x = self.x

        # after the cycle
        if self._running is not None:
            instruction, duration = self._running
            duration -= 1

            if duration == 0:
                self.x = instruction.execute(x)

            self._running = None if duration == 0 else (instruction, duration)

        return x


def parta(txt: str) -> int:
    instructions = [Instruction.parse(line) for line in txt.splitlines()]
    computer = Computer(instructions)

    signal_strength_sum = 0
    for cycle in range(1, 220 + 1):
        result = computer.cycle()
        if (cycle - 20) % 40 == 0:
            signal_strength_sum += cycle * result

    return signal_strength_sum


def partb(txt: str) -> str:
    instructions = [Instruction.parse(line) for line in txt.splitlines()]
    computer = Computer(instructions)

    chars = []
    # crt has 6 rows and 40 cols
    for row_idx in range(6):
        for col_idx in range(40):
            is_lit = abs(col_idx - computer.cycle()) < 2
            chars.append("#" if is_lit else ".")
        chars.append("\n")

    return "".join(chars)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb:\n{partb(data)}")
