from collections.abc import Generator
from dataclasses import dataclass
from typing import Self, override

from aoc_cj import util

UP = -1j
DOWN = +1j
LEFT = -1
RIGHT = +1

DIRECTIONS = frozenset((UP, DOWN, LEFT, RIGHT))


@dataclass(frozen=True)
class Crucible:
    pos: complex
    direction: complex
    duration: int

    def can_turn_or_stop(self) -> bool:
        return True

    def _must_turn(self) -> bool:
        return self.duration >= 3

    def _next_directions(self) -> Generator[complex, None, None]:
        if self.can_turn_or_stop():
            # crucibles may not turn around 180°
            opposite_direction = self.direction * -1
            invalid_directions = [opposite_direction]
            # if the crucible must turn, it cannot continue in the current direction
            if self._must_turn():
                invalid_directions.append(self.direction)
            yield from DIRECTIONS.difference(invalid_directions)
        else:
            yield self.direction

    def next_states(self, grid: dict[complex, int]) -> Generator[Self, None, None]:
        for direction in self._next_directions():
            new_pos = self.pos + direction
            if new_pos in grid:
                new_duration = 1 if direction != self.direction else self.duration + 1
                yield self.new(pos=new_pos, direction=direction, duration=new_duration)

    @classmethod
    def new(cls, *, pos: complex = 0, direction: complex, duration: int = 0) -> Self:
        return cls(pos, direction, duration)


class UltraCrucible(Crucible):
    @override
    def can_turn_or_stop(self) -> bool:
        return self.duration >= 4

    @override
    def _must_turn(self) -> bool:
        return self.duration >= 10


def min_heat_loss(grid: dict[complex, int], crucible_cls: type[Crucible] = Crucible) -> int:
    def _helper() -> Generator[int, None, None]:
        """explore the grid, yielding the amount of heat lost each time we find a path to the destination"""
        max_x = int(max(p.real for p in grid))
        max_y = int(max(p.imag for p in grid))
        destination = complex(max_x, max_y)

        to_explore: util.PriorityQueue[Crucible] = util.PriorityQueue()
        to_explore.push(0, crucible_cls.new(direction=RIGHT))
        to_explore.push(0, crucible_cls.new(direction=DOWN))

        seen = set[Crucible]()
        while to_explore:
            state, heat_loss = to_explore.pop_with_priority()
            # skip states we've already seen and states that are more expensive than what we already know it "costs" to reach the goal
            if state in seen:
                continue
            seen.add(state)
            if state.pos == destination and state.can_turn_or_stop():
                yield heat_loss
            else:
                for s in state.next_states(grid):
                    to_explore.push(heat_loss + grid[s.pos], s)

    return min(_helper())


def part_1(txt: str) -> int:
    grid = {complex(x, y): int(c) for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line)}
    return min_heat_loss(grid)


def part_2(txt: str) -> int:
    grid = {complex(x, y): int(c) for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line)}
    return min_heat_loss(grid, crucible_cls=UltraCrucible)


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
