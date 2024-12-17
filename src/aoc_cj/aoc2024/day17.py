import contextlib
import dataclasses
import enum
import itertools
from collections.abc import Generator

import more_itertools as mi

from aoc_cj import util


class OperandType(enum.Enum):
    LITERAL = enum.auto()
    COMBO = enum.auto()


class Opcode(enum.IntEnum):
    adv = 0
    bxl = 1
    bst = 2
    jnz = 3
    bxc = 4
    out = 5
    bdv = 6
    cdv = 7


@dataclasses.dataclass(kw_only=True, slots=True)
class Computer:
    a: int
    b: int
    c: int
    program: tuple[int, ...]

    @staticmethod
    def parse(txt: str) -> "Computer":
        registers, program = txt.split("\n\n")
        a, b, c = (mi.one(util.ints(l)) for l in registers.splitlines())
        return Computer(a=a, b=b, c=c, program=tuple(util.ints(program)))

    def _combo_operand(self, val: int) -> int:
        match val:
            case 0 | 1 | 2 | 3:
                return val
            case 4:
                return self.a
            case 5:
                return self.b
            case 6:
                return self.c
        assert False, "unreachable"

    def run(self) -> Generator[int, None, None]:
        ip = 0
        with contextlib.suppress(IndexError):
            while ip < len(self.program):
                opcode = Opcode(self.program[ip])
                operand = self.program[ip + 1]
                next_ip = ip + 2
                match opcode:
                    case Opcode.adv:
                        self.a = self.div(operand)
                    case Opcode.bxl:
                        self.b ^= operand
                    case Opcode.bst:
                        self.b = self._combo_operand(operand) % 8
                    case Opcode.jnz:
                        if self.a != 0:
                            next_ip = operand
                    case Opcode.bxc:
                        self.b ^= self.c
                    case Opcode.out:
                        yield self._combo_operand(operand) % 8
                    case Opcode.bdv:
                        self.b = self.div(operand)
                    case Opcode.cdv:
                        self.c = self.div(operand)
                ip = next_ip

    def div(self, operand: int) -> int:
        numerator = self.a
        combo_op = self._combo_operand(operand)
        denominator = int(2**combo_op)
        return numerator // denominator


def part_1(txt: str) -> str:
    computer = Computer.parse(txt)
    return ",".join(map(str, computer.run()))


def part_2(txt: str) -> int | None:
    # FIXME: DOES NOT WORK ON REAL INPUT. SIMULATION IS TOO SLOW. I LIKELY NEED TO ANALYZE THE PROGRAM.
    initial_computer = Computer.parse(txt)
    for i in itertools.count():
        computer = dataclasses.replace(initial_computer, a=i)
        with contextlib.suppress(ValueError):
            if all(a == b for a, b in zip(computer.program, computer.run(), strict=True)):
                return i
    assert False, "unreachable"


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
