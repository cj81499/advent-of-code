import heapq
from collections import defaultdict
from functools import lru_cache

WALL = "#"


UP = complex(0, -1)
DOWN = complex(0, 1)
LEFT = complex(-1, 0)
RIGHT = complex(1, 0)

DIRECTIONS = {"^": UP, "v": DOWN, "<": LEFT, ">": RIGHT}


def part_1(txt: str) -> int:
    grid = defaultdict(
        set, {complex(x, y): {c} for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line) if c != "."}
    )

    min_x = min(int(p.real) for p in grid) + 1
    max_x = max(int(p.real) for p in grid) - 1
    min_y = min(int(p.imag) for p in grid) + 1
    max_y = max(int(p.imag) for p in grid) - 1

    @lru_cache
    def grid_after(minutes: int) -> dict[complex, set[str]]:
        assert minutes >= 0
        if minutes == 0:
            return grid
        start = grid_after(minutes - 1)
        new_grid: dict[complex, set[str]] = defaultdict(set)
        for p, contents in start.items():
            if WALL in contents:
                new_grid[p].add(WALL)
            else:
                for c in contents:
                    possible_new_pos = p + DIRECTIONS[c]
                    if possible_new_pos not in start or WALL not in start[possible_new_pos]:
                        new_grid[possible_new_pos].add(c)
                    else:
                        if c == "^":
                            new_grid[complex(p.real, max_y)].add(c)
                        elif c == "v":
                            new_grid[complex(p.real, min_y)].add(c)
                        elif c == "<":
                            new_grid[complex(max_x, p.imag)].add(c)
                        elif c == ">":
                            new_grid[complex(min_x, p.imag)].add(c)

        return new_grid

    start = complex(1, 0)
    goal = complex(max_x, max_y + 1)

    h = [(0, (start.real, start.imag))]
    while h:
        cost, pos_tuple = heapq.heappop(h)
        pos = complex(*pos_tuple)
        if pos == goal:
            return cost
        g = grid_after(cost + 1)
        for adj in (pos, *(pos + d for d in DIRECTIONS.values())):
            if adj in (start, goal) or (min_x <= adj.real <= max_x and min_y <= adj.imag <= max_y and len(g[adj]) == 0):
                next_state = (cost + 1, (adj.real, adj.imag))
                if next_state not in h:
                    heapq.heappush(h, next_state)

    assert False, "unreachable"


def part_2(txt: str) -> int:
    grid = defaultdict(
        set, {complex(x, y): {c} for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line) if c != "."}
    )

    min_x = min(int(p.real) for p in grid) + 1
    max_x = max(int(p.real) for p in grid) - 1
    min_y = min(int(p.imag) for p in grid) + 1
    max_y = max(int(p.imag) for p in grid) - 1

    @lru_cache
    def grid_after(minutes: int) -> dict[complex, set[str]]:
        assert minutes >= 0
        if minutes == 0:
            return grid
        start = grid_after(minutes - 1)
        new_grid: dict[complex, set[str]] = defaultdict(set)
        for p, contents in start.items():
            if WALL in contents:
                new_grid[p].add(WALL)
            else:
                for c in contents:
                    possible_new_pos = p + DIRECTIONS[c]
                    if possible_new_pos not in start or WALL not in start[possible_new_pos]:
                        new_grid[possible_new_pos].add(c)
                    else:
                        if c == "^":
                            new_grid[complex(p.real, max_y)].add(c)
                        elif c == "v":
                            new_grid[complex(p.real, min_y)].add(c)
                        elif c == "<":
                            new_grid[complex(max_x, p.imag)].add(c)
                        elif c == ">":
                            new_grid[complex(min_x, p.imag)].add(c)

        return new_grid

    def explore(*, start: complex, goal: complex, start_time: int = 0) -> int:
        h = [(start_time, (start.real, start.imag))]  # TODO: can we use a complex or do we need a tuple?
        while h:
            time, pos_tuple = heapq.heappop(h)
            pos = complex(*pos_tuple)
            if pos == goal:
                return time
            g = grid_after(time + 1)
            for adj in (pos, *(pos + d for d in DIRECTIONS.values())):
                if adj in (start, goal) or (
                    min_x <= adj.real <= max_x and min_y <= adj.imag <= max_y and len(g[adj]) == 0
                ):
                    next_state = (time + 1, (adj.real, adj.imag))
                    if next_state not in h:
                        heapq.heappush(h, next_state)
        assert False, "unreachable"

    start = complex(1, 0)
    goal = complex(max_x, max_y + 1)

    time = explore(start=start, goal=goal)  # start -> goal
    time = explore(start=goal, goal=start, start_time=time)  # goal -> start (elf forgot his snacks)
    time = explore(start=start, goal=goal, start_time=time)  # start -> goal (again...)
    return time


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
