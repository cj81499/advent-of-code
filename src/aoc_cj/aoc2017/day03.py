import itertools


def part_1(txt):
    n = int(txt)
    memory = set()
    x, y = 0, 0
    dx, dy = 0, 1
    for i in range(1, n):
        memory.add((x, y))

        # rotate heading if we can move after rotating ccw
        turned_x, turned_y = x + dy, y - dx
        if not (turned_x, turned_y) in memory:
            dx, dy = dy, -dx

        # calculate new position
        x += dx
        y += dy

    return abs(x) + abs(y)


def part_2(txt):
    n = int(txt)
    memory = {}
    x, y = 0, 0
    dx, dy = 0, 1
    val = 1
    while val <= n:
        memory[(x, y)] = val = (
            1
            if (x, y) == (0, 0)
            else sum(
                memory.get((x + dx, y + dy), 0)
                for dx, dy in itertools.product((-1, 0, 1), repeat=2)
                if (dx, dy) != (0, 0)
            )
        )

        # rotate heading if we can move after rotating ccw
        turned_x, turned_y = x + dy, y - dx
        if not (turned_x, turned_y) in memory:
            dx, dy = dy, -dx

        # calculate new position
        x += dx
        y += dy

    return val


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
