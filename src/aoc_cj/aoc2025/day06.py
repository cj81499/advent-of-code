from math import prod

from aoc_cj import util


def part_1(txt: str) -> int:
    *rows, operators = txt.splitlines()
    rows = map(util.positive_ints, rows)
    operators = operators.split()
    columns: zip[tuple[int, ...]] = zip(*rows, strict=True)
    tot = 0
    for column, operator in zip(columns, operators, strict=True):
        if operator == "*":
            result = prod(column)
        elif operator == "+":
            result = sum(column)
        else:
            msg = f"unsupported operator: {operator}"
            raise AssertionError(msg)
        tot += result
    return tot


def part_2(txt: str) -> int:
    tot = 0
    columns: zip[tuple[str, ...]] = zip(*txt.splitlines(), strict=True)
    problem_numbers = []
    for c in reversed(tuple(columns)):
        *digits, op = c
        digits = "".join(digits).strip()
        if digits == "":
            continue  # problem separator line
        problem_numbers.append(int(digits))

        if op := op.strip():
            if op == "*":
                result = prod(problem_numbers)
            elif op == "+":
                result = sum(problem_numbers)
            else:
                msg = f"unsupported operator: {op}"
                raise AssertionError(msg)
            tot += result
            problem_numbers.clear()
    return tot


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
