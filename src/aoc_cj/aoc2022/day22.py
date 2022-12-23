from collections.abc import Generator
from typing import Union

import more_itertools as mi

OPEN = "."
WALL = "#"

RIGHT = complex(1, 0)
DOWN = complex(0, 1)
LEFT = complex(-1, 0)
UP = complex(0, -1)

FACING_TO_INT = {RIGHT: 0, DOWN: 1, LEFT: 2, UP: 3}


def parse_map_path(path: str) -> Generator[Union[int, str], None, None]:
    for chunk in mi.split_when(path, lambda x, y: x.isnumeric() != y.isnumeric()):
        joined = "".join(chunk)
        yield int(joined) if joined.isnumeric() else joined


def parta(txt: str) -> int:
    board_map_s, path = txt.split("\n\n")

    board_map = {
        complex(x, y): c
        for y, line in enumerate(board_map_s.splitlines())
        for x, c in enumerate(line)
        if c in {OPEN, WALL}
    }

    # You begin the path in the leftmost open tile of the top row of tiles.
    current_pos = min((p for p, c in board_map.items() if c == OPEN and p.imag == 0), key=lambda p: p.real)
    # Initially, you are facing to the right (from the perspective of how the map is drawn).
    facing = complex(1, 0)

    for step in parse_map_path(path):
        if isinstance(step, int):
            for _ in range(step):
                new_pos = current_pos + facing
                # handle wraparound
                if new_pos not in board_map:
                    if facing == RIGHT:
                        new_pos = min((p for p in board_map if p.imag == current_pos.imag), key=lambda p: p.real)
                    elif facing == DOWN:
                        new_pos = min((p for p in board_map if p.real == current_pos.real), key=lambda p: p.imag)
                    elif facing == LEFT:
                        new_pos = max((p for p in board_map if p.imag == current_pos.imag), key=lambda p: p.real)
                    elif facing == UP:
                        new_pos = max((p for p in board_map if p.real == current_pos.real), key=lambda p: p.imag)
                    else:
                        assert False, "unreachable"
                # if new_pos is a wall
                if board_map.get(new_pos) == WALL:
                    break
                current_pos = new_pos
        elif step == "L":
            facing = complex(facing.imag, -facing.real)  # turn CCW
        elif step == "R":
            facing = complex(-facing.imag, facing.real)  # turn CW
        else:
            assert False, "unreachable"

    row = int(current_pos.imag) + 1
    col = int(current_pos.real) + 1
    return 1000 * row + 4 * col + FACING_TO_INT[facing]


def partb(txt: str) -> int:
    board_map_s, path = txt.split("\n\n")

    board_map = {
        complex(x, y): c
        for y, line in enumerate(board_map_s.splitlines())
        for x, c in enumerate(line)
        if c in {OPEN, WALL}
    }

    # You begin the path in the leftmost open tile of the top row of tiles.
    current_pos = min((p for p, c in board_map.items() if c == OPEN and p.imag == 0), key=lambda p: p.real)
    # Initially, you are facing to the right (from the perspective of how the map is drawn).
    facing = complex(1, 0)

    lines = board_map_s.splitlines()
    edge_length = min(*(len(row.strip()) for row in lines), *(len("".join(col).strip()) for col in zip(lines)))

    shape = {p2 for p in board_map.keys() if (p2 := p / edge_length).real.is_integer() and p2.imag.is_integer()}

    raise NotImplementedError()


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
