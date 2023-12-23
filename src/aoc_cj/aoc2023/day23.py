from collections import deque
from collections.abc import Generator
from typing import Callable

import more_itertools as mi

UP = -1j
DOWN = 1j
LEFT = -1
RIGHT = 1

DIRECTION_DELTA_MAP = {"^": UP, "v": DOWN, "<": LEFT, ">": RIGHT}

NextPositions = Callable[[complex, dict[complex, str]], Generator[complex, None, None]]


def parta(txt: str) -> int:
    def next_positions(pos: complex, grid: dict[complex, str]) -> Generator[complex, None, None]:
        current_grid_val = grid[pos]
        if (delta := DIRECTION_DELTA_MAP.get(current_grid_val)) is not None:
            yield pos + delta
        elif current_grid_val == ".":
            for delta in (UP, DOWN, LEFT, RIGHT):
                new_pos = pos + delta
                new_grid_val = grid.get(new_pos, "#")
                if new_grid_val != "#":
                    yield new_pos
        else:
            assert False, f"unrecognized grid val: '{current_grid_val}'"

    return solve(txt, next_positions)


def solve(txt: str, next_positions: NextPositions) -> int:
    grid = {complex(x, y): c for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line)}

    start = mi.one(p for p, c in grid.items() if p.imag == 0 and c == ".")

    max_y = int(max(p.imag for p in grid))
    goal = mi.one(p for p, c in grid.items() if p.imag == max_y and c == ".")

    return max(len(path) for path in paths_between(start, goal, grid, next_positions))


def paths_between(
    start: complex,
    goal: complex,
    grid: dict[complex, str],
    next_positions: NextPositions,
) -> Generator[frozenset[complex], None, None]:
    to_explore: deque[tuple[complex, frozenset[complex]]] = deque(((start, frozenset((start,))),))
    while to_explore:
        pos, seen = to_explore.popleft()
        if pos == goal:
            yield seen
        else:
            for next_pos in next_positions(pos, grid):
                if next_pos not in seen:
                    to_explore.append((next_pos, seen.union((pos,))))


def partb(txt: str) -> int:
    # IDEA (not implemented yet. as-is, this is fast enough for the test case, but not fast enough for the real input)
    #
    # https://www.reddit.com/r/adventofcode/comments/18oy4pc/comment/kekf0hl/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
    # there are some very long paths where there is no branching allowed.
    # By creating an adjacency graph and "merging" any nodes that have exactly 2
    # neighbors into those neighbors, we get a graph with only a couple dozen
    # nodes instead of many thousands. The same DFS as before now completes
    # reasonably quickly.

    def next_positions(pos: complex, grid: dict[complex, str]) -> Generator[complex, None, None]:
        current_grid_val = grid[pos]
        if current_grid_val != "#":
            for delta in (UP, DOWN, LEFT, RIGHT):
                new_pos = pos + delta
                new_grid_val = grid.get(new_pos, "#")
                if new_grid_val != "#":
                    yield new_pos
        else:
            assert False, f"unrecognized grid val: '{current_grid_val}'"

    return solve(txt, next_positions)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
