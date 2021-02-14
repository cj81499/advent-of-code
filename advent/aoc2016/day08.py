from __future__ import annotations

import itertools
import re

ON = True
OFF = False

SCREEN_WIDTH = 50
SCREEN_HEIGHT = 6

NUMBER_REGEX = re.compile(r"(\d+)")


def apply_instruction(screen, instruction):
    A, B = map(int, NUMBER_REGEX.findall(instruction))
    if instruction.startswith("rect "):
        for x, y in itertools.product(range(A), range(B)):
            screen[y][x] = ON
    elif instruction.startswith("rotate row y="):
        new_row = []
        for x in range(len(screen[0])):
            new_row.append(screen[A][(x - B) % len(screen[0])])
        screen[A] = new_row
    elif instruction.startswith("rotate column x="):
        new_col = []
        for y in range(len(screen)):
            new_col.append(screen[(y - B) % len(screen)][A])
        for y in range(len(screen)):
            screen[y][A] = new_col[y]


def create_screen(width=SCREEN_WIDTH, height=SCREEN_HEIGHT):
    return [[OFF for _ in range(width)] for _ in range(height)]


def screen_to_str(screen):
    return "\n".join("".join("#" if c else " " for c in row) for row in screen)


def parta(txt: str):
    screen = create_screen()
    for instruction in txt.splitlines():
        apply_instruction(screen, instruction)
    return sum(v for row in screen for v in row)


def partb(txt: str):
    screen = create_screen()
    for instruction in txt.splitlines():
        apply_instruction(screen, instruction)
    return f"\n{screen_to_str(screen)}"


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
