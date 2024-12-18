import dataclasses
import enum
import itertools
import math
from collections import deque
from collections.abc import Callable, Generator
from typing import Self

import more_itertools as mi

from aoc_cj import util


class Facing(enum.Enum):
    NORTH = -1j
    SOUTH = 1j
    EAST = 1
    WEST = -1


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class _State:
    pos: complex
    facing: Facing

    def next(self, valid_pos: Callable[[complex], bool]) -> Generator[tuple[Self, int], None, None]:
        cls = type(self)
        for new_pos in util.adj_4(self.pos):
            if valid_pos(new_pos):
                new_facing = Facing(new_pos - self.pos)
                turned = new_facing != self.facing
                cost_increase = (1000 if turned else 0) + 1
                yield cls(pos=new_pos, facing=new_facing), cost_increase


def part_1(txt: str) -> int:
    start, end, walls = parse(txt)

    initial = _State(pos=start, facing=Facing.EAST)
    to_explore = deque(((0, initial),))
    valid_pos = lambda p: p not in walls
    cheapest: dict[_State, int] = {}
    while to_explore:
        cost, state = to_explore.popleft()
        if cost < cheapest.get(state, math.inf):
            cheapest[state] = cost
            for next_state, cost_increase in state.next(valid_pos):
                to_explore.append((cost + cost_increase, next_state))

    return min(cost for s, cost in cheapest.items() if s.pos == end)


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class _CheapTracker:
    cost: int
    seen: set[complex]


def part_2(txt: str) -> int:
    start, end, walls = parse(txt)

    initial_state = _State(pos=start, facing=Facing.EAST)
    to_explore = deque[tuple[int, _State, _State]]()
    to_explore.append((0, initial_state, initial_state))
    valid_pos = lambda p: p not in walls
    cheapest: dict[_State, _CheapTracker] = {}
    while to_explore:
        cost, state, prev_state = to_explore.popleft()
        best = cheapest.get(state, None)
        # if we've found a new best
        if best is None or cost < best.cost:
            seen_on_way = cheapest[prev_state].seen if prev_state in cheapest else set()
            cheapest[state] = _CheapTracker(cost=cost, seen=seen_on_way | {state.pos})
            for next_state, cost_increase in state.next(valid_pos):
                to_explore.append((cost + cost_increase, next_state, state))
        elif cost == best.cost:
            best.seen.update(cheapest[prev_state].seen)
            best.seen.add(state.pos)

    end_states = {s: v for s, v in cheapest.items() if s.pos == end}
    min_cost = min(best.cost for _, best in end_states.items())
    positions_along_min_cost_paths = set(
        itertools.chain.from_iterable(best.seen for best in end_states.values() if best.cost == min_cost)
    )
    return len(positions_along_min_cost_paths)


def parse(txt: str) -> tuple[complex, complex, set[complex]]:
    grid = {x + y * 1j: c for y, row in enumerate(txt.splitlines()) for x, c in enumerate(row) if c != "."}
    start = mi.one(p for p, c in grid.items() if c == "S")
    end = mi.one(p for p, c in grid.items() if c == "E")
    walls = {p for p, c in grid.items() if c == "#"}
    return start, end, walls


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
