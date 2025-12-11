import heapq
import itertools
import math

import more_itertools as mi

from aoc_cj import util


def euclidean_distance(p1: tuple[int, ...], p2: tuple[int, ...]) -> float:
    assert len(p1) == len(p2), "points must be of equal length"
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(p1, p2, strict=True)))


def part_1(txt: str, *, connections: int = 1000) -> int:
    junction_boxes = {tuple(util.ints(line)) for line in txt.splitlines()}
    circuits = {p: frozenset((p,)) for p in junction_boxes}
    box_pairs = itertools.combinations(junction_boxes, r=2)

    for p1, p2 in heapq.nsmallest(connections, box_pairs, key=lambda pair: euclidean_distance(*pair)):
        # merge circuits
        merged = circuits[p1] | circuits[p2]
        for p in merged:
            circuits[p] = merged

    return math.prod(len(c) for c in heapq.nlargest(3, frozenset(circuits.values()), key=len))


def part_2(txt: str) -> int:
    junction_boxes = {tuple(util.ints(line)) for line in txt.splitlines()}
    circuits = {p: frozenset((p,)) for p in junction_boxes}
    box_pairs = itertools.combinations(junction_boxes, r=2)

    for p1, p2 in sorted(box_pairs, key=lambda pair: euclidean_distance(*pair)):
        # merge circuits
        merged = circuits[p1] | circuits[p2]
        for p in merged:
            circuits[p] = merged

        # if all points are part of the same circuit
        if mi.all_equal(circuits.values()):
            return p1[0] * p2[0]

    msg = "unreachable"
    raise AssertionError(msg)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
