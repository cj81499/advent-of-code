import contextlib
import itertools
from collections.abc import Generator

import more_itertools as mi

_DIRECTIONS = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)


def ray(lines: list[str], x: int, y: int, dx: int, dy: int) -> Generator[str]:
    for i in itertools.count():
        new_y = y + dy * i
        new_x = x + dx * i
        if new_y < 0 or new_x < 0:
            return
        try:
            yield lines[new_y][new_x]
        except IndexError:
            return


def part_1(txt: str) -> int:
    lines = txt.splitlines()
    return sum(
        1
        for y, row in enumerate(lines)
        for x, c in enumerate(row)
        if c == "X"
        for dy, dx in _DIRECTIONS
        if "".join(mi.take(4, ray(lines, x, y, dx, dy))) == "XMAS"
    )


def is_x_dash_mas(lines: list[str], x: int, y: int) -> bool:
    c = lines[y][x]
    if c != "A":
        return False
    if x - 1 < 0 or y - 1 < 0:
        return False
    with contextlib.suppress(IndexError):
        top_left = lines[y - 1][x - 1]
        top_right = lines[y - 1][x + 1]
        bottom_left = lines[y + 1][x - 1]
        bottom_right = lines[y + 1][x + 1]
        return top_left + bottom_right in ("MS", "SM") and top_right + bottom_left in ("MS", "SM")
    return False


def part_2(txt: str) -> int:
    lines = txt.splitlines()
    return sum(1 for y, row in enumerate(lines) for x, _c in enumerate(row) if is_x_dash_mas(lines, x, y))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
