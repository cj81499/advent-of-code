import dataclasses
import itertools
from collections import deque
from collections.abc import Generator
from typing import Self

import more_itertools as mi

from aoc_cj import util

Grid = dict[complex, str]


@dataclasses.dataclass(frozen=True, kw_only=True)
class StateA:
    pos: complex
    steps: int = 0
    collected: frozenset[str] = frozenset()

    def next_states(self, grid: Grid) -> Generator[Self]:
        cls = type(self)
        q = deque(((self.pos, self.steps),))
        seen: set[complex] = set()
        while len(q) > 0:
            pos, steps = q.popleft()
            if pos in seen:
                continue
            val = grid[pos]
            if val in ".@" or val.lower() in self.collected:
                q.extend((pos + delta, steps + 1) for delta in (-1j, 1, 1j, -1))
            elif val != "#" and val.islower():
                yield cls(pos=pos, steps=steps, collected=frozenset((*self.collected, val)))
            seen.add(pos)


@dataclasses.dataclass(frozen=True, kw_only=True)
class StateB:
    pos: tuple[complex, ...]
    steps: int = 0
    collected: frozenset[str] = frozenset()

    def next_states(self, grid: Grid) -> Generator[Self]:
        cls = type(self)
        for i, pos in enumerate(self.pos):
            for new_state in StateA(pos=pos, steps=self.steps, collected=self.collected).next_states(grid):
                new_positions = list(self.pos)
                new_positions[i] = new_state.pos
                yield cls(pos=tuple(new_positions), steps=new_state.steps, collected=new_state.collected)


def search[TState: (StateA, StateB)](start: TState, grid: Grid) -> int:
    all_keys = frozenset(c for c in grid.values() if c.islower())

    q = util.PriorityQueue[TState]()
    q.push(0, start)
    seen: set[tuple[complex | tuple[complex, ...], frozenset[str]]] = set()
    while q:
        state = q.pop()
        if (state.pos, state.collected) in seen:
            continue
        # if all keys have been collected
        if state.collected == all_keys:
            return state.steps
        for s in state.next_states(grid):
            q.push(s.steps, s)
        seen.add((state.pos, state.collected))
    assert False, "unreachable"


def part_1(txt: str) -> int:
    grid = {complex(x, y): c for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line)}
    start_pos = mi.one(p for p, c in grid.items() if c == "@")

    return search(StateA(pos=start_pos), grid)


def part_2(txt: str) -> int:
    grid = {complex(x, y): c for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line)}
    start_pos = mi.one(p for p, c in grid.items() if c == "@")

    # update the cave entrance
    replace = "@#@\n###\n@#@".splitlines()
    for x, y in itertools.product(range(3), repeat=2):
        grid[start_pos + complex(x - 1, y - 1)] = replace[y][x]

    start = tuple(start_pos + delta for delta in (-1 - 1j, 1 - 1j, 1 + 1j, -1 + 1j))
    return search(StateB(pos=start), grid)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
