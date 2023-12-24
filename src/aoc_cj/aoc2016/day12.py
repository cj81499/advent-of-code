from collections import defaultdict


class AssemBunnyComputer:
    def __init__(self, instructions: str):
        self._registers = defaultdict(int)
        self.pc = 0  # program counter
        self._program = [i.split() for i in instructions.splitlines()]

    @property
    def current_instruction(self):
        return self._program[self.pc]

    def run(self):
        while self.pc in range(len(self._program)):
            instruction, *args = self.current_instruction
            getattr(self, instruction)(*args)
            self.pc += 1

    def arg(self, x):
        try:
            return int(x)
        except ValueError:
            assert x.isalpha()
            return self._registers[x]

    def cpy(self, x, y):
        self._registers[y] = self.arg(x)

    def inc(self, x):
        self._registers[x] += 1

    def dec(self, x):
        self._registers[x] -= 1

    def jnz(self, x, y):
        if self.arg(x) != 0:
            self.pc += self.arg(y) - 1

    def __getitem__(self, item: str):
        return self._registers[item]

    def __setitem__(self, item: str, value: int):
        self._registers[item] = value


def part_1(txt: str):
    c = AssemBunnyComputer(txt)
    c.run()
    return c["a"]

    return solve()


def part_2(txt: str):
    return solve(part_2=True)


def solve(part_2=False):
    # see day12.md
    a = 1
    b = 1
    d = 26

    if part_2:
        d += 7

    for _ in range(d):
        c = a
        a += b
        b = c

    a += 14 * 19
    return a


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
