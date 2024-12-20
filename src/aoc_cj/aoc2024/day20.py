import dataclasses
from collections import deque

import more_itertools as mi

from aoc_cj import util


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class _State:
    cost: int
    pos: complex


def part_1(txt: str, *, target_savings: int = 100) -> int:
    grid = {x + y * 1j: c for y, row in enumerate(txt.splitlines()) for x, c in enumerate(row) if c != "#"}
    racetrack = {p for p, c in grid.items() if c in (".", "S", "E")}
    start = mi.one(p for p, c in grid.items() if c == "S")
    end = mi.one(p for p, c in grid.items() if c == "E")

    # find how far each position on the racetrack is from the end
    dist_from_end: dict[complex, int] = {}
    to_explore = deque[_State]()
    to_explore.append(_State(cost=0, pos=end))
    while to_explore:
        state = to_explore.popleft()
        if state.pos in dist_from_end:
            continue
        for pos in util.adj_4(state.pos):
            if pos in racetrack and pos not in dist_from_end:
                to_explore.append(_State(cost=state.cost + 1, pos=pos))
        dist_from_end[state.pos] = state.cost

    # for each position on the racetrack, see if we can cheat in a way that'll save us more that 100 picoseconds
    count = 0
    for pos, dist in dist_from_end.items():
        for cheat_delta in (-2, 2, -2j, 2j):
            pos_after_cheat = pos + cheat_delta
            distance_after_cheat = dist_from_end.get(pos_after_cheat)
            if distance_after_cheat is not None:
                # cost_with_cheat
                savings = dist - distance_after_cheat - 2  # 2s spent cheating
                if savings >= target_savings:
                    count += 1

    return count


def part_2(txt: str, *, target_savings: int = 100) -> int:
    grid = {x + y * 1j: c for y, row in enumerate(txt.splitlines()) for x, c in enumerate(row) if c != "#"}
    racetrack = {p for p, c in grid.items() if c in (".", "S", "E")}
    start = mi.one(p for p, c in grid.items() if c == "S")
    end = mi.one(p for p, c in grid.items() if c == "E")

    # find how far each position on the racetrack is from the end
    dist_from_end: dict[complex, int] = {}
    to_explore = deque[_State]()
    to_explore.append(_State(cost=0, pos=end))
    while to_explore:
        state = to_explore.popleft()
        if state.pos in dist_from_end:
            continue
        for cheat_start_pos in util.adj_4(state.pos):
            if cheat_start_pos in racetrack and cheat_start_pos not in dist_from_end:
                to_explore.append(_State(cost=state.cost + 1, pos=cheat_start_pos))
        dist_from_end[state.pos] = state.cost

    max_cheat_delta = 20
    cheat_deltas = set[complex]()
    for x in range(max_cheat_delta + 1):
        for y in range(max_cheat_delta + 1):
            if 2 <= x + y <= max_cheat_delta:
                cheat_deltas.add(x + y * 1j)
                cheat_deltas.add(-x + y * 1j)
                cheat_deltas.add(x + y * -1j)
                cheat_deltas.add(-x + y * -1j)

    # for each position on the racetrack, see if we can cheat in a way that'll save us more that 100 picoseconds
    count = 0
    for cheat_start_pos, dist in dist_from_end.items():
        for cheat_delta in cheat_deltas:
            cheat_end_pos = cheat_start_pos + cheat_delta
            cheat_duration = abs(cheat_delta.real) + abs(cheat_delta.imag)
            distance_after_cheat = dist_from_end.get(cheat_end_pos)
            if distance_after_cheat is not None:
                # cost_with_cheat
                savings = dist - distance_after_cheat - cheat_duration
                if savings >= target_savings:
                    count += 1

    return count


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
