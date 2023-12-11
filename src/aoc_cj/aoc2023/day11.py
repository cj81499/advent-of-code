import itertools

import more_itertools as mi

Pos = tuple[int, int]


# TODO: man_dist in utils
def man_dist(p1: Pos, p2: Pos) -> int:
    p1x, p1y = p1
    p2x, p2y = p2
    return abs(p1x - p2x) + abs(p1y - p2y)


def parta(txt: str, *, _expand_by: int = 1) -> int:
    grid = {(x, y): c for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line)}
    galaxies = {p for p, c in grid.items() if c == "#"}

    empty_rows = {y for _x, y in grid}
    empty_cols = {x for x, _y in grid}
    for g_x, g_y in galaxies:
        empty_rows.discard(g_y)
        empty_cols.discard(g_x)

    total_dist = 0
    for g1, g2 in itertools.combinations(galaxies, 2):
        min_y, max_y = mi.minmax((g1[1], g2[1]))
        min_x, max_x = mi.minmax((g1[0], g2[0]))
        num_empty_rows_between = sum(_expand_by for row_i in empty_rows if min_y < row_i < max_y)
        num_empty_cols_between = sum(_expand_by for col_i in empty_cols if min_x < col_i < max_x)
        dist = man_dist(g1, g2) + num_empty_rows_between + num_empty_cols_between
        total_dist += dist
    return total_dist


def partb(txt: str, *, expand_by: int = 1_000_000) -> int:
    return parta(txt, _expand_by=expand_by - 1)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
