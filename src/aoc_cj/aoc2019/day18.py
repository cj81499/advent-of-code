import dataclasses
import heapq
import math
from collections import deque

import more_itertools as mi

from aoc_cj import util

type Grid = dict[complex, str]


@dataclasses.dataclass(order=True, frozen=True)
class HeapEntry:
    pos: tuple[complex, ...] = dataclasses.field(compare=False)
    dist: int = 0
    collected: frozenset[str] = dataclasses.field(compare=False, default_factory=frozenset)


def bfs_from(src: complex, grid: Grid) -> dict[complex, tuple[int, set[str]]]:
    q = deque([(src, 0)])
    seen: set[complex] = {src}
    found: dict[complex, tuple[int, set[str]]] = {}
    doors_on_path: dict[complex, set[str]] = {src: set()}

    while q:
        p, dist = q.popleft()
        cur_doors = doors_on_path[p]
        ch = grid.get(p, "#")
        if ch.islower() and p != src:
            found[p] = (dist, set(cur_doors))

        for nb in util.adj_4(p):
            if nb in seen:
                continue
            c = grid.get(nb, "#")
            if c == "#":
                continue
            seen.add(nb)
            nd = set(cur_doors)
            if c.isupper():
                nd.add(c)
            doors_on_path[nb] = nd
            q.append((nb, dist + 1))

    return found


def part_1(txt: str) -> int:
    grid = {complex(x, y): c for y, row in enumerate(txt.splitlines()) for x, c in enumerate(row)}
    key_positions = {c: pos for pos, c in grid.items() if c.islower()}
    start_pos = mi.one(pos for pos, c in grid.items() if c == "@")

    # map positions (start + keys) to reachable keys with distance and required doors
    nodes = {
        pos: {key_pos: (dist, req_doors) for key_pos, (dist, req_doors) in bfs_from(pos, grid).items()}
        for pos in (*key_positions.values(), start_pos)
    }

    total_keys = frozenset(key_positions.keys())

    # Dijkstra over state (pos, collected_keys)
    # store single position in a 1-tuple to keep HeapEntry.pos consistent type
    heap = [HeapEntry((start_pos,), 0, frozenset())]
    seen_states: dict[tuple[tuple[complex, ...], frozenset[str]], int] = {((start_pos,), frozenset()): 0}

    while heap:
        entry = heapq.heappop(heap)
        if seen_states.get((entry.pos, entry.collected), math.inf) < entry.dist:
            continue
        if entry.collected == total_keys:
            return entry.dist

        # entry.pos is a 1-tuple holding the single position for part_1
        cur_pos = entry.pos[0]
        for target_pos, (dstep, required_doors) in nodes[cur_pos].items():
            key_ch = grid[target_pos]
            if key_ch in entry.collected:
                continue

            if not all(door.lower() in entry.collected for door in required_doors):
                continue

            new_collected = frozenset(set(entry.collected) | {key_ch})
            nd = entry.dist + dstep
            state = ((target_pos,), new_collected)
            if nd < seen_states.get(state, 10**18):
                seen_states[state] = nd
                heapq.heappush(heap, HeapEntry((target_pos,), nd, new_collected))

    raise ValueError("no solution")


def part_2(txt: str) -> int:
    # build grid
    grid = {complex(x, y): c for y, row in enumerate(txt.splitlines()) for x, c in enumerate(row)}
    # find original start and key positions
    start = mi.one(pos for pos, c in grid.items() if c == "@")
    key_positions = {c: pos for pos, c in grid.items() if c.islower()}

    # modify map for 4-robot scenario: replace start and its adjacents with walls,
    # place robots at the four diagonals
    deltas = [(-1 - 1j), (1 - 1j), (-1 + 1j), (1 + 1j)]
    # set center and 4-adjacent to walls
    grid[start] = "#"
    for d in (1, -1, 1j, -1j):
        grid[start + d] = "#"

    robot_positions = []
    for d in deltas:
        pos = start + d
        robot_positions.append(pos)
        grid[pos] = "@"

    # build nodes from each robot start and each key
    sources = [*key_positions.values(), *robot_positions]
    nodes = {pos: {kpos: (dist, doorset) for kpos, (dist, doorset) in bfs_from(pos, grid).items()} for pos in sources}

    total_keys = frozenset(key_positions.keys())

    # Dijkstra over ((pos1,pos2,pos3,pos4), collected_keys)
    heap = [HeapEntry(tuple(robot_positions), 0, frozenset())]
    seen_states: dict[tuple[tuple[complex, ...], frozenset[str]], int] = {(tuple(robot_positions), frozenset()): 0}

    while heap:
        entry = heapq.heappop(heap)
        dist, positions, collected = entry.dist, entry.pos, entry.collected
        if seen_states.get((positions, collected), math.inf) < dist:
            continue
        if collected == total_keys:
            return dist

        # for each robot, consider reachable keys
        for i, robot_pos in enumerate(positions):
            for target_pos, (dstep, required_doors) in nodes.get(robot_pos, {}).items():
                key_ch = grid[target_pos]
                if key_ch in collected:
                    continue

                if not all(door.lower() in collected for door in required_doors):
                    continue

                new_collected = frozenset(set(collected) | {key_ch})
                nd = dist + dstep
                new_positions = list(positions)
                new_positions[i] = target_pos
                new_positions_t = tuple(new_positions)
                state = (new_positions_t, new_collected)
                if nd < seen_states.get(state, 10**18):
                    seen_states[state] = nd
                    heapq.heappush(heap, HeapEntry(new_positions_t, nd, new_collected))

    raise ValueError("no solution")


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
