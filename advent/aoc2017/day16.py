from __future__ import annotations

import itertools  # noqa
import re  # noqa
from collections import Counter, defaultdict, deque  # noqa

ONE_BILLION = 1_000_000_000


class Programs:
    def __init__(self, num_programs):
        self._programs = [chr(ord("a") + i) for i in range(num_programs)]

    def spin(self, n: int):
        self._programs = [*self._programs[-n:], *self._programs[:-n]]

    def exchange(self, a: int, b: int):
        self._programs[a], self._programs[b] = self._programs[b], self._programs[a]

    def partner(self, a: str, b: str):
        a_i = self._programs.index(a)
        b_i = self._programs.index(b)
        self.exchange(a_i, b_i)

    def __str__(self):
        return "".join(self._programs)

    def dance(self, moves, repetitions=1):
        seen = {}
        for i in range(repetitions):
            if str(self) in seen:
                loop_size = i - seen[str(self)]
                remaining = repetitions % loop_size
                for s, n in seen.items():
                    if n == remaining:
                        self._programs = [*s]
                        return
            seen[str(self)] = i

            for move in moves:
                move_type = move[0]
                if move_type == "s":
                    self.spin(int(move[1:]))
                elif move_type == "x":
                    self.exchange(*map(int, move[1:].split("/")))
                elif move_type == "p":
                    self.partner(move[1], move[3])
                else:
                    raise Exception("unknown move")


def parta(txt: str, num_programs=16, repetitions=1):
    p = Programs(num_programs)
    p.dance(txt.split(","), repetitions)
    return str(p)


def partb(txt: str):
    return parta(txt, repetitions=ONE_BILLION)


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
