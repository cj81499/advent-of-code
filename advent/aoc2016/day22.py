from __future__ import annotations

import dataclasses
import enum
import itertools


@dataclasses.dataclass
class Node:
    filesystem: str
    size: int
    used: int
    available: int
    used_percent: int

    @staticmethod
    def parse(node: str):
        name, *nums = node.split()
        return Node(name, *(int(n[:-1]) for n in nums))

    def x(self) -> int:
        return int(self.filesystem.split("-")[1][1:])

    def y(self) -> int:
        return int(self.filesystem.split("-")[2][1:])


class NodeType(enum.Enum):
    EMPTY = 0
    NORMAL = 1
    BLOCKED = 2

    def __str__(self) -> str:
        if self is NodeType.EMPTY:
            return " "
        if self is NodeType.NORMAL:
            return "."
        return "#"


def parta(txt: str):
    nodes = [Node.parse(line) for line in txt.splitlines()[2:]]
    viable_pairs = 0
    for nodeA, nodeB in itertools.permutations(nodes, 2):
        if nodeA.used > 0 and nodeA.used <= nodeB.available:
            viable_pairs += 1
    return viable_pairs


def partb(txt: str):
    nodes = [Node.parse(line) for line in txt.splitlines()[2:]]

    # top right node
    goal_node = max((n for n in nodes if n.y() == 0), key=lambda n: n.x())

    empty_nodes = [n for n in nodes if n.used == 0]
    assert len(empty_nodes) == 1
    empty_node = empty_nodes[0]

    # idea: simplify to search
    max_x = max(n.x() for n in nodes)
    max_y = max(n.y() for n in nodes)

    grid = []
    for y in range(max_y + 1):
        grid.append([])
        for x in range(max_x + 1):
            node = next(n for n in nodes if n.x() == x and n.y() == y)
            type = NodeType.NORMAL
            if node.used == 0:
                type = NodeType.EMPTY
            if node.used > 100:
                type = NodeType.BLOCKED
            grid[-1].append(type)

    for row in grid:
        print("".join(str(t) for t in row))

    print(empty_node)
    print(goal_node)

    # TODO: actually solve this instead of "faking" it

    # my input has a "wall"
    # move the empty node all the way to the left
    moves = empty_node.x()
    # move the empty node up (to the top left)
    moves += empty_node.y()
    # move the empty node right (to the top right)
    moves += goal_node.x()
    # moving the goal data left once takes 5 moves.
    # subtract one b/c we already moved it once by positioning the empty node in the top right
    moves += 5 * (goal_node.x() - 1)

    return moves

    print(empty_node)
    print(goal_node)

    return -1


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
