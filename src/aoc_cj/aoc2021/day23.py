import json
import textwrap
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Literal, Optional, Union

from typing_extensions import TypeGuard

from aoc_cj.util import PriorityQueue

GOAL_STATE_STR = """
#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########
""".strip(
    "\n"
)

PART_B = """
  #D#C#B#A#
  #D#B#A#C#
""".strip(
    "\n"
)

Amphipod = Union[Literal["A"], Literal["B"], Literal["C"], Literal["D"]]
GridEntry = Union[Amphipod, Literal["."]]

ENERGY_COST = {"A": 1, "B": 10, "C": 100, "D": 1000}
ROOM_GOALS = {"A": 0, "B": 1, "C": 2, "D": 3}

ROOM_X = dict(zip("ABCD", range(2, 8 + 1, 2)))


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def adj(self) -> Iterator["Point"]:
        yield Point(self.x, self.y - 1)
        yield Point(self.x, self.y + 1)
        yield Point(self.x - 1, self.y)
        yield Point(self.x + 1, self.y)

    def in_hallway(self) -> bool:
        return self.y == 0


OUTSIDE_OF_ROOM = {Point(x, 1) for x in ROOM_X.values()}


def is_grid_entry(c: str) -> TypeGuard[GridEntry]:
    return c == "." or is_amphipod(c)


def is_amphipod(c: str) -> TypeGuard[Amphipod]:
    return c in ENERGY_COST


class Burrow:
    def __init__(self, grid: dict[Point, GridEntry]):
        self._grid = grid

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Burrow):
            return False
        return self._grid == other._grid

    def __hash__(self) -> int:
        simple_grid = {f"({p.x}, {p.y})": v for p, v in self._grid.items()}
        return hash(json.dumps(simple_grid, sort_keys=True))

    def next_moves(self) -> Iterator[tuple["Burrow", int]]:
        # for each amphipod
        for p, a in self._amphipod_points():
            # TODO: optimization: if the amphipod is not in its final position
            # yield a burrow for each move that amphipod could make
            yield from self._move_amphipod(p)

    def _amphipod_points(self) -> Iterator[tuple[Point, Amphipod]]:
        yield from ((p, val) for p, val in self._grid.items() if is_amphipod(val))

    def _move_amphipod(self, p: Point) -> Iterator[tuple["Burrow", int]]:
        for reachable_p, steps in self._reachable(p):
            # hallway -> hallway moves are illegal
            if p.in_hallway() and reachable_p.in_hallway():
                continue
            # never stop immediately outside room
            if reachable_p in OUTSIDE_OF_ROOM:
                continue
            amphipod = self._grid[p]
            if not reachable_p.in_hallway():
                # don't move from hallway into room unless it's destination
                if ROOM_X[amphipod] != reachable_p.x:
                    continue
                # don't block in an amphipod that doesn't belong in room
                if p.y == 1 and self._grid[Point(p.x, 2)] != amphipod:
                    continue

            # yield (burrow, cost)
            yield self._burrow_with_swaped(p, reachable_p), ENERGY_COST[amphipod] * steps

    def _reachable(self, p: Point) -> Iterator[tuple[Point, int]]:
        to_explore: set[tuple[Point, int]] = {(p, 0)}
        explored = set()
        while to_explore:
            exploring, steps = to_explore.pop()
            next_steps = steps + 1
            for adj_p in exploring.adj():
                if self._grid.get(adj_p, "") == "." and adj_p not in explored:
                    to_explore.add((adj_p, next_steps))
                    yield adj_p, next_steps
            explored.add(exploring)

    def _burrow_with_swaped(self, p1: Point, p2: Point) -> "Burrow":
        new_grid = self._grid | {p1: self._grid[p2], p2: self._grid[p1]}
        return Burrow(new_grid)

    @staticmethod
    def parse(string: str) -> "Burrow":
        grid: dict[Point, GridEntry] = {}
        s = textwrap.dedent(string.replace("#", " ")).strip("\n")
        for y, line in enumerate(s.splitlines()):
            for x, c in enumerate(line):
                if is_grid_entry(c):
                    grid[Point(x, y)] = c
        return Burrow(grid)

    def __str__(self) -> str:
        min_x = min(p.x for p in self._grid)
        max_x = max(p.x for p in self._grid)
        min_y = min(p.y for p in self._grid)
        max_y = max(p.y for p in self._grid)

        return "\n".join(
            "".join(self._grid.get(Point(x, y), " ") for x in range(min_x, max_x + 1)) for y in range(min_y, max_y + 1)
        )


GOAL_STATE = Burrow.parse(GOAL_STATE_STR)


def parta(txt: str) -> int:
    seen: set[Burrow] = set()
    pq: PriorityQueue[Burrow] = PriorityQueue()
    pq.push(0, Burrow.parse(txt))

    min_cost: Optional[int] = None
    while pq:
        item = pq.pop()
        cost, current = item.priority, item.item
        if current in seen:
            continue
        if current == GOAL_STATE:
            min_cost = cost if min_cost is None else min(cost, min_cost)
            continue
        print(current)
        print(cost)
        print()
        if min_cost and cost > min_cost:
            return min_cost
        for next_b, c in current.next_moves():
            if next_b not in seen:
                pq.push(cost + c, next_b)
        seen.add(current)

    assert min_cost is not None
    return min_cost


def partb(txt: str) -> None:
    *rest, second_to_last, last = txt.splitlines()
    new_text = "\n".join((*rest, *PART_B.splitlines(), second_to_last, last))
    print(new_text)
    b = Burrow.parse(new_text)
    print(b)
    print(b._grid)


def main(txt: str) -> None:
    # txt = GOAL_STATE_STR
    print(f"parta: {parta(txt)}")
    # print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
