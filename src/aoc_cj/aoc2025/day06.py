import dataclasses
import enum
import math
from collections.abc import Generator, Iterable, Sequence
from typing import assert_never


class Operator(enum.StrEnum):
    PLUS = "+"
    MULTIPLY = "*"

    def compute(self, numbers: Iterable[int]) -> int:
        if self == Operator.PLUS:
            return sum(numbers)
        if self == Operator.MULTIPLY:
            return math.prod(numbers)
        assert_never(self)


def transpose[T](it: Iterable[Iterable[T]]) -> Iterable[tuple[T]]:
    return zip(*it, strict=True)


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class Problem:
    rows: Sequence[str]
    op: Operator

    def solve_1(self) -> int:
        return self.op.compute(map(int, self.rows))

    def solve_2(self) -> int:
        return self.op.compute(int("".join(col)) for col in zip(*self.rows, strict=True))


def parse_problems(txt: str) -> Generator[Problem]:
    lines = txt.splitlines()
    start = 0
    op = "unknown"
    for i, column in enumerate(transpose(lines)):
        if column[-1] != " ":
            op = column[-1]
        elif all(c == " " for c in column):
            yield Problem(rows=[l[start:i] for l in lines[:-1]], op=Operator(op))
            start = i + 1
    yield Problem(rows=[l[start:] for l in lines[:-1]], op=Operator(op))


def part_1(txt: str) -> int:
    return sum(map(Problem.solve_1, parse_problems(txt)))


def part_2(txt: str) -> int:
    return sum(map(Problem.solve_2, parse_problems(txt)))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
