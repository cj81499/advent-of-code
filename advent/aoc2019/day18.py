from __future__ import annotations

import itertools  # noqa
import re  # noqa
from collections import Counter, defaultdict, deque  # noqa


def next_nodes_a(tunnels, node):
    initial_steps, initial_pos, keys = node
    # search from initial_pos.
    # treat uppercase as wall if we haven't collected their key
    # treat lowercase as empty if we have collected the key, otherwise, yield node
    q = deque()
    seen = set()
    q.append((initial_pos, initial_steps))
    while len(q) > 0:
        pos, steps = q.popleft()
        if pos not in seen:
            at_pos = tunnels.get(pos)
            if at_pos == "@" or at_pos == "." or at_pos in keys \
                    or (at_pos.isupper() and at_pos.lower() in keys):
                q.extend((p, steps + 1) for p in adj(pos))
            elif at_pos.islower():
                yield (steps, pos, "".join(sorted(keys + at_pos)))
            seen.add(pos)


def adj(pos):
    yield pos - 1j
    yield pos + 1
    yield pos + 1j
    yield pos - 1


def parta(txt: str):
    tunnels = get_tunnels(txt)
    start = get_start(tunnels)
    return search(tunnels, start)


def get_tunnels(txt):
    return {
        complex(x, y): c
        for y, row in enumerate(txt.splitlines())
        for x, c in enumerate(row)
    }


def get_start(tunnels):
    positions = [p for p, c in tunnels.items() if c == "@"]
    start_x = sum(p.real for p in positions) / len(positions)
    start_y = sum(p.imag for p in positions) / len(positions)
    return complex(start_x, start_y)


def search(tunnels, start, next_nodes=next_nodes_a):
    num_keys = sum(1 for c in tunnels.values() if c.islower())
    min_steps = float("inf")
    bests = {}
    q = deque()
    q.append((0, start, ""))
    while len(q) > 0:
        node = q.popleft()
        steps, pos, keys = node
        best = bests.get((pos, keys), float("inf"))
        if steps < best:
            bests[(pos, keys)] = steps
            if len(keys) < num_keys:
                q.extend(next_nodes(tunnels, node))
            else:
                min_steps = min(min_steps, steps)
    return min_steps


def next_nodes_b(tunnels, node):
    steps, positions, keys = node
    for i, p in enumerate(positions):
        for n in next_nodes_a(tunnels, (steps, p, keys)):
            n_s, n_p, n_k = n
            new_positions = tuple(p if i != j else n_p for j, p in enumerate(positions))
            yield (n_s, new_positions, n_k)


def partb(txt: str):
    tunnels = get_tunnels(txt)
    start = get_start(tunnels)

    # update the map
    for ((dx, dy), c) in zip(itertools.product(range(-1, 2), repeat=2), "@#@###@#@"):
        tunnels[start + complex(dx, dy)] = c

    starts = tuple((start + d) for d in (-1j-1, -1j+1, 1j+1, 1j-1))
    return search(tunnels, starts, next_nodes=next_nodes_b)


SAMPLE = """
#################
#i.G..c...e..H.p#
####.###.###.####
#j.A..b...f..D.o#
#######.@.#######
#k.E..a...g..B.n#
####.###.###.####
#l.F..d...h..C.m#
#################
""".strip()


def main(txt: str):
    txt = SAMPLE
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
