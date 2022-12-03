from collections import defaultdict


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


def parta(txt: str):
    instructions = [line.split() for line in txt.splitlines()]
    p = Program(instructions)
    while 0 <= p.ip < len(instructions):
        p.perform_instruction()
    return p.mul_count


def is_prime(n):
    # A positive integer that is greater than 1 and is not divisible without
    # a remainder by any positive integer other than itself and 1.
    return n > 1 and n % 1 == 0 and not any(n % i == 0 for i in range(2, (n // 2) + 1))


def partb(txt: str):
    # after setup, the program counts how many numbers are not prime between
    # b and c (inclusive) with a step of 17 .
    b, c = 106500, 123500
    return sum(not is_prime(n) for n in range(b, c + 1, 17))


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
