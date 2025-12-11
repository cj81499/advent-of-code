import ast
import enum
import functools
import itertools
from collections.abc import Sequence

L = int | Sequence["L"]


class CompareResult(enum.Enum):
    CORRECT = enum.auto()
    EQ = enum.auto()
    INCORRECT = enum.auto()


def compare(left: L, right: L) -> CompareResult:
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return CompareResult.CORRECT
        if left > right:
            return CompareResult.INCORRECT
        return CompareResult.EQ
    if not isinstance(left, int) and not isinstance(right, int):
        for l, r in zip(left, right, strict=False):
            if (compare_result := compare(l, r)) != CompareResult.EQ:
                return compare_result
        if len(left) < len(right):
            return CompareResult.CORRECT
        if len(left) > len(right):
            return CompareResult.INCORRECT
        return CompareResult.EQ
    if isinstance(left, int) and not isinstance(right, int):
        return compare([left], right)
    if isinstance(right, int) and not isinstance(left, int):
        return compare(left, [right])
    msg = "unreachable"
    raise AssertionError(msg)


def part_1(txt: str) -> int:
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


def part_2(txt: str) -> int:
    sep1 = [[2]]
    sep2 = [[6]]
    packets: list[L] = [sep1, sep2, *(ast.literal_eval(line) for line in txt.splitlines() if line != "")]

    packets.sort(key=functools.cmp_to_key(cmpb))

    for a, b in itertools.pairwise(packets):
        assert compare(a, b) == CompareResult.CORRECT

    sep1_i = packets.index(sep1) + 1
    sep2_i = packets.index(sep2) + 1

    return sep1_i * sep2_i


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
