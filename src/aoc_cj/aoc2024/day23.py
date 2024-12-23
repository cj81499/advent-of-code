from collections import defaultdict
from collections.abc import Mapping

import networkx as nx

Connections = Mapping[str, set[str]]


def part_1(txt: str) -> int:
    connections = _parse_connections(txt)

    groups = {
        frozenset((c1, c2, c3))
        for c1, c1_connected_to in connections.items()
        for c2 in c1_connected_to
        for c3 in c1_connected_to & connections[c2]
    }

    groups_with_chief_historian = {g for g in groups if any(c.startswith("t") for c in g)}

    return len(groups_with_chief_historian)


def part_2(txt: str) -> str:
    connections = _parse_connections(txt)

    # g = nx.Graph(connections)  # this works at runtime, but the type annotations for networkx are wrong :(  # noqa: ERA001
    g = nx.Graph((c1, c2) for c1, c1_conns in connections.items() for c2 in c1_conns)

    # https://networkx.org/documentation/stable/reference/algorithms/clique.html
    biggest_clique = max(nx.find_cliques(g), key=len)

    return ",".join(sorted(biggest_clique))


def _parse_connections(txt: str) -> Connections:
    connections = defaultdict[str, set[str]](set)
    for line in txt.splitlines():
        l, sep, r = line.partition("-")
        assert sep == "-"
        connections[l].add(r)
        connections[r].add(l)
    return connections


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
