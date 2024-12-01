import itertools
from collections.abc import Generator, Iterable, Iterator

from typing_extensions import override


class Rock:
    def __init__(self, points: Iterable[complex]) -> None:
        self._points = set(points)

        self.rightmost_x = int(max(p.real for p in self._points))
        self.leftmost_x = int(min(p.real for p in self._points))

        self.highest_y = int(max(p.imag for p in self._points))
        self.lowest_y = int(min(p.imag for p in self._points))

    @override
    def __str__(self) -> str:
        return "\n".join(
            "".join(
                "#" if complex(x, y) in self._points else "."
                for x in range(
                    self.leftmost_x,
                    self.rightmost_x + 1,
                )
            )
            for y in reversed(
                range(
                    self.lowest_y,
                    self.highest_y + 1,
                )
            )
        )

    def points(self, offset: complex = 0) -> Generator[complex, None, None]:
        yield from (p + offset for p in self._points)

    @staticmethod
    def parse(rock: str) -> "Rock":
        return Rock(
            complex(x, y) for y, line in enumerate(reversed(rock.splitlines())) for x, c in enumerate(line) if c == "#"
        )


_ROCKS_STR = """
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
"""

ROCKS = [Rock.parse(r) for r in _ROCKS_STR.strip().split("\n\n")]


class Chamber:
    WIDTH = 7

    def __init__(self) -> None:
        self._landed_rocks: set[complex] = set()
        self.highest_rock_y = 0

    def drop(self, rock: Rock, jet_pattern: Iterator[str]) -> None:
        # left edge is two units away from the left wall.
        # bottom edge is three units above the highest rock in the room
        # (or the floor, if there isn't one).
        rock_bottom_left = complex(2, self.highest_rock_y + 4)

        while True:
            # move based off of jet pattern
            j = next(jet_pattern)
            move = {"<": -1, ">": 1}[j]
            if self.can_move_rock_bottom_left_to(rock, rock_bottom_left + move):
                rock_bottom_left += move

            # move down
            if self.can_move_rock_bottom_left_to(rock, rock_bottom_left - 1j):
                rock_bottom_left -= 1j
            else:
                break

        for p in rock.points(rock_bottom_left):
            self._landed_rocks.add(p)
            self.highest_rock_y = max(self.highest_rock_y, int(p.imag))

    def can_move_rock_bottom_left_to(self, rock: Rock, rock_bottom_left: complex) -> bool:
        for p in rock.points(rock_bottom_left):
            if not (0 <= p.real < Chamber.WIDTH):
                return False
            if p.imag <= 0:
                return False
            if p in self._landed_rocks:
                return False
        return True


def part_1(txt: str, *, rounds: int = 2022) -> int:
    chamber = Chamber()
    jet_pattern = itertools.cycle(txt)
    for _rock_i, rock in zip(range(rounds), itertools.cycle(ROCKS)):
        chamber.drop(rock, jet_pattern)

    return chamber.highest_rock_y


def part_2(txt: str) -> None:
    return None


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")  # type: ignore[func-returns-value]
