import dataclasses
import functools
import itertools
import typing as t
from collections.abc import Callable, Iterable

import more_itertools as mi

type Direction = t.Literal["L", "R"]
_DIRECTIONS = frozenset[Direction](t.get_args(Direction.__value__))


def is_direction(s: str) -> t.TypeIs[Direction]:
    return s in _DIRECTIONS


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class Rotation:
    direction: Direction
    distance: int

    @classmethod
    def parse(cls, s: str) -> t.Self:
        direction = s[0]
        assert is_direction(direction)
        return cls(direction=direction, distance=int(s[1:]))


simulate_dial = functools.partial(itertools.accumulate, func=lambda a, b: (a + b) % 100, initial=50)


def solve(get_moves: Callable[[Rotation], Iterable[int]], txt: str) -> int:
    rotations = map(Rotation.parse, txt.splitlines())
    moves = mi.flatten(map(get_moves, rotations))
    return sum(pos == 0 for pos in simulate_dial(moves))


part_1 = functools.partial(solve, lambda r: (-r.distance if r.direction == "L" else r.distance,))
part_2 = functools.partial(solve, lambda r: itertools.repeat(-1 if r.direction == "L" else 1, r.distance))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
