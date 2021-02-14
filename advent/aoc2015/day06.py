import dataclasses
import re
from collections import Counter, defaultdict
from enum import Enum
from typing import Tuple


class Action(Enum):
    TURN_ON = "turn on"
    TURN_OFF = "turn off"
    TOGGLE = "toggle"


ON = True
OFF = False


@dataclasses.dataclass(frozen=True)
class Instruction:
    action: Action
    start: Tuple[int, int]
    end: Tuple[int, int]

    _PARSE_REGEX = re.compile(r"(.*) (\d+),(\d+) through (\d+),(\d+)")

    @staticmethod
    def parse(instruction: str):
        action, start_x, start_y, end_x, end_y = Instruction._PARSE_REGEX.match(instruction).groups()
        return Instruction(Action(action), (int(start_x), int(start_y)), (int(end_x), int(end_y)))

    def __repr__(self):
        return f"{self.action} {self.start}-{self.end}"


def parta(txt):
    instructions = [Instruction.parse(line) for line in txt.splitlines()]
    grid = defaultdict(lambda: False)
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


def partb(txt):
    instructions = [Instruction.parse(line) for line in txt.splitlines()]
    grid = Counter()
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


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
