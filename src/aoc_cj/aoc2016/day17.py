import hashlib
import itertools
from collections import deque
from collections.abc import Generator


def is_open(passcode: str, path: str) -> tuple[bool, ...]:
    hd = hashlib.md5(f"{passcode}{path}".encode()).hexdigest()
    return tuple(not x.isnumeric() and x != "a" for x in hd[:4])


GRID_SIZE = 4
MOVES = {"U": -1j, "D": 1j, "L": -1, "R": 1}


def paths(passcode: str) -> Generator[str]:
    GOAL = complex(GRID_SIZE - 1, GRID_SIZE - 1)
    q = deque[tuple[complex, str]]()
    q.append((0 + 0j, ""))
    while len(q) > 0:
        pos, path = q.popleft()
        if not (0 <= pos.real < GRID_SIZE and 0 <= pos.imag < GRID_SIZE):
            continue
        if pos == GOAL:
            yield path
        else:
            for direction in itertools.compress("UDLR", is_open(passcode, path)):
                next_pos: complex = pos + MOVES[direction]
                next_path: str = path + direction
                q.append((next_pos, next_path))


def part_1(txt: str) -> str | None:
    try:
        return next(paths(txt))
    except StopIteration:
        return None


def part_2(txt: str) -> int:
    return len(list(paths(txt))[-1])


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
