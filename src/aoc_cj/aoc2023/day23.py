from collections import deque
from collections.abc import Generator
from typing import Callable

import more_itertools as mi

UP = -1j
DOWN = 1j
LEFT = -1
RIGHT = 1


def parta(txt: str) -> int:
    grid = {complex(x, y): c for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line)}
    max_y = int(max(p.imag for p in grid))
    start = mi.one(p for p, c in grid.items() if p.imag == 0 and c == ".")
    goal = mi.one(p for p, c in grid.items() if p.imag == max_y and c == ".")

    def next_positions(pos: complex, grid: dict[complex, str]) -> Generator[complex, None, None]:
        current_grid_val = grid[pos]
        if current_grid_val == "^":
            yield pos + UP
        elif current_grid_val == "v":
            yield pos + DOWN
        elif current_grid_val == "<":
            yield pos + LEFT
        elif current_grid_val == ">":
            yield pos + RIGHT
        elif current_grid_val == ".":
            for delta in (UP, DOWN, LEFT, RIGHT):
                new_pos = pos + delta
                new_grid_val = grid.get(new_pos, "#")
                if new_grid_val != "#":
                    yield new_pos
        else:
            assert False, f"unrecognized grid val: '{current_grid_val}'"

    return max(len(path) for path in paths_between(start, goal, grid, next_positions))


def paths_between(
    start: complex,
    goal: complex,
    grid: dict[complex, str],
    next_positions: Callable[[complex, dict[complex, str]], Generator[complex, None, None]],
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
    # IDEA (not implemented yet. this is fast enough for the test case, but not fast enough for the real input)
    # https://www.reddit.com/r/adventofcode/comments/18oy4pc/comment/kekf0hl/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
    # there are some very long paths where there is no branching allowed.
    # By creating an adjacency graph and "merging" any nodes that have exactly 2
    # neighbors into those neighbors, we get a graph with only a couple dozen
    # nodes instead of many thousands. The same DFS as before now completes
    # reasonably quickly.

    grid = {complex(x, y): c for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line)}
    max_y = int(max(p.imag for p in grid))
    start = mi.one(p for p, c in grid.items() if p.imag == 0 and c == ".")
    goal = mi.one(p for p, c in grid.items() if p.imag == max_y and c == ".")

    theoretical_max = sum(1 for c in grid.values() if c == ".")
    print(f"{theoretical_max=}")

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

    best = 0
    for path in paths_between(start, goal, grid, next_positions):
        print(len(path))
        best = max(best, len(path))
    return best


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
