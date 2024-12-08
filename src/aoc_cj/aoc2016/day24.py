import itertools
from collections import deque

WALL = "#"
OPEN = "."

Pos = tuple[int, int]
Grid = dict[Pos, str]


def is_wall(grid: Grid, pos: Pos):
    return grid.get(pos, WALL) == WALL


def adj_pos(x: int, y: int):
    yield from ((x + dx, y + dy) for (dx, dy) in ((0, -1), (0, 1), (-1, 0), (1, 0)))


def path_distance(edges, possible_path):
    return sum(edges[tuple(sorted(pair))] for pair in itertools.pairwise(possible_path))


def possible_paths(num_targets, end_at_start=False):
    yield from ((0, *perm, 0) if end_at_start else (0, *perm) for perm in itertools.permutations(range(1, num_targets)))


def helper(txt: str, end_at_start=False):
    grid = {(x, y): c for y, line in enumerate(txt.splitlines()) for x, c in enumerate(line)}

    def distance_between(start: Pos, end: Pos):
        # dfs from start to end
        q = deque()
        q.append((0, start))
        seen = set()
        while q:
            distance, pos = q.popleft()
            if pos == end:
                return distance
            if pos not in seen:
                q.extend((distance + 1, p) for p in adj_pos(*pos) if not is_wall(grid, p))
                seen.add(pos)
        raise RuntimeError(f"{end} is not reachable from {start}")

    locations = {int(c): p for p, c in grid.items() if c.isnumeric()}

    # find shortest path from each target to each other target
    edges = {
        tuple(sorted((n1, n2))): distance_between(p1, p2)
        for ((n1, p1), (n2, p2)) in itertools.combinations(locations.items(), 2)
    }

    num_locations = len(locations)

    return min(path_distance(edges, p) for p in possible_paths(num_locations, end_at_start))


def part_1(txt: str):
    return helper(txt)


def part_2(txt: str):
    return helper(txt, end_at_start=True)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
