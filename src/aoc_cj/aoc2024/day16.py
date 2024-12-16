import dataclasses
import enum
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


def part_2(txt: str) -> int:
    start, end, walls = parse(txt)

    initial = _State(pos=start, facing=Facing.EAST)
    to_explore = deque[tuple[int, _State, _State | None]](((0, initial, None),))
    valid_pos = lambda p: p not in walls
    cheapest: dict[_State, tuple[int, set[complex]]] = {}
    while to_explore:
        cost, state, prev_state = to_explore.popleft()
        if state not in cheapest:
            if prev_state not in cheapest:
                cheapest[state] = (cost, {state.pos})
            else:
                cheapest[state] = (cost, cheapest[prev_state][1].union((state.pos,)))
            for next_state, cost_increase in state.next(valid_pos):
                to_explore.append((cost + cost_increase, next_state, state))
        else:
            cheapest_cost, seen = cheapest[state]
            seen_on_way = cheapest[prev_state][1].union((state.pos,)) if prev_state in cheapest else {state.pos}
            if cost == cheapest_cost:
                seen.update(seen_on_way)
            elif cost < cheapest_cost:
                cheapest[state] = (cost, seen_on_way)
                for next_state, cost_increase in state.next(valid_pos):
                    to_explore.append((cost + cost_increase, next_state, state))

    end_states = {s: v for s, v in cheapest.items() if s.pos == end}
    print(end_states)
    min_cost = min(cost for _, (cost, _) in end_states.items())
    min_cost_end_states = {s: p for s, (cost, p) in end_states.items() if cost == min_cost}
    print(min_cost_end_states)
    positions = set[complex]()
    for p in min_cost_end_states.values():
        positions.update(p)
    return len(positions)


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
