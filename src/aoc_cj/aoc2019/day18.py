import itertools
from collections import deque

from aoc_cj.util.priority_queue import PriorityQueue


def parse(txt: str):
    grid = {complex(x, y): c for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line)}

    start_pos = next(p for p, c in grid.items() if c == "@")
    num_keys = sum(1 for c in grid.values() if c.islower())
    return grid, start_pos, num_keys


def next_states_a(grid, state):
    steps, pos, collected = state
    q = deque()
    q.append((pos, steps))
    seen = set()
    while len(q) > 0:
        pos, steps = q.popleft()
        if pos in seen:
            continue
        val: str = grid.get(pos)
        if val in ".@" or val.lower() in collected:
            q.extend((pos + delta, steps + 1) for delta in (-1j, 1, 1j, -1))
        elif val != "#" and val.islower():
            yield (steps, pos, frozenset((*collected, val)))
        seen.add(pos)


def next_states_b(grid, state):
    steps, positions, collected = state
    for i, pos in enumerate(positions):
        for s in next_states_a(grid, (steps, pos, collected)):
            new_steps, new_pos, new_collected = s
            new_positions = list(positions)
            new_positions[i] = new_pos
            yield (new_steps, tuple(new_positions), new_collected)


def search(initial, num_keys, grid, next_states=next_states_a):
    q = PriorityQueue()
    q.push(0, initial)
    seen = set()
    while len(q) > 0:
        state = q.pop()
        steps, pos, collected = state
        if len(collected) == num_keys:
            return steps
        if (pos, collected) in seen:
            continue
        for s in next_states(grid, state):
            q.push(s[0], s)
        seen.add((pos, collected))
    return -1


def parta(txt: str):
    grid, start_pos, num_keys = parse(txt)
    initial = (0, start_pos, frozenset())
    return search(initial, num_keys, grid)


def partb(txt: str):
    grid, start_pos, num_keys = parse(txt)

    # update the cave entrance
    replace = "@#@\n###\n@#@".splitlines()
    for x, y in itertools.product(range(3), repeat=2):
        grid[start_pos + complex(x - 1, y - 1)] = replace[y][x]

    initial = (0, tuple(start_pos + delta for delta in (-1 - 1j, 1 - 1j, 1 + 1j, -1 + 1j)), frozenset())
    return search(initial, num_keys, grid, next_states_b)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
