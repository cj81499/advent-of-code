from collections import deque

import more_itertools as mi

Pos = tuple[int, int]


def parta(txt: str) -> int:
    grid = {(x, y): c for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line)}
    start_pos = mi.one(p for p, c in grid.items() if c == "S")

    def connections(p: Pos) -> tuple[Pos, Pos]:
        x, y = p
        above = (x, y - 1)
        below = (x, y + 1)
        left = (x - 1, y)
        right = (x + 1, y)
        pipe_type = grid[p]
        if pipe_type == "S":
            conns = []
            if grid.get(above, ".") in "|7F":
                conns.append(above)
            if grid.get(below, ".") in "|LJ":
                conns.append(below)
            if grid.get(left, ".") in "-LF":
                conns.append(left)
            if grid.get(right, ".") in "-J7":
                conns.append(right)
            assert len(conns) == 2, f"expected exactly 2 connections. Got {conns}"
            conn1, conn2 = conns
            return conn1, conn2
        elif pipe_type == "|":
            return above, below
        elif pipe_type == "-":
            return left, right
        elif pipe_type == "L":
            return above, right
        elif pipe_type == "J":
            return above, left
        elif pipe_type == "7":
            return below, left
        elif pipe_type == "F":
            return below, right
        assert False, f"unexpected value in pipe: '{pipe_type}'"

    distances: dict[Pos, int] = {}
    to_explore = deque([(start_pos, 0)])
    while to_explore:
        p, distance = to_explore.popleft()
        if p in distances:
            continue
        conns = connections(p)
        distances[p] = distance
        for adj_p in conns:
            if adj_p not in distances:
                to_explore.append((adj_p, distance + 1))

    return max(distances.values())


def partb(txt: str) -> int:
    grid = {(x, y): c for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line)}
    start_pos = mi.one(p for p, c in grid.items() if c == "S")

    def connections(p: Pos) -> tuple[Pos, Pos]:
        x, y = p
        above = (x, y - 1)
        below = (x, y + 1)
        left = (x - 1, y)
        right = (x + 1, y)
        pipe_type = grid[p]
        if pipe_type == "S":
            conns = []
            if grid.get(above, ".") in "|7F":
                conns.append(above)
            if grid.get(below, ".") in "|LJ":
                conns.append(below)
            if grid.get(left, ".") in "-LF":
                conns.append(left)
            if grid.get(right, ".") in "-J7":
                conns.append(right)
            assert len(conns) == 2, f"expected exactly 2 connections. Got {conns}"
            conn1, conn2 = conns
            return conn1, conn2
        elif pipe_type == "|":
            return above, below
        elif pipe_type == "-":
            return left, right
        elif pipe_type == "L":
            return above, right
        elif pipe_type == "J":
            return above, left
        elif pipe_type == "7":
            return below, left
        elif pipe_type == "F":
            return below, right
        assert False, f"unexpected value in pipe: '{pipe_type}'"

    loop: dict[Pos, int] = {}
    to_explore = deque([(start_pos, 0)])
    while to_explore:
        p, distance = to_explore.popleft()
        if p in loop:
            continue
        conns = connections(p)
        loop[p] = distance
        to_explore.extend((adj_p, distance + 1) for adj_p in conns)

    max_pos = max(p for p in grid)
    max_x, max_y = max_pos

    # find tiles enclosed by the loop
    # starting from top left corner of (0, 0), we will "flood" the grid.
    flood_reachable: set[Pos] = set()
    to_explore = deque([(0, 0)])
    while to_explore:
        p = to_explore.popleft()
        if p in flood_reachable:
            continue
        x, y = p
        if not ((0 <= x <= max_x + 1) and (0 <= y <= max_y + 1)):
            continue
        flood_reachable.add(p)
        # can reach corner only if the path is not blocked by a pipe in the loop
        can_move_up = (
            (x - 1, y - 1) not in loop or (x, y - 1) not in loop or (x - 1, y - 1) not in connections((x, y - 1))
        )
        can_move_down = (x - 1, y) not in loop or (x, y) not in loop or (x - 1, y) not in connections((x, y))
        can_move_left = (
            (x - 1, y - 1) not in loop or (x - 1, y) not in loop or (x - 1, y - 1) not in connections((x - 1, y))
        )
        can_move_right = (x, y - 1) not in loop or (x, y) not in loop or (x, y - 1) not in connections((x, y))
        # print(f"{p=} {can_move_up=} {can_move_down=} {can_move_left=} {can_move_right=}")
        if can_move_up:
            to_explore.append((x, y - 1))
        if can_move_down:
            to_explore.append((x, y + 1))
        if can_move_left:
            to_explore.append((x - 1, y))
        if can_move_right:
            to_explore.append((x + 1, y))

    # a tile is enclosed by the loop only if no corner is reached during flooding
    count = 0
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            top_left = (x, y)
            top_right = (x + 1, y)
            bottom_left = (x, y + 1)
            bottom_right = (x + 1, y + 1)
            if not any(p in flood_reachable for p in (top_left, top_right, bottom_left, bottom_right)):
                count += 1
    return count


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
