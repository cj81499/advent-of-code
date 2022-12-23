import dataclasses
import math
import re
from collections import deque
from heapq import nlargest
from typing import Callable

from aoc_cj import util


@dataclasses.dataclass
class Monkey:
    items: deque[int]
    operation: Callable[[int], int]
    test: int
    true_monkey: int
    false_monkey: int
    inspect_count = 0

    PARSE_REGEX = re.compile(
        r"Monkey (?P<number>\d+):\s+Starting items: (?P<items>.*)\s+Operation: new = (?P<operation>.*)\s+Test: divisible by (?P<test>\d*)\s+If true: throw to monkey (?P<true>\d*)\s+If false: throw to monkey (?P<false>\d*)"
    )

    @staticmethod
    def parse(monkey: str) -> "Monkey":
        match = Monkey.PARSE_REGEX.match(monkey)
        assert match is not None

        item, op, test, monkey_if_true, monkey_if_false = match.group("items", "operation", "test", "true", "false")
        lhs, op, rhs = op.split()

        def operation(old: int) -> int:
            val1 = old if lhs == "old" else int(lhs)
            val2 = old if rhs == "old" else int(rhs)

            if op == "+":
                return val1 + val2
            elif op == "*":
                return val1 * val2

            assert False, "unreachable"

        return Monkey(
            deque(int(n) for n in item.split(", ")),
            operation,
            int(test),
            int(monkey_if_true),
            int(monkey_if_false),
        )

    def turn(self, monkeys: list["Monkey"], relief_strategy: Callable[[int], int]) -> None:
        while self.items:
            item = self.items.popleft()

            # inspect
            item = self.operation(item)
            self.inspect_count += 1

            # relief
            item = relief_strategy(item)

            # test worry level
            if item % self.test == 0:
                throw_to = self.true_monkey
            else:
                throw_to = self.false_monkey

            # throw
            monkeys[throw_to].items.append(item)


def simulate(
    monkeys: list[Monkey],
    rounds: int = 20,
    relief_strategy: Callable[[int], int] = lambda n: n // 3,
) -> int:
    for _round in range(rounds):
        for m in monkeys:
            m.turn(monkeys, relief_strategy)

    return math.prod(nlargest(2, (m.inspect_count for m in monkeys)))


def parta(txt: str) -> int:
    monkeys = [Monkey.parse(m) for m in txt.split("\n\n")]
    return simulate(monkeys)


def partb(txt: str) -> int:
    monkeys = [Monkey.parse(m) for m in txt.split("\n\n")]

    test_vals = [m.test for m in monkeys]
    assert all(util.is_prime(n) for n in test_vals)
    be_relieved_by = math.prod(test_vals)

    # "find another way to keep your worry levels manageable"
    # https://www.reddit.com/r/adventofcode/comments/zih7gf/comment/izrck61/

    # relieve by taking modulus of product of all "divisibility test values"
    return simulate(monkeys, 10_000, lambda n: n % be_relieved_by)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
