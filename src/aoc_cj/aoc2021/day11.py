import itertools
from typing import Iterator

Point = tuple[int, int]
Grid = dict[Point, int]


def parse(txt: str) -> Grid:
    return {(x, y): int(c) for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line)}


def parta(txt: str) -> int:
    grid = parse(txt)

    flash_count = 0
    for _ in range(100):
        flashes, grid = step(grid)
        flash_count += flashes

    return flash_count


def adj(point: Point) -> Iterator[Point]:
    x, y = point
    yield from (p for p in ((x + dx, y + dy) for dx, dy in itertools.product(range(-1, 2), range(-1, 2))) if p != point)


def step(grid: Grid) -> tuple[int, Grid]:
    new_grid = {p: n + 1 for p, n in grid.items()}

    flashed: set[Point] = set()
    while new_flashes := {p for p, n in new_grid.items() if p not in flashed and n > 9}:
        for adj_p in itertools.chain.from_iterable(map(adj, new_flashes)):
            if adj_p in new_grid:
                new_grid[adj_p] += 1
        flashed |= new_flashes

    new_grid = {p: 0 if p in flashed else n for p, n in new_grid.items()}

    return len(flashed), new_grid


def partb(txt: str) -> int:
    grid = parse(txt)
    num_octopuses = len(grid)

    for i in itertools.count(1):
        flashes, grid = step(grid)
        if flashes == num_octopuses:
            return i

    assert False, "unreachable"


def main(txt: str) -> None:
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
