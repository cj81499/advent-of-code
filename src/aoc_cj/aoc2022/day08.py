def is_visible(x: int, y: int, grid: list[list[int]]) -> bool:
    height = grid[y][x]

    col = [r[x] for r in grid]
    row = grid[y]

    above = col[:y]
    below = col[y + 1 :]

    left = row[:x]
    right = row[x + 1 :]

    return (
        all(n < height for n in above)
        or all(n < height for n in below)
        or all(n < height for n in left)
        or all(n < height for n in right)
    )


def parta(txt: str) -> int:
    count = 0

    grid = [[int(c) for c in line] for line in txt.splitlines()]

    for y, row in enumerate(grid):
        for x, _n in enumerate(row):
            if is_visible(x, y, grid):
                count += 1
    return count


def scenic_score(x: int, y: int, grid: list[list[int]]) -> int:
    height = grid[y][x]

    col = [r[x] for r in grid]
    row = grid[y]

    view_up = reversed(col[:y])
    view_down = col[y + 1 :]
    view_left = reversed(row[:x])
    view_right = row[x + 1 :]

    viewing_distance_up = 0
    viewing_distance_down = 0
    viewing_distance_left = 0
    viewing_distance_right = 0

    for h in view_up:
        viewing_distance_up += 1
        if h >= height:
            break

    for h in view_down:
        viewing_distance_down += 1
        if h >= height:
            break

    for h in view_left:
        viewing_distance_left += 1
        if h >= height:
            break

    for h in view_right:
        viewing_distance_right += 1
        if h >= height:
            break

    return viewing_distance_up * viewing_distance_down * viewing_distance_left * viewing_distance_right


def partb(txt: str) -> int:
    max_scenic_score = 0

    grid = [[int(c) for c in line] for line in txt.splitlines()]

    for y, row in enumerate(grid):
        for x, _n in enumerate(row):
            max_scenic_score = max(max_scenic_score, scenic_score(x, y, grid))

    return max_scenic_score


def main(txt: str) -> None:
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
