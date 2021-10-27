from __future__ import annotations

from collections import deque

from aoc_cj.aoc2019.intcode_computer import IntcodeProgram

MOVES = {1: +0 - 1j, 2: +0 + 1j, 3: -1 + 0j, 4: +1 + 0j}
OPPOSITES = {1: 2, 2: 1, 3: 4, 4: 3}


def corners(grid):
    min_x = min(p.real for p in grid.keys())
    max_x = max(p.real for p in grid.keys())
    min_y = min(p.imag for p in grid.keys())
    max_y = max(p.imag for p in grid.keys())
    return min_x, max_x, min_y, max_y


def display(grid, pos=None):
    min_x, max_x, min_y, max_y = map(int, corners(grid))
    rows = []
    for y in range(min_y, max_y + 1):
        row = []
        for x in range(min_x, max_x + 1):
            p = complex(x, y)
            c = "*" if p == 0 + 0j else grid.get(p, " ")
            if pos is not None and p == pos:
                c = "D"
            row.append(c)
        rows.append("".join(row))
    screen_str = "\n".join(rows)
    return screen_str


DISPLAY_CHAR_MAP = {0: "#", 1: ".", 2: "O"}


def explore(p: IntcodeProgram, grid: dict, pos: complex = 0 + 0j):
    for command in range(1, 5):
        delta = MOVES[command]
        new_pos = pos + delta
        if new_pos not in grid:
            # try to move to new_pos
            p.write_input(command)
            p.run()
            # get result of trying to move
            status = p.outputs.popleft()
            grid[new_pos] = DISPLAY_CHAR_MAP[status]
            if status != 0:  # if we moved
                explore(p, grid, new_pos)  # explore from the new pos
                # after we're done exploring the branch, go back one step, so we can try the next move fom pos
                p.write_input(OPPOSITES[command])
                p.run()
                # pop the output from returning to where we came from. we know this is not a wall
                assert p.outputs.popleft() != 0


def get_complete_map(txt: str):
    p = IntcodeProgram.parse(txt)
    p.run()
    grid = {}
    explore(p, grid)
    # print(display(grid)) # see the grid
    return grid


def parta(txt: str):
    complete_map = get_complete_map(txt)
    # bfs on grid starting @ 0,0 to find oxygen
    q = deque([(0 + 0j, 0)])
    explored = set()
    while q:
        pos, distance = q.popleft()
        if pos not in explored:
            if complete_map[pos] == "O":
                return distance
            elif complete_map[pos] == ".":
                q.extend((pos + m, distance + 1) for m in MOVES.values())
            explored.add(pos)
    return -1


def partb(txt: str):
    complete_map = get_complete_map(txt)
    oxygen_pos = next(p for p, c in complete_map.items() if c == "O")
    q = deque([(oxygen_pos, 0)])
    explored = set()
    time = 0
    while q:
        pos, distance = q.popleft()
        if pos not in explored:
            if complete_map[pos] != "#":
                time = distance
                q.extend((pos + m, distance + 1) for m in MOVES.values())
            explored.add(pos)
    return time


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
