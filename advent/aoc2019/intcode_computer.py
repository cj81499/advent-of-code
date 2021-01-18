import itertools
from collections import deque
from typing import Callable, List


class UnknownOpcodeException(Exception):
    pass


class ProgramTerminatedException(Exception):
    pass


class IntcodeProgram:
    def __init__(self, program: List[int]):
        self._memory = program
        self._ip = 0
        self.terminated = False
        self._input_queue = deque()

    def write_input(self, n: int):
        self._input_queue.append(n)

    def set_output(self, f: Callable[[int], None]):
        self._write_output = f

    @staticmethod
    def parse(program: str):
        return IntcodeProgram([*map(int, program.split(","))])

    def run(self, max_steps=None):  # max_steps is useful for debugging infinite loops
        steps = itertools.count()
        while not self.terminated and not self.is_waiting_for_input():
            if max_steps is not None and next(steps) > max_steps:
                raise Exception("too many steps")
            self.run_next()

    def run_next(self):  # noqa: C901
        if self.terminated:
            raise ProgramTerminatedException()
        if self.is_waiting_for_input():
            return
        op = self.opcode
        if op == 1:
            self._add()
        elif op == 2:
            self._multiply()
        elif op == 3:
            self._input()
        elif op == 4:
            self._output()
        elif op == 5:
            self._jump_if_true()
        elif op == 6:
            self._jump_if_false()
        elif op == 7:
            self._less_than()
        elif op == 8:
            self._equals()
        elif op == 99:
            self._halt()
        else:
            raise UnknownOpcodeException()

    def is_waiting_for_input(self):
        return self.opcode == 3 and len(self._input_queue) == 0

    @property
    def opcode(self):
        return self[self._ip] % 100

    def _parameters(self, n: int):
        return [self._parameter(i) for i in range(1, n + 1)]

    def _parameter(self, n: int):
        i = self._ip + n
        return self[i] if self._parameter_mode(n) == 0 else i

    def _parameter_mode(self, n: int):
        return self[self._ip] // 10**(n+1) % 10

    def _add(self):
        p1, p2, p3 = self._parameters(3)
        self[p3] = self[p1] + self[p2]
        self._ip += 4

    def _multiply(self):
        p1, p2, p3 = self._parameters(3)
        self[p3] = self[p1] * self[p2]
        self._ip += 4

    def _input(self):
        self[self._parameter(1)] = self._input_queue.popleft()
        self._ip += 2

    def _output(self):
        self._write_output(self[self._parameter(1)])
        self._ip += 2

    def _jump_if_true(self):
        p1, p2 = self._parameters(2)
        if self[p1] != 0:
            self._ip = self[p2]
        else:
            self._ip += 3

    def _jump_if_false(self):
        p1, p2 = self._parameters(2)
        if self[p1] == 0:
            self._ip = self[p2]
        else:
            self._ip += 3

    def _less_than(self):
        p1, p2, p3 = self._parameters(3)
        self[p3] = 1 if self[p1] < self[p2] else 0
        self._ip += 4

    def _equals(self):
        p1, p2, p3 = self._parameters(3)
        self[p3] = 1 if self[p1] == self[p2] else 0
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
