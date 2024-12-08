from collections import Counter, defaultdict
from collections.abc import Callable, Sequence

Path = Sequence[str]
Edges = dict[str, set[str]]


def part_1(txt: str) -> int:
    edges = parse(txt)

    def can_explore(path: Path, cave: str) -> bool:
        return cave.isupper() or cave not in path

    return count_paths(edges, can_explore)


def part_2(txt: str) -> int:
    edges = parse(txt)

    def can_explore(path: Path, cave: str) -> bool:
        if cave.isupper():
            return True
        counts = Counter(path)
        if counts[cave] == 0:
            return True
        visited_any_small_cave_more_than_once = any(counts[c] > 1 for c in counts if c.islower())
        return not visited_any_small_cave_more_than_once

    return count_paths(edges, can_explore)


def parse(txt: str) -> Edges:
    edges = defaultdict(set)
    for begin, end in (line.split("-") for line in txt.splitlines()):
        if end != "start":  # can't go back to start
            edges[begin].add(end)
        if begin != "start":  # can't go back to start
            edges[end].add(begin)
    return edges


def count_paths(edges: Edges, can_explore: Callable[[Path, str], bool]) -> int:
    count = 0
    to_explore: set[Path] = {("start",)}
    while to_explore:
        exploring = to_explore.pop()
        current_pos = exploring[-1]

        if current_pos == "end":
            count += 1
            continue

        for new_pos in edges[current_pos]:
            if can_explore(exploring, new_pos):
                to_explore.add((*exploring, new_pos))

    return count


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
