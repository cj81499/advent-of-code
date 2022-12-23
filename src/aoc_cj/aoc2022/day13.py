import ast
import enum
from collections.abc import Sequence
from functools import cmp_to_key
from typing import Union

L = Union[int, Sequence["L"]]


class CompareResult(enum.Enum):
    CORRECT = enum.auto()
    EQ = enum.auto()
    INCORRECT = enum.auto()


def compare(left: L, right: L) -> CompareResult:
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return CompareResult.CORRECT
        elif left > right:
            return CompareResult.INCORRECT
        return CompareResult.EQ
    elif not isinstance(left, int) and not isinstance(right, int):
        for l, r in zip(left, right):
            if (compare_result := compare(l, r)) != CompareResult.EQ:
                return compare_result
        if len(left) < len(right):
            return CompareResult.CORRECT
        elif len(left) > len(right):
            return CompareResult.INCORRECT
        return CompareResult.EQ
    elif isinstance(left, int) and not isinstance(right, int):
        return compare([left], right)
    elif isinstance(right, int) and not isinstance(left, int):
        return compare(left, [right])
    assert False, "unreachable"


def parta(txt: str) -> int:
    pairs = txt.split("\n\n")

    count = 0
    for i, (left_s, right_s) in enumerate((l.splitlines() for l in pairs), start=1):
        left: L = ast.literal_eval(left_s)
        right: L = ast.literal_eval(right_s)

        if compare(left, right) in (CompareResult.CORRECT, CompareResult.EQ):
            count += i

    return count


def cmpb(left: L, right: L) -> int:
    return {
        CompareResult.CORRECT: -1,
        CompareResult.EQ: 0,
        CompareResult.INCORRECT: 1,
    }[compare(left, right)]


def partb(txt: str) -> int:
    sep1 = [[2]]
    sep2 = [[6]]
    packets: list[L] = [sep1, sep2, *(ast.literal_eval(line) for line in txt.splitlines() if line != "")]

    packets.sort(key=cmp_to_key(cmpb))

    from more_itertools import pairwise

    for a, b in pairwise(packets):
        assert compare(a, b) == CompareResult.CORRECT

    sep1_i = packets.index(sep1) + 1
    sep2_i = packets.index(sep2) + 1

    return sep1_i * sep2_i


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
