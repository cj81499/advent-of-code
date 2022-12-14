from collections import deque
from collections.abc import Generator
from typing import Literal

import more_itertools as mi


def parta(txt: str, part: Literal[1, 2] = 1) -> int:
    grid = {complex(x, y): c for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line)}

    def adj(p: complex) -> Generator[complex, None, None]:
        yield from (adj_p for dir in (1j, -1j, 1, -1) if (adj_p := p + dir) in grid)

    def elevation(p: complex) -> int:
        c = grid[p]
        assert len(c) == 1
        if c == "S":
            return ord("a") - ord("a")  # 0
        if c == "E":
            return ord("z") - ord("a")  # 26
        assert c.isalpha() and c.islower()
        return ord(c) - ord("a")

    def can_move(current: complex, destination: complex) -> bool:
        if part == 2:
            current, destination = destination, current
        # elevation of destination can be at most one higher than the elevation of current
        return elevation(current) + 1 >= elevation(destination)

    explore_from = "S" if part == 1 else "E"
    start_point = mi.only(p for p, c in grid.items() if c == explore_from)
    assert start_point is not None

    end_at = "E" if part == 1 else "aS"
    possible_end_points = {p for p, c in grid.items() if c in end_at}

    to_explore = deque((start_point,))
    steps_to_reach = {start_point: 0}

    while to_explore:
        current = to_explore.popleft()
        next_cost = steps_to_reach[current] + 1
        # for each adj position on the grid
        for adj_p in adj(current):
            # if we found a way to reach adj_p for the first time or by taking fewer steps
            if can_move(current, adj_p) and (adj_p not in steps_to_reach or next_cost < steps_to_reach[adj_p]):
                steps_to_reach[adj_p] = next_cost
                to_explore.append(adj_p)

    # in part 1, there's only one possible end point
    return min(steps_to_reach[p] for p in possible_end_points if p in steps_to_reach)


def partb(txt: str) -> int:
    return parta(txt, part=2)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
