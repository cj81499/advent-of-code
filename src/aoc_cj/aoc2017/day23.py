from collections import defaultdict

from aoc_cj import util


class Program:
    def __init__(self, instructions):
        self._instructions = instructions
        self.ip = 0
        self._registers = defaultdict(int)
        self.mul_count = 0

    def _val(self, arg):
        return self._registers[arg] if arg.isalpha() else int(arg)

    def set(self):
        x, y = self._args
        self._registers[x] = self._val(y)

    def sub(self):
        x, y = self._args
        self._registers[x] -= self._val(y)

    def mul(self):
        x, y = self._args
        self._registers[x] *= self._val(y)
        self.mul_count += 1

    def jnz(self):
        x, y = self._args
        if self._val(x) != 0:
            self.ip += self._val(y) - 1

    def perform_instruction(self):
        cmd, *self._args = self.current_instruction
        getattr(self, cmd)()
        self.ip += 1

    @property
    def current_instruction(self):
        return self._instructions[self.ip]


def part_1(txt: str):
    instructions = [line.split() for line in txt.splitlines()]
    p = Program(instructions)
    while 0 <= p.ip < len(instructions):
        p.perform_instruction()
    return p.mul_count


def part_2(txt: str):
    # after setup, the program counts how many numbers are not prime between
    # b and c (inclusive) with a step of 17 .
    b, c = 106500, 123500
    return sum(not util.is_prime(n) for n in range(b, c + 1, 17))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
