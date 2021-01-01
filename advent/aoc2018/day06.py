from collections import Counter


def try_set_grid(grid, x, y, value):
    if x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid):
        if grid[y][x] == -1:
            grid[y][x] = set()
            grid[y][x].add(value)
        elif isinstance(grid[y][x], set):
            grid[y][x].add(value)
    else:
        return False
    return True


def set_to_entry(grid, x, y):
    if x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid):
        if isinstance(grid[y][x], set):
            if len(grid[y][x]) > 1:
                grid[y][x] = -2
            else:
                grid[y][x] = grid[y][x].pop()


def expand(grid, seeds):
    filled_in = False
    dist = 0
    while not filled_in:
        dist += 1
        for s in seeds:
            x, y = s
            for x_mod in range(dist + 1):
                y_mod = dist - x_mod
                try_set_grid(grid, x + x_mod, y + y_mod, grid[y][x])
                try_set_grid(grid, x - x_mod, y + y_mod, grid[y][x])
                try_set_grid(grid, x + x_mod, y - y_mod, grid[y][x])
                try_set_grid(grid, x - x_mod, y - y_mod, grid[y][x])
        for s in seeds:
            x, y = s
            for x_mod in range(dist + 1):
                y_mod = dist - x_mod
                set_to_entry(grid, x + x_mod, y + y_mod)
                set_to_entry(grid, x - x_mod, y + y_mod)
                set_to_entry(grid, x + x_mod, y - y_mod)
                set_to_entry(grid, x - x_mod, y - y_mod)
        filled_in = all([True if -1 not in row else False for row in grid])


def parta(txt):
    lines = txt.splitlines()
    max_x, max_y = 0, 0
    seeds = set()
    for line in lines:
        x, y = [int(x) for x in line.split(", ")]
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    grid = [[-1 for x in range(max_x + 2)] for y in range(max_y + 2)]
    i = 1
    for line in lines:
        x, y = [int(x) for x in line.split(", ")]
        grid[y][x] = i
        seeds.add((x, y))
        i += 1

    expand(grid, seeds)

    disqualified = set()
    items_in_first_row = grid[0]
    items_in_last_row = grid[len(grid) - 1]
    items_in_first_col = [r[0] for r in grid]
    items_in_last_col = [r[len(r) - 1] for r in grid]
    disqualified.update(items_in_first_row, items_in_last_row,
                        items_in_first_col, items_in_last_col)

    flat_grid = [item for row in grid for item in row]

    count = Counter(flat_grid)
    valid = set(count) - disqualified
    max_area_size = 0
    for i in valid:
        if count[i] > max_area_size:
            max_area_size = count[i]
    return max_area_size


def dist_to_seed(x, y, seed):
    return abs(seed[0] - x) + abs(seed[1] - y)


def partb(txt, region_dist=10000):
    seeds = set()
    max_x, max_y = 0, 0
    for line in txt.splitlines():
        x, y = [int(x) for x in line.split(", ")]
        seeds.add((x, y))
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    within_region_count = 0
    for y in range(max_y):
        for x in range(max_x):
            total_dist = 0
            for s in seeds:
                total_dist += dist_to_seed(x, y, s)
            if total_dist < region_dist:
                within_region_count += 1
    return within_region_count


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
