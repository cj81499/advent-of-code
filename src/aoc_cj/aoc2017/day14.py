from collections import deque

from aoc_cj.aoc2017.day10 import knot_hash

GRID_SIZE = 128


def binary_knot_hash(txt: str):
    return bin(int(knot_hash(txt), 16))[2:].zfill(GRID_SIZE)


def part_1(txt: str):
    return sum(binary_knot_hash(f"{txt}-{i}").count("1") for i in range(GRID_SIZE))


def adj_pos(p):
    x, y = p
    yield from ((x + dx, y + dy) for (dx, dy) in ((0, -1), (1, 0), (0, 1), (-1, 0)))


def part_2(txt: str):
    not_in_group = {(x, y) for y in range(GRID_SIZE) for x, c in enumerate(binary_knot_hash(f"{txt}-{y}")) if c == "1"}
    group_count = 0
    q = deque()
    while len(not_in_group) > 0:
        q.append(not_in_group.pop())
        while len(q) > 0:
            pos = q.popleft()
            for adj in (p for p in adj_pos(pos) if p in not_in_group):
                q.append(adj)
                not_in_group.remove(adj)
        group_count += 1
    return group_count


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
