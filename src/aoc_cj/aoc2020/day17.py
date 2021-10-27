import collections
import itertools

ACTIVE = "#"
INACTIVE = "."


def neighbors(pos):
    for delta in itertools.product(*itertools.repeat((-1, 0, 1), len(pos))):
        if not all(x == 0 for x in delta):
            yield tuple(x + dx for x, dx in zip(pos, delta))


def simulate(txt, dimensions):
    # initialize space
    space = collections.defaultdict(lambda: INACTIVE)
    space.update(
        {
            (x, y, *itertools.repeat(0, dimensions - 2)): c
            for y, row in enumerate(txt.splitlines())
            for x, c in enumerate(row)
        }
    )

    # run 6 iterations of the simulation
    for _ in range(6):
        # get min and max coordinates
        mins, maxes = minmax_tuple(set(space))
        # count active neighbors for each position
        active_neighbors = collections.defaultdict(int)
        for p in expand_points(mins, maxes):
            if space[p] == ACTIVE:
                for n in neighbors(p):
                    active_neighbors[n] += 1

        # calculate the contents of the new space
        new_space = collections.defaultdict(lambda: INACTIVE)
        new_space.update(
            {
                p: ACTIVE
                for p in expand_points(mins, maxes)
                if active_neighbors[p] == 3 or (active_neighbors[p] == 2 and space[p] == ACTIVE)
            }
        )
        space = new_space

    return sum(v == ACTIVE for v in new_space.values())


def minmax_tuple(tuples):
    return tuple(min(x) for x in zip(*tuples)), tuple(max(x) for x in zip(*tuples))


def expand_points(mins, maxes):
    assert len(mins) == len(maxes)
    return itertools.product(*(range(start - 1, stop + 2) for start, stop in zip(mins, maxes)))


def parta(txt):
    return simulate(txt, 3)


def partb(txt):
    return simulate(txt, 4)


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
