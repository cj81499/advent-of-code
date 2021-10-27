from __future__ import annotations

from collections import defaultdict

from aoc_cj.aoc2019.intcode_computer import IntcodeProgram


def parta(txt: str):
    x, y = 0, 0
    dx, dy = 0, -1
    panels = defaultdict(int)
    painted = set()
    p = IntcodeProgram.parse(txt)
    while not p.terminated:
        pos = (x, y)
        color = panels[pos]
        p.write_input(color)
        p.run()
        *_, to_paint, turn = p.outputs
        if color != to_paint:
            panels[pos] = to_paint  # paint panel
            painted.add(pos)
        dx, dy = (dy, -dx) if turn == 0 else (-dy, dx)  # turn
        x, y = x + dx, y + dy  # move forward
    return len(painted)


def partb(txt: str):
    x, y = 0, 0
    dx, dy = 0, -1
    panels = defaultdict(int)
    panels[(0, 0)] = 1
    p = IntcodeProgram.parse(txt)
    while not p.terminated:
        pos = (x, y)
        p.write_input(panels[pos])
        p.run()
        *_, to_paint, turn = p.outputs
        panels[pos] = to_paint  # paint panel
        dx, dy = (dy, -dx) if turn == 0 else (-dy, dx)  # turn
        x, y = x + dx, y + dy  # move forward
    white_panels = set(p for p, color in panels.items() if color == 1)
    min_x = min(x for x, _y in white_panels)
    max_x = max(x for x, _y in white_panels)
    min_y = min(y for _x, y in white_panels)
    max_y = max(y for _x, y in white_panels)
    rows = [""]
    for y in range(min_y, max_y + 1):
        row = []
        for x in range(min_x, max_x + 1):
            row.append("#" if (x, y) in white_panels else " ")
        rows.append("".join(row))
    return "\n".join(rows)


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
