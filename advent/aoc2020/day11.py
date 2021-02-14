import collections

FLOOR = "."
EMPTY = "L"
OCCUPIED = "#"


def grid_get(grid, x, y):
    if y < 0 or len(grid) <= y or x < 0 or len(grid[y]) <= x:
        return None
    return grid[y][x]


def num_occupied_seats(fn):
    def f(grid, x, y):
        return fn(grid, x, y)[OCCUPIED]
    return f


def in_sight(fn):
    return collections.Counter(
        fn(dx, dy)
        for dx in (-1, 0, 1)
        for dy in (-1, 0, 1)
        if (dx, dy) != (0, 0)
    )


def adj(grid, x, y):
    return in_sight(lambda dx, dy: grid_get(grid, x + dx, y + dy))


def visible(grid, x, y):
    return in_sight(lambda dx, dy: seen_in_direction(grid, x, y, dx, dy))


def seen_in_direction(grid, x, y, dx, dy):
    i = 1
    while (val := grid_get(grid, x + i * dx, y + i * dy)) == FLOOR:
        i += 1
    return val


def solver(txt, fn, max_people):
    grid = txt.splitlines()
    last_grid_str = None
    grid_str = txt
    while grid_str != last_grid_str:
        next_grid = []
        for y, row in enumerate(grid):
            next_row = []
            for x, entry in enumerate(row):
                next_entry = entry
                if entry == EMPTY:
                    next_entry = OCCUPIED if fn(grid, x, y) == 0 else EMPTY
                elif entry == OCCUPIED:
                    next_entry = EMPTY if fn(grid, x, y) >= max_people else OCCUPIED
                next_row.append(next_entry)
            next_grid.append("".join(str(x) for x in next_row))
        last_grid_str = grid_str
        grid = next_grid
        grid_str = "\n".join(grid)

    return grid_str.count(OCCUPIED)


def parta(txt):
    return solver(txt, num_occupied_seats(adj), 4)


def partb(txt):
    return solver(txt, num_occupied_seats(visible), 5)


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
