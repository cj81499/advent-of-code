import operator
from typing import Callable, Union

IntFn = Callable[[int, int], int]

Monkeys = dict[str, Union[int, tuple[str, str, str]]]

OPS: dict[str, IntFn] = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
}


def evaluate(monkeys: Monkeys, name: str = "root") -> int:
    monkey = monkeys[name]
    if isinstance(monkey, int):
        return monkey

    l, op, r = monkey
    return OPS[op](evaluate(monkeys, l), evaluate(monkeys, r))


def parta(txt: str) -> int:
    monkeys = parse(txt)

    return evaluate(monkeys)


def parse(txt: str) -> Monkeys:
    monkeys: Monkeys = {}

    for l in txt.splitlines():
        name, job = l.split(": ")

        if job.isnumeric():
            monkeys[name] = int(job)
        else:
            l, op_s, r = job.split()
            monkeys[name] = (l, op_s, r)

    return monkeys


def contains(monkeys: Monkeys, search: str, name: str) -> bool:
    if search == name:
        return True

    monkey = monkeys[name]
    if isinstance(monkey, int):
        return False

    l, _op, r = monkey

    return contains(monkeys, search, l) or contains(monkeys, search, r)


def humn_value_for_target(monkeys: Monkeys, name: str, target: int) -> int:
    if name == "humn":
        return target

    monkey = monkeys[name]
    assert not isinstance(monkey, int)
    l, op, r = monkey
    if contains(monkeys, "humn", l):
        r_value = evaluate(monkeys, r)
        if op == "-":
            # reverse_result - r_value = target
            reverse_result = target + r_value
        elif op == "+":
            # reverse_result + r_value = target
            reverse_result = target - r_value
        elif op == "*":
            # reverse_result * r_value = target
            reverse_result = target // r_value
        elif op == "/":
            # reverse_result / r_value = target
            reverse_result = target * r_value
        else:
            assert False, "unreachable"
        actual = OPS[op](reverse_result, r_value)
        assert actual == target

        return humn_value_for_target(monkeys, l, reverse_result)
    else:
        assert contains(monkeys, "humn", r)
        l_value = evaluate(monkeys, l)
        if op == "-":
            # l_value - reverse_result = target
            reverse_result = l_value - target
        elif op == "+":
            # l_value + reverse_result = target
            reverse_result = target - l_value
        elif op == "*":
            # l_value * reverse_result = target
            reverse_result = target // l_value
        elif op == "/":
            # l_value / reverse_result = target
            reverse_result = target * l_value
        else:
            assert False, "unreachable"
        actual = OPS[op](l_value, reverse_result)
        assert actual == target

        return humn_value_for_target(monkeys, r, reverse_result)


def partb(txt: str) -> int:
    monkeys = parse(txt)

    root_monkey = monkeys["root"]

    assert not isinstance(root_monkey, int)
    assert isinstance(monkeys["humn"], int)

    l, op, r = root_monkey
    if contains(monkeys, "humn", l):
        target_value = evaluate(monkeys, r)
        result = humn_value_for_target(monkeys, l, target_value)

        monkeys["humn"] = result
        assert evaluate(monkeys, l) == target_value

        return result

    assert contains(monkeys, "humn", r)
    target_value = evaluate(monkeys, l)
    result = humn_value_for_target(monkeys, r, target_value)

    monkeys["humn"] = result
    assert evaluate(monkeys, r) == target_value

    return result


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
