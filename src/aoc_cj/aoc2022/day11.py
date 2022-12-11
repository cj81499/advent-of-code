import dataclasses
import math
import re
from collections import Counter, deque
from heapq import nlargest
from typing import Callable, Literal


def prime_factors(n: int) -> Counter[int]:
    pfs: Counter[int] = Counter()

    while n % 2 == 0:
        pfs[2] += 1
        n = n // 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i and divide n
        while n % i == 0:
            pfs[i] += 1
            n //= i

    if n > 2:
        pfs[n] += 1

    return Counter(pfs)


@dataclasses.dataclass
class Monkey:
    items: deque[int]
    operation: Callable[[int], int]  # TODO: comment
    test: int  # TODO: comment
    true_monkey: int  # TODO: comment
    false_monkey: int  # TODO: comment
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

    def turn(self, monkeys: list["Monkey"], part: Literal[1, 2] = 1, relieve_by: int = 3) -> None:
        while self.items:
            item = self.items.popleft()

            # inspect
            item = self.operation(item)
            self.inspect_count += 1

            # relief
            if part == 1:
                item //= relieve_by
            else:
                assert part == 2
                # "find another way to keep your worry levels manageable"
                # https://www.reddit.com/r/adventofcode/comments/zih7gf/comment/izrck61/

                # relieve by taking modulus of product of all "divisibility test values"
                item %= relieve_by

            # test worry level
            if item % self.test == 0:
                throw_to = self.true_monkey
            else:
                throw_to = self.false_monkey

            # throw
            monkeys[throw_to].items.append(item)


def parta(txt: str) -> int:
    monkeys = [Monkey.parse(m) for m in txt.split("\n\n")]

    # round
    for round in range(1, 20 + 1):
        for i, monkey in enumerate(monkeys):
            monkey.turn(monkeys)

    a, b = nlargest(2, monkeys, key=lambda m: m.inspect_count)
    return a.inspect_count * b.inspect_count


def partb(txt: str) -> int:
    monkeys = [Monkey.parse(m) for m in txt.split("\n\n")]

    test_vals = [m.test for m in monkeys]

    def is_prime(n: int) -> bool:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        return True

    assert all(is_prime(n) for n in test_vals)

    be_relieved_by = math.prod(test_vals)

    # round
    for round in range(1, 10_000 + 1):
        for i, monkey in enumerate(monkeys):
            monkey.turn(monkeys, part=2, relieve_by=be_relieved_by)

    a, b = nlargest(2, monkeys, key=lambda m: m.inspect_count)
    return a.inspect_count * b.inspect_count


def main(txt: str) -> None:
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
