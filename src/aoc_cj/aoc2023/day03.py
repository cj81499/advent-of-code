import dataclasses
import functools
import math
from collections.abc import Generator
from typing import ClassVar

from aoc_cj import util


@dataclasses.dataclass(frozen=True)
class Number:
    raw_value: str
    x_start: int
    y: int

    @property
    def value(self) -> int:
        return int(self.raw_value)

    @property
    def x_end(self) -> int:
        return self.x_start + len(self.raw_value) - 1

    def is_adjacent_to(self, pos: complex) -> bool:
        return pos in self.adjacent_positions

    @functools.cached_property  # optimization: avoid recomputing the adjacent positions
    def adjacent_positions(self) -> frozenset[complex]:
        adj = {
            complex(x, y)
            for y in (self.y - 1, self.y + 1)  # 1 above and 1 below number
            for x in range(self.x_start - 1, self.x_end + 2)  # from left to right of number
        }
        adj.add(complex(self.x_start - 1, self.y))  # to the left of number
        adj.add(complex(self.x_end + 1, self.y))  # to the right of number
        return frozenset(adj)


@dataclasses.dataclass
class EngineSchematic:
    numbers: set[Number]
    symbols: dict[complex, str]

    _parser: ClassVar = util.create_regex_parser(r"(\d+|\.+|\W)", str)

    @staticmethod
    def parse(s: str) -> "EngineSchematic":
        symbols = {}
        numbers = set()
        for y, line in enumerate(s.splitlines()):
            x = 0
            for chunk in EngineSchematic._parser(line):
                if chunk.isnumeric():
                    numbers.add(Number(chunk, x, y))
                elif len(chunk) == 1 and chunk != ".":
                    symbols[complex(x, y)] = chunk
                x += len(chunk)

        return EngineSchematic(numbers, symbols)

    def gear_ratios(self) -> Generator[int, None, None]:
        for possible_gear_pos, c in self.symbols.items():
            if c == "*":
                adjacent_numbers = {n for n in self.numbers if n.is_adjacent_to(possible_gear_pos)}
                if len(adjacent_numbers) == 2:
                    gear_ratio = math.prod(n.value for n in adjacent_numbers)
                    yield gear_ratio

    def part_numbers(self) -> Generator[int, None, None]:
        for n in self.numbers:
            if any(n.is_adjacent_to(s) for s in self.symbols):
                yield n.value


def part_1(txt: str) -> int:
    return sum(EngineSchematic.parse(txt).part_numbers())


def part_2(txt: str) -> int:
    return sum(EngineSchematic.parse(txt).gear_ratios())


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
