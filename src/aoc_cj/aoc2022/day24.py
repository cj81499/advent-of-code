import heapq
from collections import defaultdict
from functools import lru_cache

WALL = "#"


UP = complex(0, -1)
DOWN = complex(0, 1)
LEFT = complex(-1, 0)
RIGHT = complex(1, 0)

DIRECTIONS = {"^": UP, "v": DOWN, "<": LEFT, ">": RIGHT}


def parta(txt: str) -> int:
    grid = defaultdict(
        set, {complex(x, y): {c} for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line) if c != "."}
    )

    min_x = min(int(p.real) for p in grid) + 1
    max_x = max(int(p.real) for p in grid) - 1
    min_y = min(int(p.imag) for p in grid) + 1
    max_y = max(int(p.imag) for p in grid) - 1

    print(min_x, max_x, min_y, max_y)

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


def partb(txt: str) -> int:
    grid = defaultdict(
        set, {complex(x, y): {c} for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line) if c != "."}
    )

    min_x = min(int(p.real) for p in grid) + 1
    max_x = max(int(p.real) for p in grid) - 1
    min_y = min(int(p.imag) for p in grid) + 1
    max_y = max(int(p.imag) for p in grid) - 1

    print(min_x, max_x, min_y, max_y)

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
            break
        g = grid_after(cost + 1)
        for adj in (pos, *(pos + d for d in DIRECTIONS.values())):
            if adj in (start, goal) or (min_x <= adj.real <= max_x and min_y <= adj.imag <= max_y and len(g[adj]) == 0):
                next_state = (cost + 1, (adj.real, adj.imag))
                if next_state not in h:
                    heapq.heappush(h, next_state)

    start, goal = goal, start
    h = [(cost, (start.real, start.imag))]
    while h:
        cost, pos_tuple = heapq.heappop(h)
        pos = complex(*pos_tuple)
        if pos == goal:
            break
        g = grid_after(cost + 1)
        for adj in (pos, *(pos + d for d in DIRECTIONS.values())):
            if adj in (start, goal) or (min_x <= adj.real <= max_x and min_y <= adj.imag <= max_y and len(g[adj]) == 0):
                next_state = (cost + 1, (adj.real, adj.imag))
                if next_state not in h:
                    heapq.heappush(h, next_state)

    start, goal = goal, start
    h = [(cost, (start.real, start.imag))]
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


EXAMPLE_INPUT = """
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
""".strip()

# EXAMPLE_INPUT = """
# #.#####
# #.....#
# #>....#
# #.....#
# #...v.#
# #.....#
# #####.#
# """.strip()

if __name__ == "__main__":
    from aocd import data

    data = EXAMPLE_INPUT

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")