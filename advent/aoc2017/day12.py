from __future__ import annotations

import itertools  # noqa
import re  # noqa
from collections import Counter, defaultdict, deque  # noqa
from typing import Dict, Tuple  # noqa


def parse(txt: str):
    m = {}
    for line in txt.splitlines():
        src, destinations = line.split(" <-> ")
        src = int(src)
        destinations = map(int, destinations.split(","))
        m[src] = tuple(destinations)
    return m


def group_containing(connections: Dict[int, Tuple[int, ...]], n: int):
    assert n in connections
    group = set([n])
    prev_size = 0
    while prev_size != len(group):
        prev_size = len(group)
        to_add = set()
        for num in group:
            to_add.update(connections[num])
        group.update(to_add)
    return group


def parta(txt: str):
    return len(group_containing(parse(txt), 0))


def partb(txt: str):
    connections = parse(txt)
    ungrouped = set(connections.keys())
    group_count = 0
    while len(ungrouped) > 0:
        n = ungrouped.pop()
        g = group_containing(connections, n)
        ungrouped.difference_update(g)
        group_count += 1
    return group_count


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
