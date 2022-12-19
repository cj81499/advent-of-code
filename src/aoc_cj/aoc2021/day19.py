import dataclasses
import string
from collections.abc import Iterable
from typing import Literal

REQUIRED_OVERLAP_COUNT = 12


Point = tuple[int, int, int]

Sign = Literal["+", "-"]
Direction = Literal["x", "y", "z"]
Heading = tuple[Sign, Direction]

ORIGIN: Point = (0, 0, 0)


@dataclasses.dataclass
class Placement:
    point: Point
    facing: Heading
    up: Heading


class Scanner:
    def __init__(self, num: int, points: Iterable[Point]) -> None:
        self._num = num
        self._points = list(points)

    def __str__(self) -> str:
        return "\n".join(
            (
                f"--- scanner {self._num} ---",
                *(",".join(map(str, p)) for p in self._points),
            )
        )

    @staticmethod
    def parse(scanner: str) -> "Scanner":
        title, *point_lines = scanner.splitlines()
        num = int(title.strip(string.ascii_letters + "- "))
        return Scanner(num, (Scanner.parse_point(p) for p in point_lines))

    @staticmethod
    def parse_point(point: str) -> Point:
        a, b, c = map(int, point.split(","))
        return a, b, c


def parta(txt: str) -> int:
    scanners = [Scanner.parse(s) for s in txt.split("\n\n")]

    placed_scanners: dict[int, Placement] = {0: Placement(ORIGIN, ("+", "x"), ("+", "y"))}

    # high level idea:
    #   assume that the fisrt scanner has correct orientation.
    #   "Build out" from the fisrt scanner by finding other scanners that
    #   overlap with it. Continue to "build out" from the scanners we find
    #   that overlap with the scanners we've already "connected".

    assert False, "unsolved"


def partb(txt: str) -> None:
    return None


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
