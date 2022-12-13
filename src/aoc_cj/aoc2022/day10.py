from collections import deque
from collections.abc import Generator
from typing import Optional

MAX_CYCLE = 240


def parta(txt: str) -> int:
    return sum(cycle * x for cycle, x in helper(txt) if (cycle - 20) % 40 == 0)


def helper(txt: str) -> Generator[tuple[int, int], None, None]:
    X = 1
    running: Optional[tuple[str, int, int]] = None

    lines = deque(txt.splitlines())
    for cycle in range(1, MAX_CYCLE + 1):
        # start of cycle
        # if nothing is running and there are more instructions to run
        if running is None and lines:
            instruction = lines.popleft()

            if instruction == "noop":
                running = ("noop", 0, 1)
            elif instruction.startswith("addx"):
                _, n = instruction.split()
                running = ("addx", int(n), 2)

        # during the cycle
        yield cycle, X

        # after the cycle, cmds finish execution
        if running is not None:
            op, num, duration = running
            if duration == 1:
                X += num
                running = None
            else:
                running = (op, num, duration - 1)


def partb(txt: str) -> str:
    lines = []
    row = []
    for cycle, X in helper(txt):
        row_idx = (cycle - 1) % 40
        is_lit = abs(row_idx - X) < 2
        row.append("#" if is_lit else ".")
        if cycle % 40 == 0:
            lines.append("".join(row))
            row.clear()

    return "\n".join(lines)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
