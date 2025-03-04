import functools
from collections import deque
from collections.abc import Generator

import more_itertools as mi

from aoc_cj import util


def cheat_generator(txt: str, *, max_cheat_duration: int = 2) -> Generator[float]:
    grid = {x + y * 1j: c for y, row in enumerate(txt.splitlines()) for x, c in enumerate(row) if c != "#"}
    racetrack = {p for p, c in grid.items() if c in (".", "S", "E")}
    end = mi.one(p for p, c in grid.items() if c == "E")

    # find how far each position on the racetrack is from the end
    dist_from_end: dict[complex, int] = {}
    to_explore = deque[tuple[int, complex]]()
    to_explore.append((0, end))
    while to_explore:
        cost, pos = to_explore.popleft()
        for cheat_start_pos in util.adj_4(pos):
            if cheat_start_pos in racetrack and cheat_start_pos not in dist_from_end:
                to_explore.append((cost + 1, cheat_start_pos))
        dist_from_end[pos] = cost

    cheat_deltas = set[complex]()
    for x in range(max_cheat_duration + 1):
        for y in range(max_cheat_duration + 1):
            if 2 <= x + y <= max_cheat_duration:
                cheat_deltas.add(complex(x, y))
                cheat_deltas.add(complex(-x, y))
                cheat_deltas.add(complex(x, -y))
                cheat_deltas.add(complex(-x, -y))

    # for each position on the racetrack, find ways to cheat
    for cheat_start_pos, dist in dist_from_end.items():
        for cheat_delta in cheat_deltas:
            cheat_end_pos = cheat_start_pos + cheat_delta
            cheat_duration = abs(cheat_delta.real) + abs(cheat_delta.imag)
            distance_after_cheat = dist_from_end.get(cheat_end_pos)
            if distance_after_cheat is not None:
                savings = dist - distance_after_cheat - cheat_duration
                yield savings


def solve(txt: str, *, max_cheat_duration: int = 2) -> int:  # pragma: no cover - no direct test cases provided
    return mi.ilen(c for c in cheat_generator(txt, max_cheat_duration=max_cheat_duration) if c >= 100)


part_1 = solve
part_2 = functools.partial(solve, max_cheat_duration=20)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
