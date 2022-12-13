import itertools

Bug = tuple[int, ...]
Bugs = frozenset[Bug]


def str_to_bugs(s: str, recursive=False) -> Bugs:
    bugs = {
        (x, y, 0) if recursive else (x, y)
        for y, line in enumerate(s.splitlines())
        for x, c in enumerate(line)
        if c == "#"
    }
    if recursive:
        bugs.discard((2, 2, 0))
    return frozenset(bugs)


def parta(txt: str):
    bugs: Bugs = str_to_bugs(txt)
    repeat = first_repeat(bugs)
    return biodiversity(repeat)


def first_repeat(bugs: Bugs) -> Bugs:
    seen = set()
    while bugs not in seen:
        seen.add(bugs)
        bugs = step(bugs)
    return bugs


def should_add_bug(is_bug, adj_count):
    return (is_bug and adj_count == 1) or (not is_bug and adj_count in (1, 2))


def step(bugs: Bugs) -> Bugs:
    new_bugs = set()
    for x, y in itertools.product(range(5), repeat=2):
        p = (x, y)
        is_bug = p in bugs
        adj_count = sum(1 for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)) if (x + dx, y + dy) in bugs)
        if should_add_bug(is_bug, adj_count):
            new_bugs.add(p)
    return frozenset(new_bugs)


def biodiversity(bugs: Bugs) -> int:
    return sum(2 ** (5 * y + x) for x, y in bugs)


def partb(txt: str, minutes=200):
    bugs: Bugs = str_to_bugs(txt, recursive=True)
    for _ in range(minutes):
        bugs = step_recursive(bugs)
    return len(bugs)


def adj_count_recursive(bugs, pos: Bug):
    x, y, z = pos
    adj_count = sum(1 for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)) if (x + dx, y + dy, z) in bugs)

    # check outer edge of layer
    adj_count += 1 if x == 0 and (1, 2, z - 1) in bugs else 0
    adj_count += 1 if x == 4 and (3, 2, z - 1) in bugs else 0
    adj_count += 1 if y == 0 and (2, 1, z - 1) in bugs else 0
    adj_count += 1 if y == 4 and (2, 3, z - 1) in bugs else 0

    # check inside
    adj_count += 0 if (x, y) != (2, 1) else sum(1 for inner_x in range(5) if (inner_x, 0, z + 1) in bugs)
    adj_count += 0 if (x, y) != (2, 3) else sum(1 for inner_x in range(5) if (inner_x, 4, z + 1) in bugs)
    adj_count += 0 if (x, y) != (1, 2) else sum(1 for inner_y in range(5) if (0, inner_y, z + 1) in bugs)
    adj_count += 0 if (x, y) != (3, 2) else sum(1 for inner_y in range(5) if (4, inner_y, z + 1) in bugs)

    return adj_count


def step_recursive(bugs: Bugs) -> Bugs:
    new_bugs = set()
    min_z = min(z for _x, _y, z in bugs)
    max_z = max(z for _x, _y, z in bugs)
    for z in range(min_z - 1, max_z + 2):
        for x, y in itertools.product(range(5), repeat=2):
            if (x, y) != (2, 2):  # the middle (2,2) can't be a bug. it is a recursive space.
                p = (x, y, z)
                is_bug = p in bugs
                adj_count = adj_count_recursive(bugs, p)
                if should_add_bug(is_bug, adj_count):
                    new_bugs.add(p)
    return frozenset(new_bugs)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
