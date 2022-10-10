from typing import Callable

Point = tuple[int, int]
Grid = dict[Point, str]


def step(grid: Grid, width: int, height: int) -> Grid:
    move_right = lambda x, y: ((x + 1) % width, y)
    move_down = lambda x, y: (x, (y + 1) % height)
    return partial_step(partial_step(grid, move_right, ">"), move_down, "v")


def partial_step(grid: Grid, new_pos_f: Callable[[int, int], tuple[int, int]], direction: str) -> Grid:
    new_grid = {p: c for p, c in grid.items() if c != direction}
    for p, c in grid.items():
        if c == direction:
            new_p = new_pos_f(*p)
            new_grid[new_p if new_p not in grid else p] = direction
    return new_grid


def parta(txt: str) -> int:
    lines = txt.splitlines()

    height = len(lines)
    width = len(lines[0])

    grid = {(x, y): c for y, line in enumerate(lines) for x, c in enumerate(line) if c != "."}

    i = 1
    while (new_grid := step(grid, width, height)) != grid:
        grid = new_grid
        i += 1
    return i


def main(txt: str) -> None:
    print(f"parta: {parta(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
