from collections.abc import Iterable


def is_visible(x: int, y: int, grid: list[list[int]]) -> bool:
    height = grid[y][x]

    col = [r[x] for r in grid]
    row = grid[y]

    return (
        all(n < height for n in col[:y])  # above
        or all(n < height for n in col[y + 1 :])  # below
        or all(n < height for n in row[:x])  # left
        or all(n < height for n in row[x + 1 :])  # right
    )


def scenic_score(x: int, y: int, grid: list[list[int]]) -> int:
    height = grid[y][x]

    col = [r[x] for r in grid]
    row = grid[y]

    return (
        view_distance(height, reversed(col[:y]))  # up
        * view_distance(height, col[y + 1 :])  # down
        * view_distance(height, reversed(row[:x]))  # left
        * view_distance(height, row[x + 1 :])  # right
    )


def view_distance(height: int, view: Iterable[int]) -> int:
    vd = 0
    for h in view:
        vd += 1
        if h >= height:
            break
    return vd


def parta(txt: str) -> int:
    grid = [[int(c) for c in line] for line in txt.splitlines()]
    return sum(1 for y, row in enumerate(grid) for x, _n in enumerate(row) if is_visible(x, y, grid))


def partb(txt: str) -> int:
    grid = [[int(c) for c in line] for line in txt.splitlines()]
    return max(scenic_score(x, y, grid) for y, row in enumerate(grid) for x, _n in enumerate(row))


def main(txt: str) -> None:
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
