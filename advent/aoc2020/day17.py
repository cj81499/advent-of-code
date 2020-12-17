import collections  # noqa
import itertools  # noqa
import re  # noqa

ACTIVE = "#"
INACTIVE = "."


def neighbors3D(pos):
    deltas = (-1, 0, 1)
    x, y, z = pos
    return ((x + dx, y + dy, z + dz) for dx in deltas for dy in deltas for dz in deltas if (dx, dy, dz) != (0, 0, 0))


def neighbors4D(pos):
    deltas = (-1, 0, 1)
    w, x, y, z = pos
    return ((w + dw, x + dx, y + dy, z + dz) for dw in deltas for dx in deltas for dy in deltas for dz in deltas if (dw, dx, dy, dz) != (0, 0, 0, 0))


def parta(txt):
    space = collections.defaultdict(lambda: INACTIVE)
    for y, row in enumerate(txt.splitlines()):
        for x, c in enumerate(row):
            space[(x, y, 0)] = c

    for _ in range(6):
        points_to_consider = []
        for p in space:
            points_to_consider.extend(neighbors3D(p))
        new_space = collections.defaultdict(lambda: INACTIVE)
        for p in points_to_consider:
            active_neighbors = sum(space[n] == ACTIVE for n in neighbors3D(p))
            if space[p] == ACTIVE:
                new_space[p] = ACTIVE if active_neighbors in (2, 3) else INACTIVE
            else:
                new_space[p] = ACTIVE if active_neighbors == 3 else INACTIVE
        space = new_space

    return sum(v == ACTIVE for v in new_space.values())


def partb(txt):
    space = collections.defaultdict(lambda: INACTIVE)
    for y, row in enumerate(txt.splitlines()):
        for x, c in enumerate(row):
            space[(0, x, y, 0)] = c

    for _ in range(6):
        points_to_consider = []
        for p in space:
            points_to_consider.extend(neighbors4D(p))
        new_space = collections.defaultdict(lambda: INACTIVE)
        for p in points_to_consider:
            active_neighbors = sum(space[n] == ACTIVE for n in neighbors4D(p))
            if space[p] == ACTIVE:
                new_space[p] = ACTIVE if active_neighbors in (2, 3) else INACTIVE
            else:
                new_space[p] = ACTIVE if active_neighbors == 3 else INACTIVE
        space = new_space

    return sum(v == ACTIVE for v in new_space.values())


def main(txt):
    #     txt = """
    # .#.
    # ..#
    # ###
    # """.strip()
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
