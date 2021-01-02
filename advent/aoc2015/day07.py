from collections import deque
from typing import Deque


def is_int(s: str):
    try:
        int(s)
        return True
    except:  # noqa
        return False


class Instruction():
    BIT_MASK = 0b1111111111111111

    def __init__(self, instruction_str: str):
        self._instruction_str = instruction_str
        source, self.destination = instruction_str.split(" -> ")
        self.source_info = source.split()

    def can_execute(self, wires: dict):
        if len(self.source_info) == 1:
            return is_int(self.source_info[0]) or self.source_info[0] in wires

        elif len(self.source_info) == 2:
            _, source = self.source_info
            return source in wires

        elif len(self.source_info) == 3:
            source_1, _, source_2 = self.source_info

            source_1_good = is_int(source_1) or source_1 in wires
            source_2_good = is_int(source_2) or source_2 in wires

            return source_1_good and source_2_good

        return False

    def execute(self, wires):  # noqa
        assert self.can_execute(wires)
        if len(self.source_info) == 1:
            if is_int(self.source_info[0]):
                wires[self.destination] = int(
                    self.source_info[0]) & Instruction.BIT_MASK
            else:
                wires[self.destination] = wires[self.source_info[0]
                                                ] & Instruction.BIT_MASK
        elif len(self.source_info) == 2:
            mode, source = self.source_info
            if not is_int(source):
                source = wires[source]
            if mode == "NOT":
                wires[self.destination] = ~ int(source) & Instruction.BIT_MASK
            else:
                print(mode)

        elif len(self.source_info) == 3:
            source_1, mode, source_2 = self.source_info
            if not is_int(source_1):
                source_1 = wires[source_1]
            if not is_int(source_2):
                source_2 = wires[source_2]
            if mode == "RSHIFT":
                wires[self.destination] = int(source_1) >> int(
                    source_2) & Instruction.BIT_MASK
            elif mode == "LSHIFT":
                wires[self.destination] = int(source_1) << int(
                    source_2) & Instruction.BIT_MASK
            elif mode == "AND":
                wires[self.destination] = int(source_1) & int(
                    source_2) & Instruction.BIT_MASK
            elif mode == "OR":
                wires[self.destination] = int(source_1) | int(
                    source_2) & Instruction.BIT_MASK
            else:
                print(mode)

    def __repr__(self):
        return self._instruction_str


def build_instructions_deque(txt, partb=False) -> Deque[Instruction]:
    instructions: Deque[Instruction] = deque()

    for instruction in txt.splitlines():
        i = Instruction(instruction)
        if not partb or i.destination != "b":
            instructions.append(i)

    return instructions


def run(instructions: Deque[Instruction], wires: dict):
    while instructions:
        i: Instruction = instructions.popleft()
        if i.can_execute(wires):
            i.execute(wires)
        else:
            instructions.append(i)


def parta(txt):
    wires = {}
    run(build_instructions_deque(txt), wires)
    return wires["a"]


def partb(txt):
    wires = {"b": parta(txt)}
    run(build_instructions_deque(txt, partb=True), wires)
    return wires["a"]


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
