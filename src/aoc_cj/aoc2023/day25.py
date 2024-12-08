import math

import networkx as nx


def part_1(txt: str) -> int:
    """
    With help from https://github.com/thecae/advent-of-code/blob/main/Python/2023/day25.py

    TIL about min-cut! https://en.wikipedia.org/wiki/Minimum_cut
    """

    graph: nx.Graph[str] = nx.Graph()
    for line in txt.splitlines():
        lhs, sep, rhs = line.partition(": ")
        assert sep == ": "
        rhs_components = rhs.split(" ")
        for component in rhs_components:
            graph.add_edge(lhs, component)

    cuts = nx.minimum_edge_cut(graph)
    assert len(cuts) == 3
    graph.remove_edges_from(cuts)

    return math.prod(len(c) for c in nx.connected_components(graph))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
