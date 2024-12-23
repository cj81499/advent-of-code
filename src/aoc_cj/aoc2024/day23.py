import networkx as nx


def part_1(txt: str) -> int:
    g = _parse_graph(txt)
    groups = {frozenset((cpu1, cpu2, cpu3)) for cpu1 in g for cpu2 in g[cpu1] for cpu3 in g[cpu1].keys() & g[cpu2]}
    groups_with_chief_historian = {g for g in groups if any(c.startswith("t") for c in g)}
    return len(groups_with_chief_historian)


def part_2(txt: str) -> str:
    g = _parse_graph(txt)
    # https://networkx.org/documentation/stable/reference/algorithms/clique.html
    biggest_clique = max(nx.find_cliques(g), key=len)
    return ",".join(sorted(biggest_clique))


def _parse_graph(txt: str) -> "nx.Graph[str]":
    return nx.Graph(map(_parse_line, txt.splitlines()))


def _parse_line(line: str) -> tuple[str, str]:
    l, sep, r = line.partition("-")
    assert sep == "-"
    return l, r


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
