import heapq
import itertools
import math

import more_itertools as mi
import networkx as nx

from aoc_cj import util


def euclidean_distance(p1: tuple[int, ...], p2: tuple[int, ...]) -> float:
    assert len(p1) == len(p2), "points must be of equal length"
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(p1, p2, strict=True)))


def part_1(txt: str, *, connections: int = 1000) -> int:
    junction_box_positions = {tuple(util.ints(line)) for line in txt.splitlines()}
    pairs = itertools.combinations(junction_box_positions, r=2)

    uf = nx.utils.UnionFind(junction_box_positions)
    for p1, p2 in heapq.nsmallest(connections, pairs, key=lambda pair: euclidean_distance(*pair)):
        uf.union(p1, p2)

    return math.prod(heapq.nlargest(3, (len(sub) for sub in uf.to_sets())))


def part_2(txt: str) -> int:
    junction_box_positions = {tuple(util.ints(line)) for line in txt.splitlines()}
    pairs = itertools.combinations(junction_box_positions, r=2)

    uf = nx.utils.UnionFind(junction_box_positions)
    for p1, p2 in sorted(pairs, key=lambda pair: euclidean_distance(*pair)):
        uf.union(p1, p2)

        # if all points are part of the same circuit (have the same rep)
        if mi.all_equal(uf[p] for p in uf):
            return p1[0] * p2[0]

    assert False, "unreachable"


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
