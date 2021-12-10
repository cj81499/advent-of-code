import heapq
from collections import defaultdict

Point = tuple[int, int]
Grid = dict[Point, int]


def parta(txt: str) -> int:
    grid = parse_grid(txt)
    return sum(1 + grid[p] for p in low_points(grid))


def partb(txt: str) -> int:
    grid = parse_grid(txt)

    reverse_flow = defaultdict(set)
    for from_p, n in grid.items():
        if n == 9:
            continue
        to_p = min((a for a in adj(from_p) if a in grid), key=lambda a: grid[a])
        reverse_flow[to_p].add(from_p)

    basin_sizes = []
    for low_point in low_points(grid):
        basin = set()
        to_explore = {low_point}
        while to_explore:
            current_point = to_explore.pop()
            basin.add(current_point)
            new_var = reverse_flow.get(current_point)
            if new_var:
                to_explore.update(p for p in new_var if p not in basin)
        basin_sizes.append(len(basin))

    a, b, c = heapq.nlargest(3, basin_sizes)
    return a * b * c


def parse_grid(txt: str) -> Grid:
    return {(x, y): int(c) for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line)}


def low_points(grid: Grid) -> set[Point]:
    return {p for p, n in grid.items() if all(n < grid[a] for a in adj(p) if a in grid)}


def adj(point: Point) -> set[Point]:
    x, y = point
    return {(x + dx, y + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))}


def main(txt: str) -> None:
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
