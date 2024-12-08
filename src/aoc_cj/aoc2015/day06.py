import dataclasses
import enum
import re
from collections import Counter, defaultdict
from typing import override


class Action(enum.Enum):
    TURN_ON = "turn on"
    TURN_OFF = "turn off"
    TOGGLE = "toggle"


ON = True
OFF = False


@dataclasses.dataclass(frozen=True)
class Instruction:
    action: Action
    start: tuple[int, int]
    end: tuple[int, int]

    _PARSE_REGEX = re.compile(r"(.*) (\d+),(\d+) through (\d+),(\d+)")

    @staticmethod
    def parse(instruction: str) -> "Instruction":
        match = Instruction._PARSE_REGEX.match(instruction)
        if not match:
            raise ValueError("invalid instruction")
        action, start_x, start_y, end_x, end_y = match.groups()
        return Instruction(Action(action), (int(start_x), int(start_y)), (int(end_x), int(end_y)))

    @override
    def __repr__(self) -> str:
        return f"{self.action} {self.start}-{self.end}"


def part_1(txt: str) -> int:
    instructions = [Instruction.parse(line) for line in txt.splitlines()]
    grid = defaultdict(bool)
    for instruction in instructions:
        for x in range(instruction.start[0], instruction.end[0] + 1):
            for y in range(instruction.start[1], instruction.end[1] + 1):
                if instruction.action is Action.TURN_ON:
                    grid[(x, y)] = ON
                elif instruction.action is Action.TURN_OFF:
                    grid[(x, y)] = OFF
                elif instruction.action is Action.TOGGLE:
                    grid[(x, y)] = not grid[(x, y)]
                else:
                    raise Exception("unknown action")

    return sum(grid[(x, y)] for x in range(1000) for y in range(1000))


def part_2(txt: str) -> int:
    instructions = [Instruction.parse(line) for line in txt.splitlines()]
    grid = Counter[tuple[int, int]]()
    for instruction in instructions:
        for x in range(instruction.start[0], instruction.end[0] + 1):
            for y in range(instruction.start[1], instruction.end[1] + 1):
                if instruction.action is Action.TURN_ON:
                    grid[(x, y)] += 1
                elif instruction.action is Action.TURN_OFF:
                    grid[(x, y)] = max(0, grid[(x, y)] - 1)
                elif instruction.action is Action.TOGGLE:
                    grid[(x, y)] += 2
                else:
                    raise Exception("unknown action")

    return sum(grid[(x, y)] for x in range(1000) for y in range(1000))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
