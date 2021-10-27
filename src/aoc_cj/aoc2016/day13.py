from __future__ import annotations

from collections import deque


def is_open(x, y, fav_num):
    n = x * x + 3 * x + 2 * x * y + y + y * y + fav_num
    num_ones = bin(n).count("1")
    return num_ones % 2 == 0


def parta(txt: str, target_pos=(31, 39)):
    return solve(txt, target_pos=target_pos)


def partb(txt: str):
    return solve(txt, max_steps=50)


def solve(txt, target_pos=None, max_steps=None):
    fav_num = int(txt)
    q = deque([(1, 1, 0)])  # (x, y, steps)
    seen = set()
    while len(q) > 0:
        x, y, steps = q.popleft()
        if (x, y) in seen or (max_steps is not None and steps > max_steps):
            continue
        if target_pos is not None and (x, y) == target_pos:
            return steps
        new_points = ((x + dx, y + dy) for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)))
        new_points = ((x, y) for x, y in new_points if x >= 0 and y >= 0)
        q.extend((x, y, steps + 1) for x, y in new_points if is_open(x, y, fav_num))
        seen.add((x, y))
    return -1 if max_steps is None else len(seen)


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
