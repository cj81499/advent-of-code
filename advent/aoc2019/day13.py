from __future__ import annotations

from collections import Counter

from advent.aoc2019.intcode_computer import IntcodeProgram


def chunk(li: list, n: int):
    yield from (li[i:i+n] for i in range(0, len(li), n))


def parta(txt: str):
    screen = {}
    p = IntcodeProgram.parse(txt)
    p.run()
    for x, y, tile_id in chunk([*p.outputs], 3):
        screen[(x, y)] = tile_id
    return Counter(screen.values())[2]


def screen_corners(screen):
    min_x = min(x for x, y in screen.keys())
    max_x = max(x for x, y in screen.keys())
    min_y = min(y for x, y in screen.keys())
    max_y = max(y for x, y in screen.keys())
    return min_x, max_x, min_y, max_y


DISPLAY_CHAR_MAP = {0: " ", 1: "█", 2: "#", 3: "─", 4: "o"}


def display(screen, score):
    min_x, max_x, min_y, max_y = screen_corners(screen)
    rows = []
    for y in range(min_y, max_y + 1):
        row = []
        for x in range(min_x, max_x + 1):
            c = DISPLAY_CHAR_MAP[screen[(x, y)]]
            row.append(c)
        rows.append("".join(row))
    screen_str = "\n".join(rows)
    return f"{screen_str}\nScore: {score}"


def partb(txt: str):
    screen = {}
    score = None
    p = IntcodeProgram.parse(txt)
    p[0] = 2
    ball_x, paddle_x = None, None
    while not p.terminated:
        p.run_next()
        if len(p.outputs) > 0 and len(p.outputs) % 3 == 0:
            x, y, tile_id = (p.outputs.popleft() for _ in range(3))
            if (x, y) == (-1, 0):
                score = tile_id
            else:
                screen[(x, y)] = tile_id
                if tile_id == 4:
                    ball_x = x
                elif tile_id == 3:
                    paddle_x = x
        if p.is_waiting_for_input():
            # print(display(screen, score))
            joystick = 0
            if ball_x != paddle_x:
                joystick = 1 if ball_x > paddle_x else -1
            p.write_input(joystick)
    return score


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
