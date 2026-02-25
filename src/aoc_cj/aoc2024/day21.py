import dataclasses
import enum
import functools
import itertools
from collections.abc import Iterable
from typing import assert_never, override

import more_itertools as mi
from frozendict import frozendict

from aoc_cj import util

NUMERIC_BUTTON_ARRANGEMENT = frozendict[str, complex](
    {
        "7": 0 + 0j,
        "8": 1 + 0j,
        "9": 2 + 0j,
        "4": 0 + 1j,
        "5": 1 + 1j,
        "6": 2 + 1j,
        "1": 0 + 2j,
        "2": 1 + 2j,
        "3": 2 + 2j,
        "0": 1 + 3j,
        "A": 2 + 3j,
    }
)

DIRECTIONAL_BUTTON_ARRANGEMENT = frozendict[str, complex](
    {
        "^": 1 + 0j,
        "A": 2 + 0j,
        "<": 0 + 1j,
        "v": 1 + 1j,
        ">": 2 + 1j,
    }
)


class Direction(enum.Enum):
    UP = -1j
    DOWN = 1j
    LEFT = -1
    RIGHT = 1

    @override
    def __str__(self) -> str:
        if self is Direction.UP:
            return "^"
        if self is Direction.DOWN:
            return "v"
        if self is Direction.LEFT:
            return "<"
        if self is Direction.RIGHT:
            return ">"
        assert_never(self)


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class KeypadPressingRobot:
    keypad: frozendict[str, complex]

    @functools.lru_cache(maxsize=1)
    def _valid_positions(self) -> frozenset[complex]:
        return frozenset(self.keypad.values())

    def ways_to_press(self, seq: str) -> frozenset[str]:
        chunks: list[Iterable[str]] = []
        for start, end in itertools.pairwise(("A", *seq)):
            chunks.append(self.ways_to_get_between(start, end))
            chunks.append("A")
        return frozenset("".join(chosen) for chosen in itertools.product(*chunks))

    @functools.cache
    def ways_to_get_between(self, b1: str, b2: str) -> frozenset[str]:
        start = self.keypad[b1]
        end = self.keypad[b2]
        delta = end - start
        dx, dy = int(delta.real), int(delta.imag)
        x_it = itertools.repeat(Direction.LEFT if dx < 0 else Direction.RIGHT, abs(dx))
        y_it = itertools.repeat(Direction.UP if dy < 0 else Direction.DOWN, abs(dy))
        it = itertools.chain(x_it, y_it)
        possible_paths = mi.unique_everseen(itertools.permutations(it))
        # remove paths that'd move to positions where no button is present
        return frozenset("".join(map(str, p)) for p in possible_paths if self._is_valid_path(start, p))

    # TODO: can we make this recursive and cache it for a perf boost?
    def _is_valid_path(self, start: complex, possible_path: Iterable[Direction]) -> bool:
        valid_positions = self._valid_positions()
        p = start
        for d in possible_path:
            p += d.value
            if p not in valid_positions:
                return False
        return True


NUMERIC_ROBOT = KeypadPressingRobot(keypad=NUMERIC_BUTTON_ARRANGEMENT)
DIRECTIONAL_ROBOT = KeypadPressingRobot(keypad=DIRECTIONAL_BUTTON_ARRANGEMENT)


@dataclasses.dataclass(frozen=True, slots=True)
class Code:
    value: str

    def complexity(self) -> int:
        return self.length_of_shortest_sequence() * self.numeric_part()

    def length_of_shortest_sequence(self) -> int:
        out = NUMERIC_ROBOT.ways_to_press(self.value)
        out = set(itertools.chain.from_iterable(DIRECTIONAL_ROBOT.ways_to_press(o) for o in out))
        out = set(itertools.chain.from_iterable(DIRECTIONAL_ROBOT.ways_to_press(o) for o in out))
        return min(len(o) for o in out)

    def numeric_part(self) -> int:
        return mi.one(util.ints(self.value))


def part_1(txt: str) -> int:
    return sum(c.complexity() for c in map(Code, txt.splitlines()))


def part_2(txt: str) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
