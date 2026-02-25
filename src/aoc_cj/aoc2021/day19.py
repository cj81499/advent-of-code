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


# import enum
# import itertools

# Beacon = tuple[int, int, int]


# class Order(enum.Enum):
#     XYZ = enum.auto()
#     XZY = enum.auto()
#     YXZ = enum.auto()
#     YZX = enum.auto()
#     ZXY = enum.auto()
#     ZYX = enum.auto()


# class Sign(enum.Enum):
#     POSITIVE = enum.auto()
#     NEGATIVE = enum.auto()


# class Scan:
#     def __init__(self, n: int, beacons: list[Beacon]) -> None:
#         self.n = n
#         self.beacons = list(beacons)

#     @staticmethod
#     def parse(txt: str) -> "Scan":
#         lines = iter(txt.splitlines())
#         n = int(next(lines).strip("- scanner"))
#         splits = (map(int, l.split(",")) for l in lines)
#         beacons = ((a, b, c) for a, b, c in splits)
#         return Scan(n, beacons)

#     def __repr__(self) -> str:
#         return f"Scan(n={self.n}, beacons={self.beacons})"


# def parta(txt: str) -> None:
#     scans = list(map(Scan.parse, txt.split("\n\n")))
#     for s in scans:
#         print(s)
#         print()

#     # flips/transforms
#     # TODO: this isn't right. you can get orientations that aren't possible.
#     for a, b, c in itertools.permutations("xyz", 3):
#         for sign_a, sign_b, sign_c in itertools.product("+-", repeat=3):
#             print(f"{sign_a}{a}, {sign_b}{b}, {sign_c}{c}")

#     for order in Order:
#         for sign1, sign2, sign3 in itertools.product(Sign, repeat=3):
#             print(order, sign1, sign2, sign3)

#     return None


def partb(txt: str) -> None:
    return None


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
