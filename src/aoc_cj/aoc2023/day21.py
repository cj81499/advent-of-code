import itertools
from functools import cache, cached_property

import more_itertools as mi
from typing_extensions import Self

UP = -1j
DOWN = 1j
LEFT = -1
RIGHT = 1


class Grid:
    def __init__(self, contents: dict[complex, str]) -> None:
        self._contents = contents

        @cache
        def _reachable_from_normalized(p: complex) -> frozenset[complex]:
            return frozenset(
                new_p for delta in (UP, DOWN, LEFT, RIGHT) if self._contents[self._normalize(new_p := p + delta)] != "#"
            )

        self._reachable_from_normalized = _reachable_from_normalized

    @classmethod
    def parse(cls, s: str) -> Self:
        return cls({complex(x, y): c for y, line in enumerate(s.splitlines()) for x, c in enumerate(line)})

    @cached_property
    def start(self) -> complex:
        return mi.one(p for p, c in self._contents.items() if c == "S")

    def reachable_from(self, p: complex) -> frozenset[complex]:
        normalized_p = self._normalize(p)
        p_diff = p - normalized_p
        return frozenset(p_diff + norm_reachable for norm_reachable in self._reachable_from_normalized(normalized_p))

    def _normalize(self, p: complex) -> complex:
        return complex(p.real % self._x_bound, p.imag % self._y_bound)

    @cached_property
    def _x_bound(self) -> int:
        return int(max(p.real for p in self._contents)) + 1

    @cached_property
    def _y_bound(self) -> int:
        return int(max(p.imag for p in self._contents)) + 1


def solve(txt: str, steps: int) -> int:
    grid = Grid.parse(txt)
    to_explore = {grid.start}
    for _ in range(steps):
        to_explore = set(itertools.chain.from_iterable(map(grid.reachable_from, to_explore)))
    return len(to_explore)


def parta(txt: str) -> int:
    return solve(txt, 64)  # pragma: no cover


def partb(txt: str) -> int:
    raise NotImplementedError()
    return solve(txt, 26501365)  # type: ignore[unreachable] # pragma: no cover


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
