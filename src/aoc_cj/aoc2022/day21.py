import abc
import enum
from typing import Callable, Optional, Union

from typing_extensions import override

IntFn = Callable[[int, int], int]

Monkeys = dict[str, Union[int, tuple[str, str, str]]]

ROOT = "root"
HUMN = "humn"


class Side(enum.Enum):
    LEFT = enum.auto()
    RIGHT = enum.auto()


class Operation(enum.Enum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"

    def apply(self, left: int, right: int) -> int:
        return {
            Operation.ADD: left + right,
            Operation.SUBTRACT: left - right,
            Operation.MULTIPLY: left * right,
            Operation.DIVIDE: left // right,
        }[self]

    def opposite(self) -> "Operation":
        return {
            Operation.ADD: Operation.SUBTRACT,
            Operation.SUBTRACT: Operation.ADD,
            Operation.MULTIPLY: Operation.DIVIDE,
            Operation.DIVIDE: Operation.MULTIPLY,
        }[self]

    def reverse(self, result: int, value: int, value_on: Side) -> int:
        if value_on is Side.LEFT and self is Operation.SUBTRACT:
            return -result + value
        return self.opposite().apply(result, value)


class Monkey(abc.ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abc.abstractmethod
    def evaluate(self, monkeys: dict[str, "Monkey"]) -> int:
        pass

    @staticmethod
    def parse(monkey: str) -> "Monkey":
        name, value_s = monkey.split(": ")
        if value_s.isnumeric():
            return IntMonkey(name, int(value_s))
        left, op, right = value_s.split()
        return UnresolvedMonkey(name, left, Operation(op), right)

    @abc.abstractmethod
    def contains(self, name: str, monkeys: dict[str, "Monkey"]) -> bool:
        pass

    @abc.abstractmethod
    def _solve_humn(self, monkeys: dict[str, "Monkey"], target: int) -> int:
        pass


class IntMonkey(Monkey):
    def __init__(self, name: str, value: int) -> None:
        super().__init__(name)
        self.value = value

    @override
    def evaluate(self, _monkeys: dict[str, Monkey]) -> int:
        return self.value

    @override
    def contains(self, name: str, monkeys: dict[str, Monkey]) -> bool:
        return self.name == name

    @override
    def _solve_humn(self, monkeys: dict[str, Monkey], target: int) -> int:
        assert self.name == HUMN
        return target


class UnresolvedMonkey(Monkey):
    def __init__(self, name: str, left: str, op: Operation, right: str) -> None:
        super().__init__(name)

        self.left = left
        self.op = op
        self.right = right

        self._resolved: Optional[ResolvedMonkey] = None

    @override
    def evaluate(self, monkeys: dict[str, Monkey]) -> int:
        return self._resolve(monkeys).evaluate(monkeys)

    @override
    def contains(self, name: str, monkeys: dict[str, Monkey]) -> bool:
        return self._resolve(monkeys).contains(name, monkeys)

    def solve_humn(self, monkeys: dict[str, Monkey]) -> int:
        assert self.name == ROOT
        # either left or right must contain HUMN
        resolved = self._resolve(monkeys)
        assert (left_contains_humn := resolved.left.contains(HUMN, monkeys)) ^ resolved.right.contains(HUMN, monkeys)
        monkey_containing_humn, monkey_not_containing_humn = (
            (resolved.left, resolved.right) if left_contains_humn else (resolved.right, resolved.left)
        )
        # we know the value of monkey that doesn't contain HUMN
        known_value = monkey_not_containing_humn.evaluate(monkeys)
        # if this is the root monkey, we don't have a target value yet.
        return monkey_containing_humn._solve_humn(monkeys, target=known_value)

    @override
    def _solve_humn(self, monkeys: dict[str, Monkey], target: int) -> int:
        return self._resolve(monkeys)._solve_humn(monkeys, target)

    def _resolve(self, monkeys: dict[str, Monkey]) -> "ResolvedMonkey":
        if self._resolved is None:
            self._resolved = ResolvedMonkey(self.name, monkeys[self.left], self.op, monkeys[self.right])
        return self._resolved


class ResolvedMonkey(Monkey):
    def __init__(self, name: str, left: Monkey, op: Operation, right: Monkey) -> None:
        super().__init__(name)

        self.left = left
        self.op = op
        self.right = right

        self._contains_humn: Optional[bool] = None

    @override
    def evaluate(self, monkeys: dict[str, Monkey]) -> int:
        return self.op.apply(self.left.evaluate(monkeys), self.right.evaluate(monkeys))

    @override
    def contains(self, name: str, monkeys: dict[str, Monkey]) -> bool:
        if self._contains_humn is None:
            self._contains_humn = self.left.contains(name, monkeys) or self.right.contains(name, monkeys)
        return self._contains_humn

    @override
    def _solve_humn(self, monkeys: dict[str, Monkey], target: int) -> int:
        # either left or right must contain HUMN
        assert (left_contains_humn := self.left.contains(HUMN, monkeys)) ^ self.right.contains(HUMN, monkeys)
        monkey_containing_humn, monkey_not_containing_humn, known_value_side = (
            (self.left, self.right, Side.RIGHT) if left_contains_humn else (self.right, self.left, Side.LEFT)
        )
        # we know the value of monkey that doesn't contain HUMN
        known_value = monkey_not_containing_humn.evaluate(monkeys)
        unknown_value = self.op.reverse(target, known_value, known_value_side)
        return monkey_containing_humn._solve_humn(monkeys, target=unknown_value)


def part_1(txt: str) -> int:
    monkeys = {m.name: m for m in (Monkey.parse(l) for l in txt.splitlines())}
    return monkeys[ROOT].evaluate(monkeys)


def part_2(txt: str) -> int:
    monkeys = {m.name: m for m in (Monkey.parse(l) for l in txt.splitlines())}
    root_monkey = monkeys[ROOT]
    assert isinstance(root_monkey, UnresolvedMonkey)
    return root_monkey.solve_humn(monkeys)


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
