import itertools
from typing import List


class UnknownOpcodeException(Exception):
    pass


class ProgramTerminatedException(Exception):
    pass


class IntcodeProgram:
    def __init__(self, program: List[int]):
        self._memory = program
        self._ip = 0
        self.terminated = False

    @staticmethod
    def parse(program: str):
        return IntcodeProgram([*map(int, program.split(","))])

    def run(self, max_steps=None):  # max_steps is useful for debugging infinite loops
        steps = itertools.count()
        while not self.terminated:
            if max_steps is not None and next(steps) > max_steps:
                raise Exception("too many steps")
            self.run_next()

    def run_next(self):
        if self.terminated:
            raise ProgramTerminatedException()
        op = self.opcode
        if op == 1:
            self._add()
        elif op == 2:
            self._multiply()
        elif op == 99:
            self._halt()
        else:
            raise UnknownOpcodeException()

    @property
    def opcode(self):
        return self[self._ip]

    def _parameters(self, n: int):
        return self[self._ip + 1: self._ip+1+n]

    def _add(self):
        p1, p2, p3 = self._parameters(3)
        self[p3] = self[p1] + self[p2]
        self._ip += 4

    def _multiply(self):
        p1, p2, p3 = self._parameters(3)
        self[p3] = self[p1] * self[p2]
        self._ip += 4

    def _halt(self):
        self.terminated = True
        # self._ip += 1

    def __getitem__(self, item: int):
        return self._memory[item]

    def __setitem__(self, idx: int, item: int):
        self._memory[idx] = item

    @property
    def state(self):
        return [*self._memory]
