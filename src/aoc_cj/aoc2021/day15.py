import heapq
import itertools
from collections.abc import Iterator

Point = tuple[int, int]


def adj(point: Point) -> Iterator[Point]:
    x, y = point
    yield from ((x + dx, y + dy) for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)))


def min_risk(grid: dict[Point, int]) -> int:
    goal = max(grid)

    risk_of_path_to_point = {(0, 0): 0}
    h = [(0, (0, 0))]
    while h:
        risk_so_far, p = heapq.heappop(h)

        if p == goal:
            continue

        for adj_p in adj(p):
            if adj_p in grid and adj_p not in risk_of_path_to_point:
                new_risk = risk_so_far + grid[adj_p]
                risk_of_path_to_point[adj_p] = new_risk
                heapq.heappush(h, (new_risk, adj_p))

    return risk_of_path_to_point[goal]


def part_1(txt: str) -> int:
    grid = {(x, y): int(n) for y, line in enumerate(txt.splitlines()) for x, n in enumerate(line)}
    return min_risk(grid)


def part_2(txt: str) -> int:
    grid = {(x, y): int(n) for y, line in enumerate(txt.splitlines()) for x, n in enumerate(line)}

    max_x, max_y = max(grid)

    full_grid = {
        (i * (max_x + 1) + x, j * (max_y + 1) + y): 1 + (n + i + j - 1) % 9
        for ((x, y), n), i, j in itertools.product(grid.items(), range(5), range(5))
    }

    return min_risk(full_grid)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
