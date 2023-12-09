import itertools
import math
import re
from typing import Callable

PATTERN = re.compile(r"^(\w+) = \((\w+), (\w+)\)$")

Network = dict[str, tuple[str, str]]


def parse(txt: str) -> tuple[str, Network]:
    sequence, network_s = txt.split("\n\n")
    net: Network = {}
    for l in network_s.splitlines():
        match = PATTERN.match(l)
        assert match is not None
        pos, left, right = match.groups()
        net[pos] = (left, right)
    return sequence, net


def navigate(
    sequence: str,
    network: Network,
    start: str = "AAA",
    is_end: Callable[[str], bool] = lambda p: p == "ZZZ",
) -> int:
    seq = itertools.cycle(sequence)
    pos = start
    steps = 0
    while not is_end(pos):
        move = next(seq)
        if move == "L":
            pos = network[pos][0]
        elif move == "R":
            pos = network[pos][1]
        else:
            assert False, f"move must be 'L' or 'R' but was {move}"
        steps += 1
    return steps


def parta(txt: str) -> int:
    sequence, network = parse(txt)
    return navigate(sequence, network)


def partb(txt: str) -> int:
    sequence, network = parse(txt)
    positions = (k for k in network if k.endswith("A"))
    steps_taken = (navigate(sequence, network, start=p, is_end=lambda p: p.endswith("Z")) for p in positions)
    return math.lcm(*steps_taken)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
