import dataclasses
import itertools
import re
from typing import NamedTuple

import more_itertools as mi


class Point(NamedTuple):
    x: int
    y: int


@dataclasses.dataclass(frozen=True)
class Node:
    point: Point
    size: int
    used: int

    __PATTERN = re.compile(r"(?P<fs>[\w\d\/-]+) *(?P<size>\d+)T *(?P<used>\d+)T *(?P<avail>\d+)T *(?P<percent>\d+)%")
    PREFIX = "/dev/grid/node"

    @staticmethod
    def parse(node: str) -> "Node":
        match = Node.__PATTERN.match(node)
        assert match is not None
        size, used, avail = map(int, match.group("size", "used", "avail"))
        assert size - used == avail
        *_, x, y = match.group("fs").split("/")[-1].split("-")[-2:]
        point = Point(int(x[1:]), int(y[1:]))
        return Node(point, size, used)

    @property
    def avail(self) -> int:
        return self.size - self.used

    def is_empty(self) -> bool:
        return self.used == 0


def part_1(txt: str) -> int:
    nodes = [Node.parse(line) for line in txt.splitlines() if line.startswith(Node.PREFIX)]
    return sum(a.used != 0 and a.used <= b.avail for a, b in itertools.permutations(nodes, 2))


def part_2(txt: str) -> int:
    grid = {(n := Node.parse(line)).point: n for line in txt.splitlines() if line.startswith(Node.PREFIX)}
    max_x, _max_y = max(grid)

    # use empty node to move data where we want
    empty_nodes = {n for n in grid.values() if n.used == 0}
    empty_node = mi.one(empty_nodes)  # there is only 1 empty node in my input

    # first, empty node must be moved next to goal data
    goal_pos = Point(max_x, 0)
    empty_node_pos = empty_node.point

    # detect the example input
    is_example = goal_pos == Point(2, 0)
    if is_example:
        # in the example, we move twice to get the empty node to the top right
        # corner of the grid, moving the goal 1 to the left in the process
        steps = 2
    else:
        # in my input there's a horizontal "wall" of nodes
        # the empty data must move around (by going all the way to the left)
        steps = (
            empty_node_pos.x  # go all the way to the left (to get around the wall)
            + empty_node_pos.y  # go all the way to the top
            + goal_pos.x  # go all the way to the right, moving the goal 1 to the left in the process
        )

    # moving goal data left one node takes 5 steps
    # it must be moved max_x - 1 more times (it's already been moved left once)
    steps += (max_x - 1) * 5  # remaining steps

    return steps


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
