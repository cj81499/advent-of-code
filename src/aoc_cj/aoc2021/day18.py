import abc
import dataclasses
import itertools
from collections.abc import Iterator
from math import ceil, floor
from typing import Optional, override

import more_itertools as mi


@dataclasses.dataclass
class TreeNode(abc.ABC):
    parent: Optional["PairNode"]

    @abc.abstractmethod
    def magnitude(self) -> int:
        pass

    def reduce(self) -> "TreeNode":
        while self.reduce_once():
            pass
        return self

    def reduce_once(self) -> bool:
        if to_explode := next(self._explodable(), None):
            to_explode.explode()
            return True
        if to_split := next(self._splitable(), None):
            to_split.split()
            return True
        return False

    def root(self) -> "TreeNode":
        traverse = self
        while traverse.parent is not None:
            traverse = traverse.parent
        return traverse

    def replace_with(self, other: "TreeNode") -> None:
        p = self.parent
        assert p is not None
        if p.left is self:
            p.left = other
        elif p.right is self:
            p.right = other

    def add(self, other: "TreeNode") -> "TreeNode":
        return PairNode(None, self, other).reduce()

    @abc.abstractmethod
    def _explodable(self, depth: int = 0) -> Iterator["PairNode"]:
        pass

    @abc.abstractmethod
    def _in_order_traverse(self) -> Iterator["TreeNode"]:
        pass

    @abc.abstractmethod
    def _splitable(self) -> Iterator["ValueNode"]:
        pass


@dataclasses.dataclass
class PairNode(TreeNode):
    left: TreeNode
    right: TreeNode

    def __post_init__(self) -> None:
        self.left.parent = self
        self.right.parent = self

    @override
    def magnitude(self) -> int:
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    @override
    def _explodable(self, depth: int = 0) -> Iterator["PairNode"]:
        if depth > 4:
            return  # too deep
        yield from self.left._explodable(depth + 1)
        if depth == 4:
            yield self
        yield from self.right._explodable(depth + 1)

    @override
    def _splitable(self) -> Iterator["ValueNode"]:
        yield from self.left._splitable()
        yield from self.right._splitable()

    @override
    def _in_order_traverse(self) -> Iterator[TreeNode]:
        yield from self.left._in_order_traverse()
        yield self
        yield from self.right._in_order_traverse()

    def _surrounding_value_nodes(self) -> tuple[Optional["ValueNode"], Optional["ValueNode"]]:
        last_value_node = None
        seen_self = False
        for n in self.root()._in_order_traverse():
            if n is self:
                seen_self = True
            elif n.parent is self:
                continue
            elif isinstance(n, ValueNode):
                if seen_self:
                    return (last_value_node, n)
                else:
                    last_value_node = n

        return (last_value_node, None)

    def explode(self) -> None:
        assert isinstance(self.right, ValueNode)
        assert isinstance(self.left, ValueNode)
        left_value_node, right_value_node = self._surrounding_value_nodes()
        if left_value_node is not None:
            left_value_node.value += self.left.value
        if right_value_node is not None:
            right_value_node.value += self.right.value

        self.replace_with(ValueNode(self.parent, 0))

    @override
    def __repr__(self) -> str:
        return f"[{self.left},{self.right}]"


@dataclasses.dataclass
class ValueNode(TreeNode):
    value: int

    @override
    def magnitude(self) -> int:
        return self.value

    @override
    def _explodable(self, depth: int = 0) -> Iterator[PairNode]:
        yield from ()  # ValueNodes are never explodable

    @override
    def _splitable(self) -> Iterator["ValueNode"]:
        if self.value >= 10:
            yield self

    def split(self) -> None:
        half = self.value / 2

        p = self.parent
        assert p is not None
        new_pair = PairNode(p, ValueNode(None, floor(half)), ValueNode(None, ceil(half)))
        if p.left is self:
            p.left = new_pair
        elif p.right is self:
            p.right = new_pair

    @override
    def _in_order_traverse(self) -> Iterator[TreeNode]:
        yield self

    @override
    def __repr__(self) -> str:
        return str(self.value)


def parse(txt: str) -> TreeNode:
    it = mi.peekable(txt)
    return (parse_pair if it.peek() == "[" else parse_int)(it)


def parse_pair(it: "mi.peekable[str]") -> PairNode:
    assert next(it) == "["
    left = (parse_pair if it.peek() == "[" else parse_int)(it)
    assert next(it) == ","
    right = (parse_pair if it.peek() == "[" else parse_int)(it)
    assert next(it) == "]"
    return PairNode(None, left, right)


def parse_int(it: Iterator[str]) -> ValueNode:
    return ValueNode(None, int(next(it)))


def sum_lines(lines: list[str]) -> TreeNode:
    it = iter(lines)
    total = parse(next(it))
    for line in it:
        total = total.add(parse(line))
    return total


def part_1(txt: str) -> int:
    return sum_lines(txt.splitlines()).magnitude()


def part_2(txt: str) -> int:
    return max(parse(a).add(parse(b)).magnitude() for a, b in itertools.permutations(txt.splitlines(), 2))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
