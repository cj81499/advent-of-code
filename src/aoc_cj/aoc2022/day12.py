from collections import deque
from collections.abc import Generator

import more_itertools as mi


def adj(p: complex) -> Generator[complex, None, None]:
    for dir in (1j, -1j, 1, -1):
        yield p + dir


def height(p: complex, grid: dict[complex, str]) -> str:
    val = grid[p]
    if val == "S":
        return "a"
    if val == "E":
        return "z"
    assert val.isalpha() and val.islower()
    return val


def parta(txt: str) -> int:
    grid = {x + (y * 1j): c for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line)}

    start_pos = mi.only(p for p, c in grid.items() if c == "S")
    assert start_pos is not None
    end_pos = mi.only(p for p, c in grid.items() if c == "E")
    assert end_pos is not None

    to_explore = deque((start_pos,))
    reached = {start_pos: 0}

    while to_explore:
        exploring = to_explore.popleft()
        next_cost = reached[exploring] + 1
        height_p = height(exploring, grid)
        for adj_p in adj(exploring):
            if adj_p in grid:
                height_adj = height(adj_p, grid)
                if ord(height_adj) <= ord(height_p) + 1:
                    if adj_p not in reached or next_cost < reached[adj_p]:
                        reached[adj_p] = next_cost
                        to_explore.append(adj_p)

    return reached[end_pos]


def partb(txt: str) -> int:
    grid = {x + (y * 1j): c for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line)}

    end_pos = mi.only(p for p, c in grid.items() if c == "E")
    assert end_pos is not None
    possible_starts = {p for p, c in grid.items() if c in ("a", "S")}

    to_explore = deque((end_pos,))
    reached = {end_pos: 0}

    while to_explore:
        exploring = to_explore.popleft()
        next_cost = reached[exploring] + 1
        height_p = height(exploring, grid)
        for adj_p in adj(exploring):
            if adj_p in grid:
                height_adj = height(adj_p, grid)
                if ord(height_p) <= ord(height_adj) + 1:
                    if adj_p not in reached or next_cost < reached[adj_p]:
                        reached[adj_p] = next_cost
                        to_explore.append(adj_p)

    return min(reached[s] for s in possible_starts if s in reached)


def main(txt: str) -> None:
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
