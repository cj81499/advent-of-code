import collections
import dataclasses
import math
from collections.abc import Generator, Sequence
from typing import ClassVar

import more_itertools as mi

from aoc_cj import util


@dataclasses.dataclass(frozen=True)
class Game:
    id: int
    reveals: Sequence[tuple[int, str]]

    MAXES: ClassVar = {"red": 12, "green": 13, "blue": 14}
    _parser: ClassVar = util.create_regex_parser(r"[\w\d]+", str)

    def is_possible(self) -> bool:
        return all(int(count) <= Game.MAXES[color] for count, color in self.reveals)

    def power(self) -> int:
        return math.prod(self.min_cube_counts().values())

    def min_cube_counts(self) -> collections.Counter[str]:
        max_counts: collections.Counter[str] = collections.Counter()
        for count, color in self.reveals:
            max_counts[color] = max(max_counts[color], count)
        return max_counts

    @staticmethod
    def parse(s: str) -> "Game":
        _, game_id, *reveals = Game._parser(s)
        return Game(int(game_id), [(int(count), color) for count, color in mi.chunked(reveals, 2, strict=True)])


def parse_games(txt: str) -> Generator[Game, None, None]:
    yield from (Game.parse(l) for l in txt.splitlines())


def parta(txt: str) -> int:
    return sum(g.id for g in parse_games(txt) if g.is_possible())


def partb(txt: str) -> int:
    return sum(g.power() for g in parse_games(txt))


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
