import dataclasses
import itertools
import re
from collections import Counter
from collections.abc import Iterator

from aoc_cj import util

PATTERN = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")
Point = tuple[int, int]


@dataclasses.dataclass
class Line:
    start_x: int
    start_y: int
    end_x: int
    end_y: int

    @staticmethod
    def parse(txt: str) -> "Line":
        match = PATTERN.match(txt)
        assert match is not None
        return Line(*map(int, match.groups()))

    def __iter__(self) -> Iterator[Point]:
        p = (self.start_x, self.start_y)
        dx = util.clamp(self.end_x - self.start_x, -1, 1)
        dy = util.clamp(self.end_y - self.start_y, -1, 1)
        while p != (self.end_x, self.end_y):
            yield p
            p = (p[0] + dx, p[1] + dy)
        yield p

    def is_horizontal(self) -> bool:
        return self.start_y == self.end_y

    def is_vertical(self) -> bool:
        return self.start_x == self.end_x


def parta(txt: str) -> int:
    lines = map(Line.parse, txt.splitlines())
    counts = Counter(itertools.chain(*(iter(l) for l in lines if l.is_horizontal() or l.is_vertical())))
    return sum(n >= 2 for n in counts.values())


def partb(txt: str) -> int:
    lines = map(Line.parse, txt.splitlines())
    counts = Counter(itertools.chain(*(iter(l) for l in lines)))
    return sum(n >= 2 for n in counts.values())


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
