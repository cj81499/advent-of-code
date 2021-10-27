from __future__ import annotations

from collections import defaultdict, deque


class RcvException(Exception):
    def __init__(self, last_sent) -> None:
        super().__init__()
        self.last_sent = last_sent


class Program:
    def __init__(self, instructions):
        self._instructions = instructions
        self._ip = 0
        self._registers = defaultdict(int)
        self._last_sent = 0

    def _val(self, arg):
        return self._registers[arg] if arg.isalpha() else int(arg)

    def snd(self):
        assert len(self._args) == 1
        self._last_sent = self._val(self._args[0])

    def set(self):
        x, y = self._args
        self._registers[x] = self._val(y)

    def add(self):
        x, y = self._args
        self._registers[x] += self._val(y)

    def mul(self):
        x, y = self._args
        self._registers[x] *= self._val(y)

    def mod(self):
        x, y = self._args
        self._registers[x] %= self._val(y)

    def rcv(self):
        assert len(self._args) == 1
        if self._val(self._args[0]) != 0:
            raise RcvException(self._last_sent)

    def jgz(self):
        x, y = self._args
        if self._val(x) > 0:
            self._ip += self._val(y) - 1

    def perform_instruction(self):
        cmd, *self._args = self.current_instruction
        getattr(self, cmd)()
        self._ip += 1

    @property
    def current_instruction(self):
        return self._instructions[self._ip]


class ProgramB(Program):
    def __init__(self, instructions, pid):
        super().__init__(instructions)
        self._registers["p"] = pid
        self._q = deque()
        self.send_count = 0

    def snd(self):
        assert len(self._args) == 1
        self._reciever._q.append(self._val(self._args[0]))
        self.send_count += 1

    def rcv(self):
        assert len(self._args) == 1
        # if we can't recieve, don't do anything.
        if self.is_waiting():
            self._ip -= 1  # subtract 1 from ip so we don't advance the program
            return
        self._registers[self._args[0]] = self._q.popleft()

    def set_reciever(self, reciever):
        self._reciever = reciever

    def is_waiting(self):
        return self.current_instruction[0] == "rcv" and len(self._q) == 0


def val(registers, a):
    return registers[a] if a.isalpha() else int(a)


def parta(txt: str):
    instructions = [line.split() for line in txt.splitlines()]
    p = Program(instructions)
    try:
        while True:
            p.perform_instruction()
    except RcvException as e:
        return e.last_sent


def partb(txt: str):
    instructions = [line.split() for line in txt.splitlines()]
    p0 = ProgramB(instructions, 0)
    p1 = ProgramB(instructions, 1)
    p0.set_reciever(p1)
    p1.set_reciever(p0)
    while not (p0.is_waiting() and p1.is_waiting()):
        p0.perform_instruction()
        p1.perform_instruction()
    return p1.send_count


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
