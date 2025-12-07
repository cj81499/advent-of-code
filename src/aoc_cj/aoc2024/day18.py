import heapq
import itertools
from typing import Self

from aoc_cj import util


class HeapItem[T]:
    __slots__ = ("cost", "value")

    def __init__(self, cost: int, value: T) -> None:
        self.cost = cost
        self.value = value

    def __lt__(self, other: Self) -> bool:
        return self.cost < other.cost


class NoPathFoundError(Exception):
    """Error raised when no path from start to goal could be found"""


def part_1(txt: str, max_dim: int = 70, simulate: int = 1024) -> int:
    byte_positions = [x + y * 1j for x, y in map(util.ints, txt.splitlines())]
    start = 0j
    goal = max_dim + max_dim * 1j
    blocked = set(itertools.islice(byte_positions, simulate))
    return explore(max_dim, start, goal, blocked)


def explore(max_dim: int, start: complex, goal: complex, blocked: set[complex]) -> int:
    to_explore = [HeapItem(cost=0, value=start)]
    seen = set[complex]()
    while to_explore:
        item = heapq.heappop(to_explore)
        pos = item.value
        if pos in seen:
            continue
        if pos == goal:
            return item.cost
        for adj_pos in util.adj_4(pos):
            # if position in bounds and is not blocked
            if 0 <= adj_pos.real <= max_dim and 0 <= adj_pos.imag <= max_dim and adj_pos not in blocked:
                heapq.heappush(to_explore, HeapItem(cost=item.cost + 1, value=adj_pos))
        seen.add(pos)
    raise NoPathFoundError


def part_2(txt: str, max_dim: int = 70) -> str:
    byte_positions = [x + y * 1j for x, y in map(util.ints, txt.splitlines())]
    start = 0j
    goal = max_dim + max_dim * 1j

    # use binary search to find the first element in byte_positions that'll cut
    # off all paths from start to goal.
    # a linear search would work, but is quite a bit slower.
    left = 0
    right = len(byte_positions) - 1
    result: complex | None = None
    while left <= right:
        mid = (left + right) // 2
        blocked = set(byte_positions[: mid + 1])
        try:
            explore(max_dim, start, goal, blocked)
        except NoPathFoundError:
            # no path found. The element must not be further to the right
            result = byte_positions[mid]
            right = mid - 1
        else:
            # path found. The element must be further to the right
            left = mid + 1
    assert result is not None

    return f"{int(result.real)},{int(result.imag)}"


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
