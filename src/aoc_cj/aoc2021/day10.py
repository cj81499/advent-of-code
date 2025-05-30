import enum
import functools
import statistics
from typing import NamedTuple

PAIRS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

CORRUPT_POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

INCOMPLETE_POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


class LineStatus(enum.Enum):
    CORRUPTED = enum.auto()
    INCOMPLETE = enum.auto()


class HelperResponse(NamedTuple):
    line_status: LineStatus
    first_illegal: str
    unclosed: list[str]


def part_1(txt: str) -> int:
    return sum(map(score_for_line, txt.splitlines()))


def score_for_line(line: str) -> int:
    status, c, _unclosed = process_line(line)
    return CORRUPT_POINTS[c] if status is LineStatus.CORRUPTED else 0


def process_line(line: str) -> HelperResponse:
    unclosed: list[str] = []
    for c in line:
        if c in PAIRS:
            unclosed.append(c)
        elif c != PAIRS[unclosed.pop()]:
            return HelperResponse(LineStatus.CORRUPTED, c, unclosed)
    return HelperResponse(LineStatus.INCOMPLETE, "", unclosed)


def part_2(txt: str) -> int:
    scores = [
        autocomplete_score(unclosed)
        for status, _c, unclosed in map(process_line, txt.splitlines())
        if status is LineStatus.INCOMPLETE
    ]

    assert len(scores) % 2 != 0  # assert odd number of scores
    med = statistics.median_low(scores)  # get median
    return int(med)


def autocomplete_score(unclosed: list[str]) -> int:
    closing_chars = (PAIRS[c] for c in reversed(unclosed))
    return functools.reduce(lambda acc, c: 5 * acc + INCOMPLETE_POINTS[c], closing_chars, 0)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
