from collections import deque


def is_open(x: int, y: int, fav_num: int) -> bool:
    n = x * x + 3 * x + 2 * x * y + y + y * y + fav_num
    num_ones = (n).bit_count()
    return num_ones % 2 == 0


def part_1(txt: str, target_pos: tuple[int, int] = (31, 39)) -> int:
    return solve(txt, target_pos=target_pos)


def part_2(txt: str) -> int:
    return solve(txt, max_steps=50)


def solve(txt: str, target_pos: tuple[int, int] | None = None, max_steps: int | None = None) -> int:
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


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
